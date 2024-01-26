from tkinter import *
from PIL import Image, ImageTk
def options(root):
    padx=10
    pady=10
    font=("Papyrus 22 bold")
    #To convert format of image to png
    img= Image.open("blue_dress1.png")
    #To resize image to make it bigger
    img=img.resize((700,700))
    img_tk=ImageTk.PhotoImage(img)
    Label(root, image=img_tk).place(x=0, y=0)
    def center_screen():
            w=700
            h=750
            screenwidth=root.winfo_screenwidth()
            screenheight=root.winfo_screenheight()
            x=int((screenwidth-w)/2)
            y=int((screenheight-h)/2)
            root.geometry(f'{w}x{h}+{x}+{y}')
            
    def resizable_screen():
            root.resizable(False,False)    
        #botton for Admin 
    btn_admin=Button(root,text="Admin",font=font,bg="black",fg="pink")
    btn_admin.place(x=500,y=450)
      #botton for Customer
    btn_customer=Button(root,text="Customer",font=font,bg="black",fg="pink")
    btn_customer.place(x=500,y=550)
    
    
    root.title("Welcome")
    center_screen()
    resizable_screen()
    
    root.mainloop()
def call():
    root = Tk()
    
    options(root)
    root.mainloop()
call()