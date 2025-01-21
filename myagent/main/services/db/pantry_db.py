import sqlite3

DB_PATH = "data/pantry.db"

def create_pantry_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pantry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ingredient TEXT UNIQUE NOT NULL,
        quantity REAL NOT NULL,
        unit TEXT NOT NULL,
        location TEXT NOT NULL  -- pantry, fridge, freezer
    );
    """)  # Ensure the semicolon at the end of the SQL query

    
    conn.commit()
    conn.close()
    
    
def add_ingredient(ingredient, quantity, unit, location):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO pantry (ingredient, quantity, unit, location)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(ingredient) DO UPDATE SET quantity = quantity + ?;
    """, (ingredient, quantity, unit, location, quantity))

    conn.commit()
    conn.close()    


def get_pantry():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT ingredient, quantity, unit, location FROM pantry")
    data = cursor.fetchall()

    conn.close()
    return data


if __name__ == "__main__":
    create_pantry_table()
    print("Pantry table initilized")
 
    result = get_pantry()
    print(result)
    