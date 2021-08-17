import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING
from tkinter import *
from tkcalendar import DateEntry
import datetime
import GetImage as GM

def main(root,name,email,mobile,password,gender):

    root.title("User Signup")
    width=750
    height=550
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    BgImg = GM.getImage("D:\Programming\Python\Room_Rental\Images\BG.jpg", 744, 540)
    BGLabel=tk.Label(root,image=BgImg)
    BGLabel.image=BgImg
    ft = tkFont.Font(family='Times',size=16)
    BGLabel["font"] = ft
    BGLabel["justify"] = "center"
    BGLabel["text"] = ""
    BGLabel.place(x=3,y=1,width=744,height=545)

    Title=tk.Label(root)
    Title["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=28)
    Title["font"] = ft
    Title["fg"] = "#333333"
    Title["justify"] = "center"
    Title["text"] = "Student Verification"
    Title.place(x=150,y=10,width=590,height=75)

    Divider=tk.Label(root)
    Divider["bg"] = "#90ee90"
    ft = tkFont.Font(family='Times',size=16)
    Divider["font"] = ft
    Divider["fg"] = "#333333"
    Divider["justify"] = "center"
    Divider["text"] = ""
    Divider.place(x=0,y=100,width=744,height=3)

    BackLogo = GM.getImage("D:\Programming\Python\Room_Rental\Images\Logo.png",131,77)
    Back=tk.Button(root,image=BackLogo)
    Back.image = BackLogo
    Back["justify"] = "center"
    Back.place(x=10,y=10,width=131,height=77)
    Back["command"] = lambda : Back_command(root)

    EnterAddressLabel=tk.Label(root)
    EnterAddressLabel["bg"] = "#999999"
    ft = tkFont.Font(family='Times',size=16)
    EnterAddressLabel["font"] = ft
    EnterAddressLabel["fg"] = "#000000"
    EnterAddressLabel["justify"] = "center"
    EnterAddressLabel["text"] = "Enter Permanent Address"
    EnterAddressLabel.place(x=70,y=180,width=242,height=30)

    EnterAddress=tk.Entry(root)
    EnterAddress["bg"] = "#393d49"
    EnterAddress["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    EnterAddress["font"] = ft
    EnterAddress["fg"] = "#ffffff"
    EnterAddress["justify"] = "left"
    EnterAddress["text"] = ""
    EnterAddress.place(x=370,y=160,width=319,height=78)

    SelectDate=tk.Label(root)
    ft = tkFont.Font(family='Times',size=16)
    SelectDate["bg"] = "#999999"
    SelectDate["font"] = ft
    SelectDate["fg"] = "#000000"
    SelectDate["justify"] = "center"
    SelectDate["text"] = "Select Date of Birth"
    SelectDate.place(x=90,y=260,width=195,height=56)

    EnterDate = DateEntry(root, width=27, background='brown', foreground='white', date_pattern='dd/mm/y')
    EnterDate["borderwidth"] = 3
    EnterDate.place(x=370,y=270,width=300,height=45)
    #EnterDate["show"] = "E"

    SignUp=tk.Button(root)
    SignUp["bg"] = "#1eff69"
    ft = tkFont.Font(family='Times',size=16)
    SignUp["borderwidth"] = "4px"
    SignUp["font"] = ft
    SignUp["fg"] = "#000000"
    SignUp["justify"] = "center"
    SignUp["text"] = "Sign Up"
    SignUp.place(x=240,y=440,width=300,height=45)
    SignUp["command"] = lambda : SignUp_command(root,name,email,mobile,password,gender,EnterAddress.get(), str(EnterDate.get_date()))

def Back_command(root) :
    import UserSignUp as usp
    usp.main(root,'S')

def SignUp_command(root,n,e,m,p,g,a,d) :
    from tkinter import messagebox
    from tkinter.messagebox import askokcancel, showinfo, WARNING
    print(d)
    if g ==1 : gender = 'Male'
    else : gender = 'Female'
    if a!='' and d!='':  
        import DatabaseConnection as DB
        #student_id = int(DB.runQuery("select max(s_id) from Student")[0][0]) + 1
        student_id = int(bool(DB.runQuery("select max(s_id) from Student")[0][0])) + 1  #cloud
        status = DB.insertStudent(student_id,n,a,gender,d,e,float(m),p)
        if status:            
            messagebox.showinfo("Success", "Student Account Created Sucessfully !")
            import Welcome as wc 
            wc.App(root)
        else : messagebox.showerror("Error","Oops! somwthing went wrong. Try again with Unique details.")
    else :
        messagebox.showerror("Error","Details are not valid. Please enter valid details.")