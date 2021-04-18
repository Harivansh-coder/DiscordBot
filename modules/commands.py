from .toss import toss
from .help import help
from .memes import memes
async def pong(message):
    await message.channel.send("pong")

commands = {
    "!help":help,
    "!ping":pong,
    "!memes":memes,
    "!toss":toss 
}