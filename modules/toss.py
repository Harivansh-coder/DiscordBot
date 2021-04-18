import random

async def toss(message):
    await message.channel.send(random.choice(["heads","tails"]))

