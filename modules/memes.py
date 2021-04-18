from .settings import loadReddit, getPostLimit, getSubreddits
import random

def get_memes():
    """Function to get and post memes in a discord server """
    reddit = loadReddit()
    postLimit = getPostLimit()
    subreddit = reddit.subreddit(getSubreddits())
    posts = subreddit.hot(limit=postLimit)
    image_urls, image_titles = [], []

    for post in posts:
        image_urls.append(post.url.encode("utf-8"))
        image_titles.append(post.title.encode("utf-8"))

    lenUrl = len(image_urls)
    image_urls = [i.decode('utf-8') for i in image_urls]
    return image_urls[random.randint(0, postLimit - 1)]


async def memes(message):
    
    await message.channel.send(get_memes())
