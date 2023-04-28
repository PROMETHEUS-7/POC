from entity.tweet import Tweet
from entity.user import User
from entity.category import Category


class TweetService:
    # Get My Tweet List. Method = GET
    def get_user_tweets_list(self, user_id):
        tweets = [Tweet(tweet_id=11, title="My Tweet Example",
                        category=Category(category_id=1, name="Science").__dict__,
                        created_by=User(user_id=10, name="John").__dict__),
                  Tweet(tweet_id=12, title="My Tweet Example 2",
                        category=Category(category_id=2, name="Politics").__dict__,
                        created_by=User(user_id=10, name="John").__dict__),
                  Tweet(tweet_id=13, title="My Tweet Example 3",
                        category=Category(category_id=3, name="Entertainment").__dict__,
                        created_by=User(user_id=10, name="John").__dict__)]
        return tweets  # DONE

    # Get Popular Tweet List. Method = GET
    def get_popular_tweets_list(self):
        tweets = [Tweet(tweet_id=11, title="My Tweet Example",
                        category=Category(category_id=1, name="Science").__dict__,
                        created_by=User(user_id=10, name="John").__dict__),
                  Tweet(tweet_id=12, title="My Tweet Example 2",
                        category=Category(category_id=2, name="Politics").__dict__,
                        created_by=User(user_id=10, name="John").__dict__),
                  Tweet(tweet_id=13, title="My Tweet Example 3",
                        category=Category(category_id=3, name="Entertainment").__dict__,
                        created_by=User(user_id=10, name="John").__dict__)]
        return tweets  # DONE

    # Get Single Tweet. Method = GET
    def get_tweet(self, tweet_id):
        tweet = Tweet(tweet_id, title="Get Single Tweet Test",
                      category=Category(category_id=1, name="Science").__dict__,
                      content="Content of tweet",created_by=User(user_id=10, name="John").__dict__)
        if tweet_id == 10:  # ask Jinaraj if this is correct
            return tweet  # DONE

    # Create Tweet. Method = POST
    def create_tweet(self, title, created_by, content, category):
        return True  # DONE

    # Get Tweet By Category. Method = GET
    def get_tweet_by_category(self, category_id):
        tweets = [
            Tweet(tweet_id=11, title="My Tweet Example", category=Category(category_id=category_id).__dict__,
                  created_by=User(user_id=10, name="John").__dict__),
            Tweet(tweet_id=12, title="My Tweet Example 2", category=Category(category_id=category_id).__dict__,
                  created_by=User(user_id=10, name="John").__dict__),
            Tweet(tweet_id=13, title="My Tweet Example 3",category=Category(category_id=category_id).__dict__,
                  created_by=User(user_id=10, name="John").__dict__)]
        if category_id == 10:
            return tweets

