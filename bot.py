import praw
import time
import requests
import config

reddit_username = config.reddit['username']
reddit_password = config.reddit['password']
reddit_id = config.reddit['id']
reddit_secret = config.reddit['secret']
reddit_subreddit = config.reddit['subreddit']

telegram_auth_token = config.telegram['auth_token']
telegram_group_id = config.telegram['group_id']

bot_launch_time = time.time()

# Stream bot API
reddit = praw.Reddit(client_id = reddit_id,
                     client_secret = reddit_secret,
                     username = reddit_username,
                     password = reddit_password,
                     user_agent = "pythonpraw")

subreddit = reddit.subreddit(reddit_subreddit)

def send_message(message):
    telegram_api_url = f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id=@{telegram_group_id}&text={message}"
    tel_resp = requests.get(telegram_api_url)

for submission in subreddit.stream.submissions():
    if submission.created_utc > bot_launch_time:
        # Chat bot send message
        if "[uk]" in submission.title.lower():
            print(f"New Post: {submission.title}")
            send_message(f"Post: {submission.title} \n"
            f"Link: reddit.com{submission.permalink}")


messageBot.run_4ever(auto_reconnect=True)
