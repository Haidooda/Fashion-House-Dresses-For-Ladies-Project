from tkinter import *
from PIL import Image, ImageTk
root = Tk()
def buy(root):
    frame=Frame(root)
    # Create the main window
    
    root.title('BUY A DRESS')
    # Set the background color
    root.configure(bg="#ffeff2")  # Light pink background color
    
    root.geometry("1000x1000")
    
    # Load and resize the image
    path = 'blue_dress1.png'
    img = Image.open(path)
    img = img.resize((700, 700))
    img_tk = ImageTk.PhotoImage(img)

     #Display the image in the center of the window
    Label1=Label(frame, image=img_tk)
    Label1.place(x=100,y=100)

    # Create a button with the specified color and border
    button = Button(frame, text="Click Me!", bg="#fed3e6", bd=1, relief="solid", command=lambda: print("Button Clicked"), font=("Papyrus 19 bold"))
    # Place the button in the center of the window
    button.grid(row=0,column=0,columnspan=2)

    # Add a label with any sentence
    label = Label(root, text="Hello, this is a simple GUI!", bg="#ffeff2")
    label.place(anchor='center',relx=0.5,rely=0.5)

    frame.place(anchor='center',relx=0.5,rely=0.5)
    # Run the GUI
    root.mainloop()

# Call the function to create the GUI

def call():
    
    buy(root)
    root.mainloop()
call()