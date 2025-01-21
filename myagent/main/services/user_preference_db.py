# import sqlite3

# DB_PATH = "data/user.db"

# def create_user_preference():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
    
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS user_profile (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         height REAL NOT NULL,
#         weight REAL NOT NULL,
#         goal TEXT CHECK(goal IN ('weight_loss', 'muscle_gain', 'maintenance')) NOT NULL
       
#     )
#     """)
    
#     conn.commit()
#     conn.close()
    
    
# def insert_user_profile(name, height, weight, goal):
#     """Inserts a new user profile into the database."""
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()

#     cursor.execute("""
#     INSERT INTO user_profile (name, height, weight, goal)
#     VALUES (?, ?, ?, ?)
#     """, (name, height, weight, goal))
    
#     conn.commit()
#     conn.close()


# def get_user_profile():
#     """Fetches the most recent user profile from the database."""
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()

#     cursor.execute("SELECT name, height, weight, goal FROM user_profile ORDER BY id DESC LIMIT 1")
#     row = cursor.fetchone()
#     conn.close()

#     if row:
#         return {
#             "name": row[0],
#             "height": row[1],
#             "weight": row[2],
#             "goal": row[3]
#         }
#     return None  # Return None if no user profile exists



# # if __name__ == "__main__":
# #     create_pantry_table()
# #     print("Pantry table initilized")
# #     # add_ingredient("Firm Tofu", 3, "pack", "fridge")
# #     # add_ingredient("Soft tofu", 1, "pack", "fridge")
# #     # add_ingredient("quinoa", 1, "pack", "pantry")
# #     # add_ingredient("brown rice", 500, "grams", "pantry")
# #     result = get_pantry()
# #     print(result)
    