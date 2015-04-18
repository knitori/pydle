class User:
    def __init__(self, client, nickname, realname=None, username=None, hostname=None):
        self.client = client
        self.nickname = nickname
        self.realname = realname
        self.username = username
        self.hostname = hostname

    @property
    def name(self):
        return self.nickname

    @property
    def hostmask(self):
        return '{n}!{u}@{h}'.format(n=self.nickname, u=self.username or '*', h=self.hostname or '*')


class Channel:
    def __init__(self, client, name):
        self.client = client
        self.name = name
        self.users = set()


class Server:
    def __init__(self, name):
        self.name = name
