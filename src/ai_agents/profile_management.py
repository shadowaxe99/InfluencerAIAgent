from pymongo import MongoClient

class UserProfile:
    def __init__(self, user_id, profile_data=None, operation=None, db_uri='mongodb_connection_string', db_name='database_name'):
        self.user_id = user_id
        self.profile_data = profile_data
        self.operation = operation
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.profiles_collection = self.db.profiles

    def manage_user_profile(self):
        if self.operation == 'create':
            return self.profiles_collection.insert_one(self.profile_data).inserted_id
        elif self.operation == 'retrieve':
            return self.profiles_collection.find_one({'_id': self.user_id})
        elif self.operation == 'update':
            return self.profiles_collection.update_one({'_id': self.user_id}, {'$set': self.profile_data}).modified_count > 0
        elif self.operation == 'delete':
            return self.profiles_collection.delete_one({'_id': self.user_id}).deleted_count > 0
        else:
            raise ValueError("Invalid operation. Must be 'create', 'retrieve', 'update', or 'delete'.")

    def get_profile(self):
        return self.profiles_collection.find_one({'_id': self.user_id})

    def update_profile(self, updated_data):
        return self.profiles_collection.update_one({'_id': self.user_id}, {'$set': updated_data}).modified_count > 0

    def delete_profile(self):
        return self.profiles_collection.delete_one({'_id': self.user_id}).deleted_count > 0

# Example usage:
# user_profile = UserProfile(user_id="12345", profile_data={"name": "John Doe"}, operation="create")
# user_profile.manage_user_profile()
