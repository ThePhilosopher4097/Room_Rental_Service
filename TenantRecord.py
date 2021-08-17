from AddRoom import RoomImage
import tkinter as tk
from tkinter import ttk
from tkinter.constants import LEFT
import tkinter.font as tkFont
import GetImage as GM
from tkinter import Frame, messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING

treev = ''; treev2 = ''; Root = '';  User = '';  ID = ''
def main(root,Room,user,id):

    global User;   User = Room;   global Root;   Root = root;   global ID;  ID = id
    root.title("Student Home")
    width=750
    height=600
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    BgImg = GM.getImage("D:\Programming\Python\Room_Rental\Images\BG.jpg", 744, 592)
    BGLabel=tk.Label(root,image=BgImg)
    BGLabel.image=BgImg
    BGLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=10)
    BGLabel["font"] = ft
    BGLabel["fg"] = "#333333"
    BGLabel["justify"] = "center"
    BGLabel["text"] = ""
    BGLabel.place(x=3,y=2,width=744,height=594)

    Divider=tk.Label(root)
    Divider["bg"] = "#90ee90"
    ft = tkFont.Font(family='Times',size=10)
    Divider["font"] = ft
    Divider["fg"] = "#333333"
    Divider["justify"] = "center"
    Divider["text"] = ""
    Divider.place(x=0,y=170,width=744,height=3)

    img = GM.getImage("D:\Programming\Python\Room_Rental\Images\Logo.png",172,100)
    Logo=tk.Button(root,image=img)
    Logo.image=img
    Logo["justify"] = "center"
    Logo.place(x=20,y=60,width=172,height=100)

    Title=tk.Button(root)
    Title["bg"] = "#34d8eb"
    ft = tkFont.Font(family='Times',size=25)
    Title["font"] = ft
    Title["fg"] = "#000000"
    Title["justify"] = "center"
    Title["text"] = "Aspire Room Rental Services\n\n"+Room+"'s Tenant Records"
    Title.place(x=210,y=10,width=523,height=150)

    Back=tk.Button(root)
    Back["bg"] = "#eb8c34"
    ft = tkFont.Font(family='Times',size=16)
    Back["font"] = ft
    Back["fg"] = "#000000"
    Back["justify"] = "center"
    Back["text"] = "Back"
    Back.place(x=20,y=10,width=172,height=43)
    Back["command"] = lambda : Back_command(root,user,id)

    History=tk.Button(root)
    History["bg"] = "#ffb800"
    ft = tkFont.Font(family='Times',size=14)
    History["font"] = ft
    History["fg"] = "#2e3436"
    History["justify"] = "center"
    History["text"] = "Show Tenants so far"
    History.place(x=150,y=190,width=450,height=52)
    History["command"] = lambda : History_command(root,id,resultbg)

    Divider2=tk.Label(root)
    Divider2["bg"] = "#90ee90"
    ft = tkFont.Font(family='Times',size=10)
    Divider2["font"] = ft
    Divider2["fg"] = "#333333"
    Divider2["justify"] = "center"
    Divider2["text"] = ""
    Divider2.place(x=3,y=260,width=744,height=2)

    resultbg = tk.Label(root)
    resultbg["fg"] = "#000000"; resultbg["bg"] = "#cccccc"
    resultbg.place(x=20,y=280,width=710,height=300)
    resultbg["text"] = "Search result will appear here..."

def Back_command(root,user,id):
    import OwnerHome as H
    H.main(root,user,id)
        
def History_command(root,id,lbl):
    
    import DatabaseConnection as DB
    available = DB.runQuery2("select count(b_id) from Booking where owner_id = "+str(id))[0]
    if available != 0 :
        Records = DB.runQuery("select S.name,b_id,b_date,Amount,R.city from Booking B, Student S, Room R where B.owner_id = "+str(id)+" AND B.student_id=S.s_id AND B.room_id = R.r_id")
        global treev2
        treev2 = ttk.Treeview(root, selectmode = 'browse', columns=(1, 2, 3, 4, 5, 6), show='headings', height=40, style="Treeview")
        treev2.place(x=20,y=270,width= 710,height=300)
        verscrlbar = ttk.Scrollbar(root, orient ="vertical", command = treev2.yview)
        verscrlbar.pack(side ='right', fill ='x')
        style = ttk.Style()
        style.configure("Treeview", rowheight=70)
        treev2.configure(xscrollcommand = verscrlbar.set)
        
        treev2.column("1", width = 50, anchor ='c')
        treev2.column("2", width = 100, anchor ='c')
        treev2.column("3", width = 30, anchor ='c')
        treev2.column("4", width = 60, anchor ='c')
        treev2.column("5", width = 60, anchor ='c')
        treev2.column("6", width = 95, anchor ='c')
        treev2.heading("1", text="Sr No.")
        treev2.heading("2", text="Tenant Name")
        treev2.heading("3", text="Booking-ID")
        treev2.heading("4", text ="Date")
        treev2.heading("5", text ="Amount")
        treev2.heading("6", text="City")
        
        i = 1
        for R in Records :
            treev2.insert("", 'end', text =str(R[0]), values =(i,R[0],R[1],R[2],R[3],R[4]));    i=i+1

    else :  lbl["text"] = "No Records found !"
