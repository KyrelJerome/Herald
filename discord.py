from bot import PostBot

class DiscordBot(PostBot):

    def __init__(self, secret):
        self.password = secret
        self.

    def post(self, description, images):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

