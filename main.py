import praw
import random
import time

reddit = praw.Reddit(
    client_id="nyxpIckhxBEKcQoOqvvG5A",
    client_secret="IQeDYKdU92ZcTuf_guJf6j50M1cFjw",
    user_agent="<console:temporary:1.12>",
    username="temporary_bot",
    password="TemporaryBot1")

subreddit = reddit.subreddit("apple")

app_recommendations = ["Try using Helium",
                       "Try using Daily wall",
                       "Try using 5k video player",
                       "Try using Garage band",
                       "Try using Automator",
                       "Try using Keynote",
                       "Try using Numbers",
                       "Try using Stickies",
                       "Try using Pages",
                       "Try using iMovie",
                       "Try using Todoist",
                       "Try using Unsplash",
                       "Try using Drover",
                       "Try using Adobe acrobat reader",
                       "Try using xMind",
                       "Try using Among us",
                       "Try using Wonder-share pdf element",
                       "Try using Arduino",
                       "Try using Slide-pad",
                       "Try using Typing Dan focus",
                       "Try using powershell",
                       "Try using numi",
                       "Try using freecad",
                       "Try using matlab"]

for submission in subreddit.hot(limit=10):
    print("**********************")
    print(submission.title)
    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " app " in comment_lower:
                print("---------------------")
                print(comment.body)
                random_index = random.randint(0, len(app_recommendations) - 1)
                comment.reply(body=app_recommendations[random_index])
                # time.sleep(120)
