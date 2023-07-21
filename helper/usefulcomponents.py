import praw

# components for readable code

class Components:
    def __init__(self, reddit):
        self = self
        self.reddit = reddit
    def new_submissions(self):
        submissions = self.reddit.subreddit("theletterh").stream.submissions(skip_existing=True)
        return submissions
    def new_mentions(self):
        mentions = self.reddit.inbox.mentions
        return praw.models.util.stream_generator(mentions, skip_existing=True)