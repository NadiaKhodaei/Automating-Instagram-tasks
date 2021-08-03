"""
    instabot example

    Dependencies:
        You must have a file with comments to post.
        The file should have one comment per line.

    Notes:
        You can change file and add there your comments.
"""

import os
import sys
import threading
import time
import argparse
import config
sys.path.append(os.path.join(sys.path[0], "comments.txt/comments_emoji.txt/"))
from instabot import Bot  # noqa: E402
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("hashtags", type=str, nargs="+", help="hashtags")
args = parser.parse_args()

if len(sys.argv) < 3:
    print("USAGE: Pass a path to the file with comments " "and a hashtag to comment")
    print("Example: %s pytho dog cat" % sys.argv[0])
    exit()

comments_file_name = sys.argv[1]
hashtags = sys.argv[2:]
if not os.path.exists(comments_file_name):
    print("Can't find '%s' file." % comments_file_name)
    exit()
wait = 1 * 60  # in seconds
bot = Bot(comments_file=comments_file_name)
bot.login(username='', password='')
for hashtag in hashtags:
    bot.comment_hashtag(hashtag)
bot.logout()
