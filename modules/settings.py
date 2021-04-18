from .keys import keys
from praw import Reddit
class Settings:
    DISCORD_TOKEN = keys["DISCORDTOKEN"]
    CLIENT_ID = keys["CLIENTID"]
    CLIENT_SECRET = keys["CLIENTSECRET"]
    POST_LIMIT = 21
    SUB_REDDIT= "memes"
    BOT_NAME = "AdvanceBot"

def loadReddit():
    reddit = Reddit(
        client_id=Settings.CLIENT_ID,
        client_secret=Settings.CLIENT_SECRET,
        user_agent=Settings.BOT_NAME,
    )
    return reddit
def getPostLimit():
    return Settings.POST_LIMIT

def getSubreddits():
    return Settings.SUB_REDDIT


def runClient(Client):
    discord = Client
    discord.run(Settings.DISCORD_TOKEN)
    # discordclient.run(keys["DISCORDTOKEN"]).