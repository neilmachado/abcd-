import praw 
import time
import pyfiglet
import random 
import requests
import sys
from sys import exit



reddit = praw.Reddit(client_id="v0Pz31H8ifemvg", #14 letter key
                     client_secret="6qR4HFiQ1GsqOjK8mzS_9NKW8wTSuQ", #27 letter key
                     password="12345678",
                     user_agent="testscript by u/Proof-Slice3328",
                     username="Proof-Slice3328")
 
result = pyfiglet.figlet_format("Dylan OP") 
print(result) 

print("Starting Magic............")

print(reddit.user.me())

REDDIT_USERNAME=(reddit.user.me())

response = requests.get("https://www.reddit.com/user/{}/about.json".format(REDDIT_USERNAME),  headers = {'User-agent': 'hiiii its {}'.format(REDDIT_USERNAME)}).json()
if "error" in response:
 if response["error"] == 404:
      print("account {} is shadowbanned. poor bot :( shutting down the script...".format(REDDIT_USERNAME))
      sys.exit()
 else:
      print(response)
else:
    print("{} is not shadowbanned! We think..".format(REDDIT_USERNAME))

name = input("Enter a name : ") 

title = input("Enter an epic title: ") 
url = input("Enter a sassy link: ") 
comment = input ("Enter your comment : ")


print("Reading reddit list")
subredit_list = open("data.txt", "r")
subreddits = subredit_list.read().split(',')

for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title,url=url)
    com = " [click here:]({}) {}".format(comment, name)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(15,25)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)