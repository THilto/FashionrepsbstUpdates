import praw
import time
import requests
import config

# Reddit login data
reddit_username = config.reddit['username']
reddit_password = config.reddit['password']
reddit_id = config.reddit['id']
reddit_secret = config.reddit['secret']
reddit_subreddit = config.reddit['subreddit']

# Telegram data
telegram_auth_token = config.telegram['auth_token']
telegram_group_id = config.telegram['group_id']

bot_launch_time = time.time()

# Messages parameters, used so telegram doesn't get confused with '&'
message_params = {
    "chat_id": telegram_group_id,
    "text": "",
}

# Stream bot API
reddit = praw.Reddit(client_id = reddit_id,
                     client_secret = reddit_secret,
                     username = reddit_username,
                     password = reddit_password,
                     user_agent = "pythonpraw")

subreddit = reddit.subreddit(reddit_subreddit)

# Telegram
def send_message(message):
    message_params["text"] = message
    requests.get(f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage", params=message_params)

# New posts stream
for submission in subreddit.stream.submissions():
    if submission.created_utc > bot_launch_time:
        # Chat bot send message
        if "[uk]" in submission.title.lower():
            print(f"New Post: {submission.title}")
            send_message(f"Post: {submission.title} \n"
            f"Link: reddit.com{submission.permalink}")