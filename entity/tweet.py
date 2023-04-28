class Tweet:
    def __init__(self, tweet_id, title, category=None, content=None, created_by=None):
        self.tweet_id = tweet_id
        self.title = title
        self.content = content
        self.category = category
        self.created_by = created_by
