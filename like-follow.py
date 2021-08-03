"""
    ULTIMATE SCRIPT

    It uses data written in files:
        * follow_followers.txt
        * follow_following.txt
        * like_hashtags.txt
        * like_users.txt
    and do the job. This bot can be run 24/7.
"""

import os
import sys
import time
sys.path.append(os.path.join(sys.path[0], "../../"))
from instabot import Bot  # noqa: E402
sys.stdout = open('output.txt', 'w')
bot = Bot()
bot.login(username='', password='')

print("Current script's schedule:")
like_hashtags_list = bot.read_list_from_file("like_hashtags.txt")
print("Going to like hashtags:", like_hashtags_list)
wait = 1 * 60  # in seconds
tasks_list = []
for item in like_hashtags_list:
    tasks_list.append((bot.like_hashtag, {"hashtag": item, "amount": None }))
    time.sleep(wait)
    #users=tasks_list.append((bot.get_hashtag_users, {"hashtag": item, "amount":None }))
    users = bot.get_hashtag_users(item)
    bot.follow_users(users)
sys.stdout.close()
time.sleep(wait)
# shuffle(tasks_list)
for func, arg in tasks_list:
    func(**arg)
