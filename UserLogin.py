import tkinter as tk
import tkinter.font as tkFont
import GetImage as GM
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING

def main(root,token):
    
    root.title("User Login")
    width=750;    height=500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    BgImg = GM.getImage("D:\Programming\Python\Room_Rental\Images\BG.jpg", 744, 495)
    BGLabel=tk.Label(root,image=BgImg)
    BGLabel.image=BgImg
    BGLabel["justify"] = "center"
    BGLabel.place(x=3,y=1,width=744,height=494)

    Title=tk.Label(root)
    Title["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=28)
    Title["font"] = ft
    Title["fg"] = "#333333"
    Title["justify"] = "center"
    if token == 'S' :   who = 'Student'
    else :  who = 'Owner'
    Title["text"] = who+" Login"
    Title.place(x=150,y=10,width=590,height=75)

    Divider=tk.Label(root)
    Divider["bg"] = "#90ee90"
    ft = tkFont.Font(family='Times',size=10)
    Divider["font"] = ft
    Divider["fg"] = "#333333"
    Divider["justify"] = "center"
    Divider["text"] = ""
    Divider.place(x=0,y=100,width=744,height=3)
    
    EnterUsername=tk.Label(root)
    EnterUsername["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=16)
    EnterUsername["font"] = ft
    EnterUsername["fg"] = "#ffffff"
    EnterUsername["justify"] = "center"
    EnterUsername["text"] = "Enter Username \n(Your Email is your username)"
    EnterUsername.place(x=60,y=160,width=270,height=54)

    PasswordLabel=tk.Label(root)
    PasswordLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=14)
    PasswordLabel["font"] = ft
    PasswordLabel["fg"] = "#ffffff"
    PasswordLabel["justify"] = "center"
    PasswordLabel["text"] = "Enter Password"
    PasswordLabel.place(x=120,y=270,width=160,height=31)

    Username=tk.Entry(root)
    Username["bg"] = "#eeeeee"
    Username["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    Username["font"] = ft
    Username["fg"] = "#000000"
    Username["justify"] = "center"
    Username["text"] = ""
    Username.place(x=350,y=160,width=330,height=40)

    Password=tk.Entry(root,show='*')
    Password["bg"] = "#eeeeee"
    Password["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    Password["font"] = ft
    Password["fg"] = "#000000"
    Password["justify"] = "center"
    Password["text"] = ""
    Password.place(x=350,y=270,width=330,height=40)

    Login=tk.Button(root)
    Login["bg"] = "#1eff69"
    Login["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=16)
    Login["font"] = ft
    Login["fg"] = "#000000"
    Login["justify"] = "center"
    Login["text"] = "Login"
    Login.place(x=230,y=390,width=300,height=45)
    Login["command"] = lambda : Login_command(root,Username.get(),Password.get(),token)

    BackLogo = GM.getImage("D:\Programming\Python\Room_Rental\Images\Logo.png",131,77)
    Back=tk.Button(root,image=BackLogo)
    Back.image = BackLogo
    Back["justify"] = "center"
    Back.place(x=10,y=10,width=131,height=77)
    Back["command"] = lambda : Back_command(root)

def Login_command(root,username,password,token):

    if username != '' and password != '' :
        import DatabaseConnection as DB
        if token == 'O' :
            cnt = DB.runQuery2("select count(o_id) from Owner where email = '"+username+"' AND password = '"+password+"'")
            if cnt[0] == 0 : 
                messagebox.showerror("Failed","Wrong ! Incorrect username or password.")    
            else : 
                username,id = DB.runQuery2("select name,o_id from Owner where email = '"+username+"' AND password = '"+password+"'")
                import OwnerHome as Home
                Home.main(root,username,id)
        else : 
            cnt = DB.runQuery2("SELECT count(s_id) FROM Student WHERE email ='%s' AND password ='%s'" % (username, password))
            if cnt[0] == 0 : 
                messagebox.showerror("Failed","Wrong ! Incorrect username or password.")    
            else :  
                TUP = DB.runQuery2("SELECT name, s_id FROM Student WHERE email ='%s' AND password ='%s'" % (username, password))
                import StudentHome as Home
                Home.main(root,TUP[0],TUP[1])
    else :
        messagebox.showerror("Error","Details are not valid. Please enter valid details.")


def Back_command(root):
    import Welcome as wc
    wc.App(root)
