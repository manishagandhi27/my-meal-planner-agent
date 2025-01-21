# from user_profile_db import create_user_profile, get_user_profile, insert_user_profile
import sqlite3
import os

def get_db_connection():
    # Get the absolute path of the `services/` directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Points to `src/main/services/`

    # Construct the DB path inside `services/data/`
    DB_DIR = os.path.join(BASE_DIR, "data")  # ✅ Ensures "data/" is inside "services/"
    DB_PATH = os.path.join(DB_DIR, "user.db")
    conn = sqlite3.connect(DB_PATH)
    return conn
    


   

# create_user_profile()

# # Insert a sample user profile
# insert_user_profile(
#     name="Manisha G",
#     height=5.1,
#     weight=125,
#     goal="weight_loss"
# )

# print("User profile inserted successfully!")