class Response:
    def __init__(self, response_id, response_created_by=None, response_content=None):
        self.response_id = response_id
        self.response_content = response_content
        self.response_created_by = response_created_by
