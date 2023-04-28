from quart import Quart, request

from entity.role import Role
from entity.user import User
from service.tweet_service import TweetService  # importing necessary directories.
from service.user_service import UserService  # syntax = from directory_name.file_title  class name
from service.category_service import CategoryService
from service.response_service import ResponseService
from service.role_service import RoleService
app = Quart(__name__)

# Registration

# try:
#     result = UserService().registration(username)
#
# except:


@app.route('/register', methods=['POST'])
async def registration():
    data = await request.json
    new_user = User(**data)
    result = UserService().registration(new_user)
    if result is True:
        return "Registered Successfully", 200
    else:
        return "The Username is already taken", 400


# Login


@app.route('/login', methods=['POST'])
async def login():
    data = await request.form
    credentials = User(**data)
    # username = data.get('username')
    # password = data.get('password')
    result = UserService().login(credentials.username, credentials.password)
    if result is True:
        return "Successfully Logged in"
    else:
        return "login Unsuccessful"

# View Profile


@app.route('/view_profile', methods=['GET'])
async def view_profile():
    user_id = '2'
    result = UserService().view_profile(user_id)
    if result is False:
        return "No Such User"
    else:
        return result

# Edit Profile


@app.route('/edit_profile', methods=['PUT'])
async def edit_profile():
    data = await request.form
    name = data.get('name')
    password = data.get('password')
    result = UserService().edit_profile(name, password)
    if result is True:
        return 'Profile Successfully updated'

# Delete Profile


@app.route('/delete_profile', methods=['DELETE'])
async def delete_profile():
    user_id = 1
    result = UserService().delete_profile(user_id)
    if result is True:
        return "Profile Successfully Deleted"

# Dashboard


@app.route('/dashboard', methods=['GET'])
async def dashboard():
    user_id = 10
    result = UserService().dashboard(user_id)
    result1 = result["Popular Tweets"]
    result11 = [tweet.__dict__ for tweet in result1]
    result2 = result["My Tweets"]
    result22 = [tweet.__dict__ for tweet in result2]
    result3 = [result11, result22]
    resultf = [items for items in result3]
    return [items for items in resultf]

# Create Tweet


@app.route('/create_tweet', methods=['POST'])
async def create_tweet():
    data = await request.get_json()
    title = data.get('title')
    created_by = data.get('created_by')
    content = data.get('content')
    category = data.get('category')
    result = TweetService().create_tweet(title, created_by, content, category)
    if result is True:
        return "Tweet created Successfully"

# Get User Tweet List


@app.route('/get_user_tweets', methods=['GET'])
async def get_user_tweet_list():
    tweets = TweetService().get_user_tweets_list(user_id=10)
    return [tweet.__dict__ for tweet in tweets]
# calling function inside the TweetService() class
# square bracket is used, so it would be like a list of
# dictionaries  which can be converted to json format

# Get Single Tweet


@app.route('/get_single_tweet', methods=['GET'])
async def get_tweet():
    user_id = 10
    result = TweetService().get_tweet(user_id)
    return result.__dict__

# Get Popular Tweet List


@app.route('/get_popular_tweets', methods=['GET'])
async def view_list_of_popular_tweets():
    tweets = TweetService().get_popular_tweets_list()
    return [tweet.__dict__ for tweet in tweets]

# Get List Of Category


@app.route('/get_category_list', methods=['GET'])
async def get_category_list():
    category = CategoryService().get_category_list()
    category_data = [item.__dict__ for item in category]
    return category_data


# Get Tweets By Category
@app.route('/get_tweets_by_category', methods=['GET'])
async def get_tweets_by_category():
    category_id = 10
    result = TweetService().get_tweet_by_category(category_id)
    result_data = [item.__dict__ for item in result]
    return result_data


# Create Response
@app.route('/create_response_for_tweet', methods=['POST'])
async def create_response_for_tweet():
    tweet_id = 10
    data = await request.json
    response_content = data.get('response_content')
    response_creator_name = data.get('respond_creator_name')
    result = ResponseService().create_response_for_tweet(tweet_id)
    return result


# Create Reply for Response
@app.route('/create_reply_for_response', methods=['POST'])
async def create_reply_for_response():
    response_id = 10
    data = await request.json
    reply_content = data.get('reply_content')
    reply_creator_name = data.get('reply_creator_name')
    result = ResponseService().create_reply_for_response(response_id)
    return result


# View List of Responses By Tweet
@app.route('/view_responses_by_tweet', methods=['GET'])
async def view_responses_by_tweet():
    tweet_id = 10
    result = ResponseService().view_responses_by_tweet(tweet_id)
    result_data = [item.__dict__ for item in result]
    return result_data


# View List of Replies By Responses
@app.route('/view_replies_by_responses', methods=['GET'])
async def view_replies_by_responses():
    response_id = 10
    result = ResponseService().view_replies_by_responses(response_id)
    result_data = [item.__dict__ for item in result]
    return result_data


# View all Users By Admin
@app.route('/view_all_users', methods=['GET'])
async def view_all_users():
    result = RoleService().view_all_users()
    return result


# Flag Tweet
@app.route('/flag_tweet', methods=['POST'])
async def flag_tweet():
    tweet_id = 10
    data = await request.form
    reason = data.get('reason')
    result = UserService().flag_tweet(tweet_id)
    return result


# Assign Role
@app.route('/assign_role', methods=['PUT'])
async def assign_role():
    data = await request.json
    new_role = Role(**data)
    result = RoleService().assign_role(user_id=11)
    if result is True:
        return f'Role Changed to {new_role.role_name}'

if __name__ == '__main__':
    app.run()
