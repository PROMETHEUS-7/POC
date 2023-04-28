from entity.category import Category


class CategoryService:
    # Get List Of Categories
    def get_category_list(self):
        category_list = [Category(category_id=1, name="Science", description="This is the description of Science"),
                         Category(category_id=2, name="Politics", description="This is the description of Politics"),
                         Category(category_id=3, name="Entertainment", description="This is the description of "
                                                                                   "Entertainment")]
        return category_list
