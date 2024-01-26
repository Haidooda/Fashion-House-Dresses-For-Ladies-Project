import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import io

def fetch_and_display_photo(root):
    # Connect to the SQLite database (replace 'your_database.db' with your actual database)
    print('clicked')
    conn = sqlite3.connect('dress.db')
    print('clicked1')
    cursor = conn.cursor()
    print('clicked2')
    # Assuming your dress table has columns 'id', 'colors', 'dress_photo'
    cursor.execute("SELECT dress_photo FROM dress WHERE dress_id = 1")  # Adjust the query as needed
    print('clicked3')
    photo_data = cursor.fetchone()
    print('clicked4')
    # Close the database connection
    conn.close()

    if photo_data:
        # Convert the binary image data to a PhotoImage
        image_data = io.BytesIO(photo_data[0])
        photo_image = ImageTk.PhotoImage(Image.open(image_data))

        # Display the image in a new window
        image_window = tk.Toplevel(root)
        image_window.title("Dress Photo")
        label2 = tk.Label(image_window, text='mm')
        label = tk.Label(image_window, image=photo_image)
        label.photo = photo_image  # Keep a reference to prevent garbage collection
        label.pack()
        label2.pack()
    else:
        print('Sorry, no photo data found.')

def create_gui():
    # Create the main window
    root = tk.Tk()

    # Set the background color
    root.configure(bg="#ffeff2")

    # Create a button with the specified color and border
    button = tk.Button(root, text="Show Dress Photo", bg="#fed3e6", bd=1, relief="solid", command=lambda: fetch_and_display_photo(root))
    button.pack(pady=20)

    # Add a label with any sentence
    label = tk.Label(root, text="Hello, this is a simple GUI!", bg="#ffeff2")
    label.pack(pady=10)

    # Run the GUI
    root.mainloop()

# Call the function to create the GUI
create_gui()
