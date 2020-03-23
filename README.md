# Send MEMES
Meme server using Twilio and PRAW

> Usecase
![Example](https://github.com/cmattey/send_memes/blob/master/imgsrc/ss.jpeg)

## Usage
- Just send a message to the Twilio Number asking for memes, Eg: "Meme me!"
- Since I'm currently using a Trial account, the app only works for my number :)

## Setup
- install requirements using
```sh
pip install -r requirements.txt
```

- ![create](http://twilio.com/try-twilio) a Twilio account
- Buy a Number
- ![register](https://www.reddit.com/prefs/apps/) an application on reddit

- export the necessary env variables in your terminal instance:
```sh
export TWILIO_ACCOUNT_SID="xyz"
...
```
It's better to store all your environment variables into a .env or .flaskenv file so you
don't have to export env variables every time you reopen the terminal

- Click on your active number and under "Messaging" configure the webhook for "When a Message comes in",
to point to you application. The webhook won't be able to locate your localhost,
so either expose it using ngrok, or host the app on heroku, and provide that link here.

- Send a message to your Twilio Number from your number (which you used to register, if you're using a Trial account)
