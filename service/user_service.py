# from entity.user import User

from service.tweet_service import TweetService


class UserService:
    # Registration
    def registration(self, user):
        with open('C:/Users/Admin/PycharmProjects/Quart/POC/storage/users.txt', 'r', newline='') as file:
            lines = file.readlines()
            if user.username in lines:
                return False
        user_list = []

        for line in lines:
            values = line.rstrip().split(',')
            user_dict = {
                'user_id': values[0],
                'name': values[1],
                'username': values[2],
                'password': values[3],
                'email': values[4],
                'designation': values[5],
                'role': values[6],
                'strike': values[7]
            }
            user_list.append(user_dict)
        last_id = user_list[-1]['user_id']
        if last_id.isdigit() is True:
            last_id = int(last_id)
        else:
            last_id = 0
        user.user_id = last_id + 1
        user_list.append(user.__dict__)

        # To Write into the file
        with open('C:/Users/Admin/PycharmProjects/Quart/POC/storage/users.txt', 'w', newline='') as file:
            for user in user_list:
                line = f"{user['user_id']},{user['name']},{user['username']},{user['password']}," \
                       f"{user['email']},{user['designation']},{user['role']},{user['strike']}\n"
                if user == user_list[-1]:
                    file.write(line.strip())
                else:
                    file.write(line)
        return True

    # Login. Method = POST
    def login(self, username, password):
        with open('C:/Users/Admin/PycharmProjects/Quart/POC/storage/users.txt', 'r', newline='') as file:
            user_profile = []
            for line in file:
                values = line.strip().split(',')
                if values[2] == username and values[3] == password:
                    return True

    # View Profile of any User. Method = GET
    def view_profile(self, user_id):
        with open('C:/Users/Admin/PycharmProjects/Quart/POC/storage/users.txt', 'r', newline='') as file:
            user_profile = []
            for line in file:
                values = line.strip().split(',')
                if values[0] == user_id:
                    user_dict = {
                        'user_id': values[0],
                        'name': values[1],
                        'username': values[2],
                        'password': values[3],
                        'email': values[4],
                        'designation': values[5],
                        'role': values[6],
                        'strike': values[7]
                    }
                    user_profile.append(user_dict)
                    return user_profile
            return False


    # Edit Profile
    def edit_profile(self, name, password):
        return True

    # Delete Profile
    def delete_profile(self, user_id):
        return True

    # Dashboard
    def dashboard(self, user_id):
        dashboard = {
            "Popular Tweets": TweetService().get_popular_tweets_list(),
            "My Tweets": TweetService().get_user_tweets_list(user_id)
        }
        return dashboard

    # Flag Tweet
    def flag_tweet(self, tweet_id):
        return f'Tweet with id {tweet_id} has been flagged'
