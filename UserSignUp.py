import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING
from tkinter import *
import GetImage as GM
Gender = 0
def main(root,token):

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
    BGLabel["justify"] = "center"
    BGLabel.place(x=3,y=1,width=744,height=545)

    Title=tk.Label(root)
    Title["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=28)
    Title["font"] = ft
    Title["fg"] = "#333333"
    Title["justify"] = "center"
    if token == 'O' : Title["text"] = "Owner Sign-up"
    else : Title["text"] = "Student Sign-up"
    Title.place(x=150,y=10,width=590,height=75)

    Divider=tk.Label(root)
    Divider["bg"] = "#90ee90"
    ft = tkFont.Font(family='Times',size=16)
    Divider["font"] = ft
    Divider["fg"] = "#333333"
    Divider["justify"] = "center"
    Divider["text"] = ""
    Divider.place(x=0,y=100,width=744,height=3)

    EnterName=tk.Entry(root)
    EnterName["bg"] = "#393d49"
    EnterName["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    EnterName["font"] = ft
    EnterName["fg"] = "#ffffff"
    EnterName["justify"] = "center"
    EnterName["text"] = ""
    EnterName.place(x=340,y=130,width=330,height=40)

    var = IntVar()
    Male=tk.Radiobutton(root,variable=var,value=1,indicatoron=0)
    Male["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=14)
    Male["font"] = ft
    Male["justify"] = "center"
    Male["text"] = "Male"
    Male.place(x=340,y=190,width=150,height=30)
    Male["command"] = lambda : Male_command(var.get())

    Female=tk.Radiobutton(root,variable=var,value=2,indicatoron=0)
    Female["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=14)
    Female["font"] = ft
    Female["justify"] = "center"
    Female["text"] = "Female"
    Female.place(x=520,y=190,width=150,height=30)
    Female["command"] = lambda : Female_command(var.get())

    EnterEmail=tk.Entry(root)
    EnterEmail["bg"] = "#393d49"
    EnterEmail["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    EnterEmail["font"] = ft
    EnterEmail["fg"] = "#ffffff"
    EnterEmail["justify"] = "center"
    EnterEmail["text"] = ""
    EnterEmail.place(x=340,y=250,width=330,height=40)

    EnterMobile=tk.Entry(root)
    EnterMobile["bg"] = "#393d49"
    EnterMobile["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    EnterMobile["font"] = ft
    EnterMobile["fg"] = "#ffffff"
    EnterMobile["justify"] = "center"
    EnterMobile["text"] = ""
    EnterMobile.place(x=340,y=310,width=330,height=40)

    EnterNameLabel=tk.Label(root)
    EnterNameLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=14)
    EnterNameLabel["font"] = ft
    EnterNameLabel["fg"] = "#ffffff"
    EnterNameLabel["justify"] = "center"
    EnterNameLabel["text"] = "Enter Name"
    EnterNameLabel.place(x=160,y=130,width=128,height=34)

    SelectGender=tk.Label(root)
    SelectGender["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=14)
    SelectGender["font"] = ft
    SelectGender["fg"] = "#ffffff"
    SelectGender["justify"] = "center"
    SelectGender["text"] = "Select Gender"
    SelectGender.place(x=160,y=190,width=128,height=38)

    EnterEmailLabel=tk.Label(root)
    ft = tkFont.Font(family='Times',size=14)
    EnterEmailLabel["font"] = ft
    EnterEmailLabel["bg"] = "#393d49"
    EnterEmailLabel["fg"] = "#ffffff"
    EnterEmailLabel["justify"] = "center"
    EnterEmailLabel["text"] = "Enter Email"
    EnterEmailLabel.place(x=150,y=250,width=137,height=33)

    EnterMobileLabel=tk.Label(root)
    EnterMobileLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=14)
    EnterMobileLabel["font"] = ft
    EnterMobileLabel["fg"] = "#ffffff"
    EnterMobileLabel["justify"] = "center"
    EnterMobileLabel["text"] = "Enter Mobile"
    EnterMobileLabel.place(x=150,y=300,width=137,height=48)

    EnterPassword=tk.Entry(root,show='*')
    EnterPassword["bg"] = "#393d49"
    EnterPassword["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    EnterPassword["font"] = ft
    EnterPassword["fg"] = "#ffffff"
    EnterPassword["justify"] = "center"
    EnterPassword["text"] = ""
    EnterPassword.place(x=340,y=370,width=330,height=40)

    if token == 'O' :
        SignUp=tk.Button(root)
        SignUp["bg"] = "#1eff69"
        ft = tkFont.Font(family='Times',size=16)
        SignUp["borderwidth"] = "4px"
        SignUp["font"] = ft
        SignUp["fg"] = "#000000"
        SignUp["justify"] = "center"
        SignUp["text"] = "Sign Up"
        SignUp.place(x=240,y=490,width=300,height=45)
        SignUp["command"] = lambda : SignUp_command(root,EnterPassword.get(),ConfirmPassword.get(),EnterEmail.get(),EnterName.get(),EnterMobile.get(),var.get())
    else :
        Next=tk.Button(root)
        Next["bg"] = "#1eff69"
        ft = tkFont.Font(family='Times',size=16)
        Next["borderwidth"] = "4px"
        Next["font"] = ft
        Next["fg"] = "#000000"
        Next["justify"] = "center"
        Next["text"] = "Next"
        Next.place(x=240,y=490,width=300,height=45)
        Next["command"] = lambda : Next_command(root,EnterPassword.get(),ConfirmPassword.get(),EnterEmail.get(),EnterName.get(),EnterMobile.get(),var.get())

    SetPasswordLabel=tk.Label(root)
    SetPasswordLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=14)
    SetPasswordLabel["font"] = ft
    SetPasswordLabel["fg"] = "#ffffff"
    SetPasswordLabel["justify"] = "center"
    SetPasswordLabel["text"] = "Set a Password"
    SetPasswordLabel.place(x=140,y=370,width=161,height=37)

    BackLogo = GM.getImage("D:\Programming\Python\Room_Rental\Images\Logo.png",131,77)
    Back=tk.Button(root,image=BackLogo)
    Back.image = BackLogo
    Back["justify"] = "center"
    Back.place(x=10,y=10,width=131,height=77)
    Back["command"] = lambda : Back_command(root)

    ConfirmPasswordLabel=tk.Label(root)
    ConfirmPasswordLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=14)
    ConfirmPasswordLabel["font"] = ft
    ConfirmPasswordLabel["fg"] = "#ffffff"
    ConfirmPasswordLabel["justify"] = "center"
    ConfirmPasswordLabel["text"] = "Confirm Password"
    ConfirmPasswordLabel.place(x=140,y=430,width=160,height=35)

    ConfirmPassword=tk.Entry(root,show='*')
    ConfirmPassword["bg"] = "#393d49"
    ConfirmPassword["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    ConfirmPassword["font"] = ft
    ConfirmPassword["fg"] = "#ffffff"
    ConfirmPassword["justify"] = "center"
    ConfirmPassword["text"] = ""
    ConfirmPassword.place(x=340,y=430,width=330,height=40)

def Male_command(v):
    global Gender;  Gender = v

def Female_command(v):
    global Gender;   Gender = v

def SignUp_command(root,C1,C2,e,n,m,g):
    if C1==C2 and C1!='' and e!='' and n!='' and m!='' and g>0 and g<3 :  
        if g ==1 :  gen = 'Male'
        else : gen = 'Female'
        import DatabaseConnection as DB
        #owner_id = DB.runQuery("select max(o_id) from Owner")[0][0] + 1
        owner_id = int(bool(DB.runQuery("select max(o_id) from Owner")[0][0])) + 1
        status = DB.insertOwner(owner_id,n,gen,float(m),e,C1)
        print(status)
        if str(status)!='False' :
            messagebox.showinfo("Success", "Room Owner Account Created Sucessfully !")
            import Welcome as wc 
            wc.App(root)
        else :  messagebox.showerror("Error","Oops! Something went wrong. Either the email-id is already used.")
    elif C1!=C2 :
        messagebox.showerror("Error","Confirm Password does not match")
    else :
        messagebox.showerror("Error","Details are not valid. Please enter valid details.")

def Next_command(root,C1,C2,e,n,m,g):
    if C1==C2 and C1!='' and e!='' and n!='' and m!='' and g>0 and g<3 :  
        import StudentVerification as SV; SV.main(root,n,e,float(m),C1,g)
    elif C1!=C2 :
        messagebox.showerror("Error","Confirm Password does not match")
    else :
        messagebox.showerror("Error","Details are not valid. Please enter valid details.")


def Back_command(root):
    import Welcome as WC
    WC.App(root)
