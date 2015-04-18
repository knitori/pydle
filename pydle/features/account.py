## account.py
# Account system support.
from pydle.features import rfc1459

class AccountSupport(rfc1459.RFC1459Support):

    ## Internal.

    def _rename_user(self, user, new):
        super()._rename_user(user, new)
        # Unset account info.
        user = self.users[new]
        user.account = None
        user.identified = False


    ## IRC API.

    def whois(self, nickname):
        future = super().whois(nickname)

        # Add own info.
        if nickname in self._whois_info:
            whois_info = self._whois_info[nickname]
            whois_info.account = None
            whois_info.identified = False

        return future


    ## Message handlers.

    def on_raw_307(self, message):
        """ WHOIS: User has identified for this nickname. (Anope) """
        target, nickname = message.params[:2]

        if nickname in self.users:
            user = self._get_or_create_user(nickname)
            user.identified = True
        if nickname in self._pending_whois:
            whois_info = self._whois_info[nickname]
            whois_info.identified = True

    def on_raw_330(self, message):
        """ WHOIS account name (Atheme). """
        target, nickname, account = message.params[:3]

        if nickname in self.users:
            user = self._get_or_create_user(nickname)
            user.account = nickname
            user.identified = True
        if nickname in self._pending_whois:
            whois_info = self._whois_info[nickname]
            whois_info.account = account
            whois_info.identified = True
