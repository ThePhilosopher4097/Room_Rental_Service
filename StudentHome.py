from AddRoom import RoomImage
import tkinter as tk
from tkinter import ttk
from tkinter.constants import LEFT
import tkinter.font as tkFont
import GetImage as GM
from tkinter import Frame, messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING

treev = ''; treev2 = ''; Root = '';  User = '';  ID = ''
def main(root,user,id):

    global User;   User = user;   global Root;   Root = root;   global ID;  ID = id
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
    Title["text"] = "Aspire Room Rental Services\n\nWelcome "+user
    Title.place(x=210,y=10,width=523,height=150)

    Logout=tk.Button(root)
    Logout["bg"] = "#eb8c34"
    ft = tkFont.Font(family='Times',size=16)
    Logout["font"] = ft
    Logout["fg"] = "#000000"
    Logout["justify"] = "center"
    Logout["text"] = "Logout"
    Logout.place(x=20,y=10,width=172,height=43)
    Logout["command"] = lambda : Logout_command(root)

    SearchBar=tk.Entry(root)
    SearchBar["bg"] = "#ffffff"
    SearchBar["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=15)
    SearchBar["font"] = ft
    SearchBar["fg"] = "#000000"
    SearchBar["justify"] = "center"
    SearchBar["text"] = ""
    SearchBar.place(x=20,y=190,width=360,height=50)

    img = GM.getImage("D:\Programming\Python\Room_Rental\Images\search.jpg",50,45)
    Search=tk.Button(root,image=img,compound=LEFT)
    Search.image=img
    Search["bg"] = "#77eb34"
    ft = tkFont.Font(family='Times',size=14)
    Search["font"] = ft
    Search["fg"] = "#2e3436"
    Search["justify"] = "center"
    Search["text"] = "Search"
    Search.place(x=390,y=190,width=120,height=50)
    Search["command"] = lambda : Search_command(root,SearchBar.get(),resultbg)

    """MyRooms=tk.Button(root)
    MyRooms["bg"] = "#ffb800"
    ft = tkFont.Font(family='Times',size=14)
    MyRooms["font"] = ft
    MyRooms["fg"] = "#2e3436"
    MyRooms["justify"] = "center"
    MyRooms["text"] = "My \nRooms"
    MyRooms.place(x=530,y=190,width=100,height=52)
    MyRooms["command"] = lambda : MyRooms_command(root)
    """
    History=tk.Button(root)
    History["bg"] = "#ffb800"
    ft = tkFont.Font(family='Times',size=14)
    History["font"] = ft
    History["fg"] = "#2e3436"
    History["justify"] = "center"
    History["text"] = "Booking History"
    History.place(x=530,y=190,width=200,height=52)
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

def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are you sure to logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.App(root)


def MyRooms_command(root):
    print("command")


def History_command(root,id,lbl):
    
    import DatabaseConnection as DB
    available = DB.runQuery2("select count(b_id) from Booking where student_id = "+str(id))[0]
    if available != 0 :
        Records = DB.runQuery("select b_id,b_date,Amount,owner_name,name,city from Booking B, Room R where student_id = "+str(id)+" AND B.owner_id=R.owner_id")
        global treev2
        treev2 = ttk.Treeview(root, selectmode = 'browse', columns=(1, 2, 3, 4, 5, 6, 7), show='headings', height=40, style="Treeview")
        treev2.place(x=20,y=270,width= 710,height=300)
        verscrlbar = ttk.Scrollbar(root, orient ="vertical", command = treev2.yview)
        verscrlbar.pack(side ='right', fill ='x')
        style = ttk.Style()
        style.configure("Treeview", rowheight=70)
        treev2.configure(xscrollcommand = verscrlbar.set)
        
        treev2.column("1", width = 25, anchor ='c')
        treev2.column("2", width = 25, anchor ='c')
        treev2.column("3", width = 50, anchor ='c')
        treev2.column("4", width = 45, anchor ='c')
        treev2.column("5", width = 60, anchor ='c')
        treev2.column("6", width = 70, anchor ='c')
        treev2.column("7", width = 120, anchor ='c')
        treev2.heading("1", text="Sr No.")
        treev2.heading("2", text="Booking-ID")
        treev2.heading("3", text ="Date")
        treev2.heading("4", text ="Amount")
        treev2.heading("5", text ="City")
        treev2.heading("6", text ="Owner Name")
        treev2.heading("7", text="Room Name")
        i = 1
        for R in Records :
            treev2.insert("", 'end', text =str(R[0]), values =(i,R[0],R[1],R[2],R[5],R[3],R[4]));    i=i+1

    else :  lbl["text"] = "No Records found !"

def Search_command(root,key,lbl) :

    if len(key) != 0 :
        import DatabaseConnection as DB
        Records = DB.runQuery("select r_id,name,type,city,price from Room where location LIKE '%{}%' OR city LIKE '%{}%'".format(key,key))
        print(Records)
        if len(Records) !=0 :
            global treev
            treev = ttk.Treeview(root, selectmode = 'browse', columns=(1, 2, 3, 4, 5), show='headings', height=40, style="Treeview")
            treev.place(x=20,y=270,width= 710,height=300)
            verscrlbar = ttk.Scrollbar(root, orient ="vertical", command = treev.yview)
            verscrlbar.pack(side ='right', fill ='x')
            style = ttk.Style()
            style.configure("Treeview", rowheight=90)
            treev.configure(xscrollcommand = verscrlbar.set)
            
            treev.column("1", width = 30, anchor ='c')
            treev.column("2", width = 90, anchor ='c')
            treev.column("3", width = 90, anchor ='c')
            treev.column("4", width = 90, anchor ='c')
            treev.column("5", width = 90, anchor ='c')
            treev.heading("1", text="Room-ID")
            treev.heading("2", text ="Room Name")
            treev.heading("3", text ="Room Type")
            treev.heading("4", text ="City")
            treev.heading("5", text ="Rent")
            for R in Records :
                treev.insert("", 'end', text =str(R[0]), values =(R[0],R[1],R[2],R[3],R[4]))
            treev.bind("<Double-1>",gotoPreview)

    else :  lbl["text"] = "No rooms found for the given location...try something else"; 

def gotoPreview (event) :
    item=treev.selection()[0]
    print(treev.item(item,"values")[0])
    Room_ID = treev.item(item,"values")[0]
    import RoomPreview as RP;   RP.main(Root,User,'S',ID,Room_ID)