import tkinter as tk
import tkinter.font as tkFont
import GetImage as GM
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING

RoomImage = ''
def main(root,user,id,pagetoken):
    
    root.title("Add Room")
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
    Logo.place(x=20,y=60,width=172,height=100)

    Title=tk.Button(root)
    Title["bg"] = "#34d8eb"
    ft = tkFont.Font(family='Times',size=25)
    Title["font"] = ft
    Title["fg"] = "#000000"
    Title["justify"] = "center"
    if pagetoken == 'A' : tstr = ' Add Room'
    else : tstr = ' Update Room'
    Title["text"] = "Aspire Room Rental Services \n\n"+tstr
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

    Name=tk.Entry(root)
    Name["bg"] = "#ffffff"
    Name["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    Name["font"] = ft
    Name["fg"] = "#333333"
    Name["justify"] = "center"
    Name["text"] = ""
    Name.place(x=30,y=230,width=350,height=45)

    Location=tk.Text(root)
    Location["bg"] = "#ffffff"
    Location["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    Location["font"] = ft
    Location["fg"] = "#333333"
    Location.place(x=30,y=330,width=350,height=100)

    City=tk.Entry(root)
    City["bg"] = "#ffffff"
    City["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    City["font"] = ft
    City["fg"] = "#333333"
    City["justify"] = "center"
    City["text"] = ""
    City.place(x=400,y=230,width=325,height=45)

    Amenities=tk.Text(root)
    Amenities["bg"] = "#ffffff"
    Amenities["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    Amenities["font"] = ft
    Amenities["fg"] = "#333333"
    Amenities.place(x=400,y=330,width=325,height=100)

    Type=tk.Entry(root)
    Type["bg"] = "#ffffff"
    Type["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    Type["font"] = ft
    Type["fg"] = "#333333"
    Type["justify"] = "center"
    Type["text"] = ""
    Type.place(x=140,y=450,width=240,height=45)

    NameLabel=tk.Label(root)
    NameLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=13)
    NameLabel["font"] = ft
    NameLabel["fg"] = "#ffffff"
    NameLabel["justify"] = "center"
    NameLabel["text"] = "Specify  Room Name"
    NameLabel.place(x=110,y=190,width=180,height=30)

    CityLabel=tk.Label(root)
    CityLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=13)
    CityLabel["font"] = ft
    CityLabel["fg"] = "#ffffff"
    CityLabel["justify"] = "center"
    CityLabel["text"] = "City"
    CityLabel.place(x=470,y=190,width=180,height=30)

    LocationLabel=tk.Label(root)
    LocationLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=13)
    LocationLabel["font"] = ft
    LocationLabel["fg"] = "#ffffff"
    LocationLabel["justify"] = "center"
    LocationLabel["text"] = "Room Location"
    LocationLabel.place(x=110,y=290,width=180,height=30)

    AmenitiesLabel=tk.Label(root)
    AmenitiesLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=13)
    AmenitiesLabel["font"] = ft
    AmenitiesLabel["fg"] = "#ffffff"
    AmenitiesLabel["justify"] = "center"
    AmenitiesLabel["text"] = "Specify Amenities"
    AmenitiesLabel.place(x=470,y=290,width=180,height=30)

    Price=tk.Entry(root)
    Price["bg"] = "#ffffff"
    Price["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=13)
    Price["font"] = ft
    Price["fg"] = "#333333"
    Price["justify"] = "center"
    Price["text"] = ""
    Price.place(x=470,y=450,width=100,height=45)

    PriceLabel=tk.Label(root)
    PriceLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=13)
    PriceLabel["font"] = ft
    PriceLabel["fg"] = "#ffffff"
    PriceLabel["justify"] = "center"
    PriceLabel["text"] = "Rent (₹)"
    PriceLabel.place(x=400,y=450,width=70,height=45)

    TypeLabel=tk.Label(root)
    TypeLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=13)
    TypeLabel["font"] = ft
    TypeLabel["fg"] = "#ffffff"
    TypeLabel["justify"] = "center"
    TypeLabel["text"] = "Room Type"
    TypeLabel.place(x=30,y=450,width=100,height=45)

    Done=tk.Button(root)
    Done["bg"] = "#46eb43"
    Done["borderwidth"] = "4px"
    ft = tkFont.Font(family='Times',size=16)
    Done["font"] = ft
    Done["fg"] = "#2e3436"
    Done["justify"] = "center"
    Done["text"] = "Done"
    Done.place(x=250,y=530,width=286,height=53)
    Done["command"] = lambda : Done_command(root,id,Price.get(),Location.get("1.0", "end-1c"),Name.get(),City.get(),user,Amenities.get("1.0", "end-1c"),Type.get(),pagetoken)

    ChooseImage=tk.Button(root)
    ChooseImage["bg"] = "#393d49"
    ChooseImage["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=13)
    ChooseImage["font"] = ft
    ChooseImage["fg"] = "#ffffff"
    ChooseImage["justify"] = "center"
    ChooseImage["text"] = "Choose Image"
    ChooseImage.place(x=580,y=450,width=150,height=45)
    ChooseImage["command"] = lambda : ChooseImage_command(root,ChooseImage)

def Back_command(root,user,id):
    import OwnerHome as Home
    Home.main(root,user,id)

def Done_command(root,id,p,l,n,c,o,a,t,pagetoken):
    if check_float(p)==False or l=='' or n=='' or c=='' or o=='' or a=='' or t=='' or RoomImage=='' :
        messagebox.showerror("Failed ! ","Error : Some fields are still empty.")
    else : 
        print(p,a,n,l,c,o,t,RoomImage)
        import DatabaseConnection as DB
        if pagetoken == 'A' :
            #room_id = DB.runQuery("select max(r_id) from Room")[0][0] + 1
            room_id = int(bool(DB.runQuery("select max(r_id) from Room")[0][0])) + 1 #for cloud
            DB.insertRoom(room_id,t,c,id,o,p,a,RoomImage,l,n)
            messagebox.showinfo("Success !","Room Added Successfully.")
            owner_name = DB.runQuery2("select owner_name from Room where r_id = "+str(room_id))
            import OwnerHome as Home; Home.main(root,owner_name[0],id)
        elif pagetoken == 'U' :
            room_id = DB.runQuery2("select r_id from Room where owner_id = "+str(id))
            owner_name = DB.runQuery2("select owner_name from Room where r_id = "+str(room_id))
            print(owner_name)
            DB.runQuery2("update Room set type = '%s', city = '%s', owner_id = %s, owner_name = '%s', price = %s, Amenities = '%s', location = '%s', name = '%s' where r_id = %s" % (t,c,int(id),owner_name[0],int(p),a,l,n,int(room_id[0])))
            messagebox.showinfo("Success !","Room Updated Successfully.")
        import OwnerHome as Home; Home.main(root,owner_name[0],id)

def ChooseImage_command(root,C):
    import easygui; global RoomImage
    RoomImage = easygui.fileopenbox()
    if RoomImage != '' :
        C["fg"] = '#33ff22'

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False