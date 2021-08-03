"""
    instabot example

    Workflow:
        Follow users who post medias with hashtag.
"""

import argparse
import os
import sys
import time
sys.stdout = open('output.txt', 'w')
sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402
sys.path.append(os.path.join(sys.path[0], "comments.txt/comments_emoji.txt/"))
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")
parser.add_argument("hashtags", type=str, nargs="+", help="hashtags")
args = parser.parse_args()
if len(sys.argv) < 3:
    print("USAGE: Pass a path to the file with comments " "and a hashtag to comment")
    print("Example: %s pytho dog cat" % sys.argv[0])
    exit()
comments_file_name = sys.argv[1]
hashtags = sys.argv[2:]
bot = Bot(comments_file=comments_file_name)
bot.login(username='', password='', proxy=args.proxy)

wait = 1 * 60  # in seconds

while True:
    for hashtag in args.hashtags:
        bot.like_hashtag(hashtag)
        bot.comment_hashtag(hashtag)
        users = bot.get_hashtag_users(hashtag)
        bot.follow_users(users)   
sys.stdout.close()
time.sleep(wait)
bot.logout()

