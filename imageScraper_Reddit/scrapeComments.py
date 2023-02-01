import pandas as pd
import praw
from praw.models import MoreComments
reddit = praw.Reddit(user_agent="Comment Extraction (by /u/SageMode00)",
                     client_id="CxYuVD9eqn7MSB96p-iuQA", client_secret="Bix79KOMrBUjaPFqK1gHfGC5uHVtUg")


"""
url = "https://www.reddit.com/r/UpliftingNews/comments/lemy1b/student_who_made_30k_from_gamestop_donates_games/"
submission = reddit.submission(url=url)
posts = []
for top_level_comment in submission.comments[1:]:
    if isinstance(top_level_comment, MoreComments):
        continue
    posts.append(top_level_comment.body)
posts = pd.DataFrame(posts,columns=["body"])

"""

posts = []
for submission in reddit.subreddit("UpliftingNews").top("all"):
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        posts.append(top_level_comment.body)
posts = pd.DataFrame(posts,columns=["body"])


indexNames = posts[(posts.body == '[removed]') | (posts.body == '[deleted]')].index
posts.drop(indexNames, inplace=True)
print(posts)