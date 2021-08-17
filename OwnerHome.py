import tkinter as tk
from tkinter.constants import BOTTOM, TOP
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING

from mysql.connector.errors import DatabaseError
import GetImage as GM
import DatabaseConnection as DB; 

def main(root,user,id):
    
    root.title("Home")
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
    BGLabel["justify"] = "center"
    BGLabel.place(x=3,y=1,width=744,height=592)

    img = GM.getImage("D:\Programming\Python\Room_Rental\Images\\addroom.png",160,125)
    AddRoom=tk.Button(root,image=img, compound=TOP)
    AddRoom.image = img
    #AddRoom["bg"] = "#eeefff"
    AddRoom["borderwidth"] = "4px"
    ft = tkFont.Font(family='Times',size=16)
    AddRoom["font"] = ft
    #AddRoom["fg"] = "#2e3436"
    AddRoom["justify"] = "center"
    AddRoom["text"] = "Add Room"
    AddRoom.place(x=70,y=220,width=160,height=155)
    AddRoom["command"] = lambda : AddRoom_command(root,user,id)

    img = GM.getImage("D:\Programming\Python\Room_Rental\Images\\removeroom.png",160,125)
    RemoveRoom=tk.Button(root,image=img,compound=TOP)
    RemoveRoom.image = img
    RemoveRoom["bg"] = "#f6f5f4"
    RemoveRoom["borderwidth"] = "4px"
    ft = tkFont.Font(family='Times',size=16)
    RemoveRoom["font"] = ft
    RemoveRoom["fg"] = "#2e3436"
    RemoveRoom["justify"] = "center"
    RemoveRoom["text"] = "Remove Room"
    RemoveRoom.place(x=300,y=220,width=160,height=155)
    RemoveRoom["command"] = lambda : RemoveRoom_command(root,id)

    img = GM.getImage("D:\Programming\Python\Room_Rental\Images\preview2.jpg",160,125)
    RoomPreview=tk.Button(root,image=img,compound=TOP)
    RoomPreview.image=img
    RoomPreview["bg"] = "#eeeeee"
    RoomPreview["borderwidth"] = "4px"
    ft = tkFont.Font(family='Times',size=16)
    RoomPreview["font"] = ft
    RoomPreview["fg"] = "#2e3436"
    RoomPreview["justify"] = "center"
    RoomPreview["text"] = "Room Preview"
    RoomPreview.place(x=530,y=220,width=160,height=155)
    RoomPreview["command"] = lambda : RoomPreview_command(root,user,'O',id)

    img = GM.getImage("D:\Programming\Python\Room_Rental\Images\history.jpg",160,125)
    BookingHistory=tk.Button(root,image=img,compound=TOP)
    BookingHistory.image=img
    BookingHistory["bg"] = "#f6f5f4"
    BookingHistory["borderwidth"] = "4px"
    ft = tkFont.Font(family='Times',size=16)
    BookingHistory["font"] = ft
    BookingHistory["fg"] = "#2e3436"
    BookingHistory["justify"] = "center"
    BookingHistory["text"] = "Booking History"
    BookingHistory.place(x=70,y=410,width=160,height=155)
    BookingHistory["command"] = lambda : BookingHistory_command(root,user,id)

    img = GM.getImage("D:\Programming\Python\Room_Rental\Images\\record.png",160,125)
    TenantRecord=tk.Button(root,image=img,compound=TOP)
    TenantRecord.image=img
    TenantRecord["bg"] = "#f6f5f4"
    TenantRecord["borderwidth"] = "4px"
    ft = tkFont.Font(family='Times',size=16)
    TenantRecord["font"] = ft
    TenantRecord["fg"] = "#2e3436"
    TenantRecord["justify"] = "center"
    TenantRecord["text"] = "Tenant Record"
    TenantRecord.place(x=300,y=410,width=160,height=155)
    TenantRecord["command"] = lambda : TenantRecord_command(root,user,id)

    Divider=tk.Label(root)
    Divider["bg"] = "#90ee90"
    ft = tkFont.Font(family='Times',size=10)
    Divider["font"] = ft
    Divider["fg"] = "#333333"
    Divider["justify"] = "center"
    Divider["text"] = ""
    Divider.place(x=3,y=180,width=744,height=3)

    img = GM.getImage("D:\Programming\Python\Room_Rental\Images\Logo.png",172,100)
    Logo=tk.Button(root,image=img)
    Logo.image=img
    Logo["justify"] = "center"
    Logo.place(x=20,y=70,width=172,height=100)

    img = GM.getImage("D:\Programming\Python\Room_Rental\Images\\updateroom.png",160,125)
    UpdateRoom=tk.Button(root,image=img,compound=TOP)
    UpdateRoom.image=img
    UpdateRoom["bg"] = "#eeeeee"
    UpdateRoom["borderwidth"] = "4px"
    ft = tkFont.Font(family='Times',size=16)
    UpdateRoom["font"] = ft
    UpdateRoom["fg"] = "#2e3436"
    UpdateRoom["justify"] = "center"
    UpdateRoom["text"] = "Update Room"
    UpdateRoom.place(x=530,y=410,width=160,height=155)
    UpdateRoom["command"] = lambda : UpdateRoom_command(root,user,id)

    Title=tk.Button(root)
    Title["bg"] = "#47ed63"
    ft = tkFont.Font(family='Times',size=25)
    Title["font"] = ft
    Title["fg"] = "#000000"
    Title["justify"] = "center"
    Title["text"] = "Aspires' Room Rental Services\n\n Welcome "+user
    Title.place(x=210,y=20,width=523,height=150)

    Logout=tk.Button(root)
    Logout["bg"] = "#d93636"
    ft = tkFont.Font(family='Times',size=16)
    Logout["font"] = ft
    Logout["fg"] = "#ffffff"
    Logout["justify"] = "center"
    Logout["text"] = "Logout"
    Logout.place(x=20,y=20,width=172,height=43)
    Logout["command"] = lambda : Logout_command(root)

