import sqlite3

# Connect to the SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('dress1.db')
cursor = conn.cursor()

# Create the dress table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS dress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        color TEXT NOT NULL,
        dress_photo BLOB NOT NULL
    )
''')

# Function to read a file and return its content as BLOB
def readfile(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

# Replace 'path/to/your/image.jpg' with the actual path to your image file
image_path = 'C:\\Users\\lap-tech\\Pictures\\Wallpapers\\red.jpg'
image_data = readfile(image_path)

# Insert the image data into the database
cursor.execute('''
    INSERT INTO dress (color, dress_photo) VALUES (?, ?)
''', ('red', image_data))

# Commit the changes and close the connection
conn.commit()
conn.close()
