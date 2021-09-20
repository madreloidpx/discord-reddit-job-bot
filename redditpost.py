class RedditPost:
    def __init__(self, reddit_id, url, subreddit, title, flair):
        self.reddit_id = reddit_id
        self.url = url
        self.subreddit = subreddit
        self.title = title
        self.flair = flair
    def checkContains(self, tag):
        if tag.lower() in self.title.lower():
            return True
        return False
    def printPost(self):
        print("["+self.subreddit+":"+self.reddit_id+"]", self.title, "(" + self.url +")")