def AddRoom_command(root,user,id):
    import DatabaseConnection as DB ; 
    rc = DB.runQuery2("select count(r_id) from Room where owner_id = "+str(id))[0]
    if rc == 0 :
        import AddRoom as AR;   AR.main(root,user,id,'A')
    else : messagebox.showwarning("Cannot add more Rooms !", "You Already have a room ...delete it to add another !")

def RemoveRoom_command(root,id):
    
    import DatabaseConnection as DB ; 
    countR = DB.runQuery2("select count(r_id) from Room where owner_id = "+str(id))[0]
    if countR != 0 :       
        room_name = DB.runQuery2("select name from Room where owner_id = "+str(id))[0]
        answer = askokcancel( title='Delete Confirmation', message='Are you sure you want to remove the Room named {} ?'.format(room_name), icon=WARNING)
        if answer :
            status = DB.deletion('Room','owner_id',id)
            if status : messagebox.showwarning("Room Deleted", "Room '{}' Deleted Successfully".format(room_name))
            else : messagebox.showerror("Failed", "Oops! something went wrong.")
    else : 
        messagebox.showwarning("Nothing Here !", "Please add a room first !")

def RoomPreview_command(root,user,token,id):
    import DatabaseConnection as DB 
    #countR, room_id = DB.runQuery("select count(r_id),r_id from Room where owner_id = "+str(id))[0]  
    countR = DB.runQuery("select count(r_id) from Room where owner_id = "+str(id))[0]     #for cloud
    room_id = DB.runQuery("select r_id from Room where owner_id = "+str(id))[0]     #for cloud
    if countR != 0 :   
        import RoomPreview as RP;   RP.main(root,user,token,id,room_id)
    else :  
        messagebox.showwarning("Nothing Here","No Preview available, Please add a room")

def BookingHistory_command(root,user,id):
    import DatabaseConnection as DB
    available = int(bool(DB.runQuery("select count(room_id) from Booking where owner_id = "+str(id))[0][0]))  # for cloud
    if available != 0 :
        room_name = DB.runQuery2("select name from Room where owner_id = "+str(id))[0]
        import OwnerHistory as OH
        OH.main(root,room_name,user,id)
    else :
        messagebox.showwarning("Nothing Here !", "No Customer found !")

def TenantRecord_command(root,user,id):
    import DatabaseConnection as DB
    available = int(bool(DB.runQuery("select count(room_id) from Booking where owner_id = "+str(id))[0][0]))  # for cloud
    if available != 0 :
        room_name = DB.runQuery2("select name from Room where owner_id = "+str(id))[0]
        import TenantRecord as OH
        OH.main(root,room_name,user,id)
    else :
        messagebox.showwarning("Nothing Here !", "No booking found !")

def UpdateRoom_command(root,user,id):
    import DatabaseConnection as DB
    rc = DB.runQuery2("select count(r_id) from Room where owner_id = "+str(id))[0]
    if rc !=0 :
        import AddRoom as AR;   AR.main(root, user, id, 'U')
    else : 
        messagebox.showwarning("Nothing Here !", "Please add a room first !")

def Logout_command(root):
    answer = askokcancel( title='Logout Confirmation', message='Are you sure to logout ?', icon=WARNING)
    if answer :
        import Welcome as welcome
        welcome.App(root)

