from pymongo import MongoClient

def count_active_users():
    # Replace with your actual MongoDB connection string and database name
    mongo_connection_string = 'mongo_connection_string'  # Replace with your MongoDB connection string
    database_name = 'mydatabase'  # Replace with your database name

    client = MongoClient(mongo_connection_string)
    db = client[database_name]

    # Assuming 'users' is the collection name. Replace if using a different collection
    users_collection = db.users  # Replace with your collection name if different

    # Count documents in the 'users' collection where 'status' is set to 'active'
    active_user_count = users_collection.count_documents({'status': 'active'})

    return active_user_count

# Example usage:
active_user_count = count_active_users()
print(f"Number of active users: {active_user_count}")
