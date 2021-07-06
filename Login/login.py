from tkinter import*
from PIL import ImageTk
class Login_System:
    def __init__(self, root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("1350x700+0+0")

        self.bg_icon=ImageTk.PhotoImage(file="images/img.jpg")
        self.user_icon=PhotoImage(file="images/man-user.png")
        self.user_icon = PhotoImage(file="images/password.png"

        title=Label(self.root,text="Login System", font=("times new roman", 40, "bold"), bg="yellow", fg="red")
root=Tk()
obj=Login_System(root)
root.mainloop()