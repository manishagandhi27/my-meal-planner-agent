import sqlite3
import os

# Get the absolute path of the `services/` directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Points to `src/main/services/`

# Construct the DB path inside `services/data/`
DB_DIR = os.path.join(BASE_DIR, "data")  # ✅ Ensures "data/" is inside "services/"
DB_PATH = os.path.join(DB_DIR, "user.db")

#DB_PATH = "data/user.db"

def create_user_profile():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        height REAL NOT NULL,
        weight REAL NOT NULL,
        goal TEXT CHECK(goal IN ('weight_loss', 'muscle_gain', 'maintenance')) NOT NULL
       
    )
    """)
    
    conn.commit()
    conn.close()
    
    
def insert_user_profile(name, height, weight, goal):
    """Inserts a new user profile into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO user_profile (name, height, weight, goal)
    VALUES (?, ?, ?, ?)
    """, (name, height, weight, goal))
    
    conn.commit()
    conn.close()


def get_user_profile():
    """Fetches the most recent user profile from the database."""
    print(f"DB_PATH {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT name, height, weight, goal FROM user_profile ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "name": row[0],
            "height": row[1],
            "weight": row[2],
            "goal": row[3]
        }
    return None  # Return None if no user profile exists


