from entity.response import Response


class ResponseService:
    # Create Response For Tweet
    def create_response_for_tweet(self, tweet_id):
        return "response created successfully"

    # Create Reply for Response
    def create_reply_for_response(self, response_id):
        return "reply created successfully"

    # View Responses By Tweet
    def view_responses_by_tweet(self, tweet_id):
        responses = [
            Response(response_id=10, response_created_by="john", response_content="Content example"),
            Response(response_id=11, response_created_by="john", response_content="Content example"),
            Response(response_id=12, response_created_by="john", response_content="Content example")
        ]
        return responses

    # View Replies By Response
    def view_replies_by_responses(self, response_id):
        replies = [
            Response(response_id=10, response_created_by="john", response_content="Content example"),
            Response(response_id=11, response_created_by="john", response_content="Content example"),
            Response(response_id=12, response_created_by="john", response_content="Content example")
        ]
        return replies

