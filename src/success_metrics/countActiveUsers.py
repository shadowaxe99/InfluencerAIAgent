import pymongo


def count_active_users():
    # Implement logic to count and report the number of active users
    try:
        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["InfluencerDB"]
        # Query the database to get the list of active users
        active_users = db["users"].find({"status": "active"})
        # Count the number of active users
        active_user_count = active_users.count()
        return active_user_count
    except Exception as e:
        print("An error occurred while counting active users:", e)
        return None
