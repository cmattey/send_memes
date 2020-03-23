from flask import Flask, request

app = Flask(__name__)

from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from reddit_wrapper import get_image_memes
import random
import os

@app.route('/')
def hello():
    return "whale veil well!"

@app.route('/get_memes', methods=["GET", "POST"])
def get_memes():
    """
    Respond to incoming requests by sending a meme
    """

    resp = MessagingResponse()
    body = request.values.get('Body', None)

    funny_remarks = ["haha", "lol", "xD", "lmao", "rofl"]
    asking_for_memes = ["meme", "laugh", "funny"]
    if body and any([st in body.lower() for st in funny_remarks]):
        resp.message("Glad you found that funny :)")
        return str(resp)

    elif body and any([st in body.lower() for st in asking_for_memes]):
        meme_subreddits = ['memeeconomy', 'wholesomememes', 'dankmemes', 'meirl']
        subreddit = random.choice(meme_subreddits)

        try:
            memes = get_image_memes(subreddit, 100)
        except:
            return jsonify({'message':'Error Occured'})

        random_meme = random.choice(memes)
        msg = resp.message(random_meme['title'])
        msg.media(random_meme['url'])
        return str(resp)
    else:
        resp.message("I can only send memes, try asking me for a meme")
        return str(resp)

if __name__ == '__main__':
    app.run()
