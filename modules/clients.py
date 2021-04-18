from discord import Client
from .settings import runClient
from .commands import commands
class Discord(Client):
    async def on_ready(self):
        print("I am ready")

    async def on_message(self, message):
        if message.author == self.user:
            return
        func = commands.get(message.content)
        if func:
            await func(message)

def initClient():
    client = Discord()
    runClient(client)