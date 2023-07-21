import praw

# components for readable code

class Components:
    def __init__(self, reddit):
        self = self
        self.reddit = reddit
    def new_submissions(self):
        submissions = self.reddit.subreddit("theletterh").stream.submissions(skip_existing=True)
        return submissions
    def check_if_post_is_valid(self, submission):
        repliers = []
        for tlc in submission.comments:
            for reply in tlc.replies:
                repliers.append(reply.author)
            if tlc.author == "h-bot9000" and "h-bot10000" not in repliers:
                return True
            elif tlc.author != "h-bot9000" or "h-bot10000" in repliers:
                return False
    def new_mentions(self):
        mentions = self.reddit.inbox.mentions
        return praw.models.util.stream_generator(mentions, skip_existing=True)
