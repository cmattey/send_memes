import praw
import random
import os

class ClientInfo:
    id = os.environ.get('REDDIT_CLIENT_ID')
    secret = os.environ.get('REDDIT_CLIENT_SECRET')
    user_agent = 'send memes'

def is_image_meme(media_url):

    extension = media_url[-4:]

    if extension in ('.jpg', '.png'):
        return True

    return False

def get_image_memes(sub, count):

    reddit = praw.Reddit(client_id=ClientInfo.id, client_secret=ClientInfo.secret,
                    user_agent=ClientInfo.user_agent)

    candidates = reddit.subreddit(sub).hot(limit=count)

    memes = []
    for candidate in candidates:
        if is_image_meme(candidate.url):
            memes.append({"title": candidate.title,
                          "url": candidate.url,
                          "link": candidate.shortlink})

    return memes
