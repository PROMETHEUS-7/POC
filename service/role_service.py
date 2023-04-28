# from entity.user import User


class RoleService:
    # View all users by admin
    def view_all_users(self):
        with open('C:/Users/Admin/PycharmProjects/Quart/POC/storage/users.txt', 'r', newline='') as file:
            lines = file.readlines()
            user_list = []
            for line in lines[1:]:
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
        return user_list

    # Assign Role
    def assign_role(self, user_id):
        return True

