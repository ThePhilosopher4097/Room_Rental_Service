import tkinter as tk
from tkinter import *
from tkinter.constants import BOTTOM, LEFT
import tkinter.font as tkFont
import GetImage as GM

class App:
    def __init__(self, root):

        root.title("Welcome")
        #setting window size
        width=750
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        BgIMG = GM.getImage("D:\Programming\Python\Room_Rental\Images\BG.jpg",744,500)
        BGLabel=tk.Label(root,image=BgIMG)
        BGLabel.image=BgIMG
        ft = tkFont.Font(family='Times',size=10)
        BGLabel["font"] = ft
        BGLabel["fg"] = "#333333"
        BGLabel["justify"] = "center"
        BGLabel["text"] = ""
        BGLabel.place(x=3,y=3,width=744,height=500)

        Title=tk.Label(root)
        Title["bg"] = "#c71585"
        Title["borderwidth"] = "5px"
        ft = tkFont.Font(family='Times',size=28)
        Title["font"] = ft
        Title["fg"] = "#ffffff"
        Title["justify"] = "center"
        Title["text"] = "Aspires' Room Rental Services"
        Title.place(x=200,y=10,width=547,height=125)

        LogoIMG = GM.getImage("D:\Programming\Python\Room_Rental\Images\Logo.png",198,124)
        LogoLabel=tk.Label(root,image=LogoIMG)
        LogoLabel.image=LogoIMG
        LogoLabel["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=10)
        LogoLabel["font"] = ft
        LogoLabel["fg"] = "#333333"
        LogoLabel["justify"] = "center"
        LogoLabel["text"] = ""
        LogoLabel.place(x=3,y=10,width=200,height=125)
#sameerpatil
        UserLoginIMG = GM.getImage("D:\Programming\Python\Room_Rental\Images\Login2.jpeg",110,100)
        UserLogin=tk.Button(root, image=UserLoginIMG, compound=LEFT)
        UserLogin.image=UserLoginIMG
        UserLogin["bg"] = "#ffd700"
        UserLogin["borderwidth"] = "5px"
        ft = tkFont.Font(family='Times',size=14)
        UserLogin["font"] = ft
        UserLogin["fg"] = "#000000"
        UserLogin["justify"] = "center"
        UserLogin["text"] = "Student \nLogin"
        UserLogin.place(x=160,y=190,width=200,height=100)
        UserLogin["command"] = lambda : UserLogin_command(root,'S')

        OwnerLoginIMG = GM.getImage("D:\Programming\Python\Room_Rental\Images\Login1.jpg",110,100)
        OwnerLogin=tk.Button(root,image=OwnerLoginIMG,compound=LEFT)
        OwnerLogin.image=OwnerLoginIMG
        OwnerLogin["bg"] = "#1e9fff"
        OwnerLogin["borderwidth"] = "5px"
        ft = tkFont.Font(family='Times',size=14)
        OwnerLogin["font"] = ft
        OwnerLogin["fg"] = "#000000"
        OwnerLogin["justify"] = "center"
        OwnerLogin["text"] = "Owner \nLogin"
        OwnerLogin.place(x=160,y=330,width=200,height=100)
        OwnerLogin["command"] = lambda : UserLogin_command(root,'O')

        UserSignupIMG = GM.getImage("D:\Programming\Python\Room_Rental\Images\Login3.png",110,100)
        UserSignup=tk.Button(root,image=UserSignupIMG,compound=LEFT)
        UserSignup.image=UserSignupIMG
        UserSignup["bg"] = "#ffd700"
        UserSignup["borderwidth"] = "5px"
        ft = tkFont.Font(family='Times',size=14)
        UserSignup["font"] = ft
        UserSignup["fg"] = "#000000"
        UserSignup["justify"] = "center"
        UserSignup["text"] = "Student \nSignup"
        UserSignup.place(x=430,y=190,width=200,height=100)
        UserSignup["command"] = lambda : UserSignup_command(root,'S')

        OwnerSignupIMG = GM.getImage("D:\Programming\Python\Room_Rental\Images\Login4.jpg",110,100)
        OwnerSignup=tk.Button(root,image=OwnerSignupIMG,compound=LEFT)
        OwnerSignup.image=OwnerSignupIMG
        OwnerSignup["bg"] = "#01aaed"
        OwnerSignup["borderwidth"] = "5px"
        ft = tkFont.Font(family='Times',size=14)
        OwnerSignup["font"] = ft
        OwnerSignup["fg"] = "#000000"
        OwnerSignup["justify"] = "center"
        OwnerSignup["text"] = "Owner \nSignup"
        OwnerSignup.place(x=430,y=330,width=200,height=100)
        OwnerSignup["command"] = lambda : UserSignup_command(root,'O')

def UserLogin_command(root,token):
    import UserLogin as UL
    UL.main(root,token)

def UserSignup_command(root,who):
    import UserSignUp as USP
    USP.main(root,who)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
