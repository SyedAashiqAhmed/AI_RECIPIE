import sqlite3

# Create database and table
def create_database():
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ingredients TEXT NOT NULL
    )
    ''')

    # Sample data
    recipes = [
        ('Pasta Alfredo', 'pasta, cream, cheese, garlic'),
        ('Veggie Salad', 'lettuce, tomato, cucumber, olive oil'),
        ('Grilled Sandwich', 'bread, cheese, butter, tomato'),
        ('Fruit Smoothie', 'banana, milk, honey, berries'),
        ('Omelette', 'eggs, salt, pepper, onion'),
    ]

    cursor.executemany('INSERT INTO recipes (name, ingredients) VALUES (?, ?)', recipes)
    conn.commit()
    conn.close()
    print("Database created with sample data!")

create_database()
