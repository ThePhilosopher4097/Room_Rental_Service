import tkinter as tk
from tkinter import messagebox
from tkinter.constants import LEFT
import tkinter.font as tkFont
import GetImage as GM
from tkinter.messagebox import askokcancel, showinfo, WARNING

def main(root,user,token,id,Room_ID):
    
    root.title("Room Preview")
    width=750
    height=600
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    BgImg = GM.getImage("D:\Programming\Python\Room_Rental\Images\BG.jpg", 744, 592)
    BGLabel=tk.Label(root,image=BgImg)
    BGLabel.image=BgImg;    BGLabel["bg"] = "#393d49"
    BGLabel.place(x=3,y=2,width=744,height=594)

    Divider1=tk.Label(root)
    Divider1["bg"] = "#90ee90"
    Divider1["fg"] = "#333333"
    Divider1["justify"] = "center"
    Divider1.place(x=0,y=170,width=744,height=3)

    img = GM.getImage("D:\Programming\Python\Room_Rental\Images\Logo.png",172,100)
    Logo=tk.Button(root,image=img)
    Logo.image=img
    Logo["bg"] = "#f6f5f4"
    Logo["justify"] = "center"
    Logo.place(x=20,y=60,width=172,height=100)

    img = GM.getImage("D:\Programming\Python\Room_Rental\Images\preview1.jpg",150,150)
    Title=tk.Button(root,image=img,compound=LEFT)
    Title.image=img
    Title["bg"] = "#34d8eb"
    ft = tkFont.Font(family='Times',size=25)
    Title["font"] = ft
    Title["fg"] = "#000000"
    Title["justify"] = "center"
    Title["text"] = "Aspires Room Rental\n\nRoom Preview"
    Title.place(x=210,y=10,width=523,height=150)

    Back=tk.Button(root)
    Back["bg"] = "#eb8c34"
    ft = tkFont.Font(family='Times',size=16)
    Back["font"] = ft
    Back["fg"] = "#000000"
    Back["justify"] = "center"
    Back["text"] = "Back"
    Back.place(x=20,y=10,width=172,height=43)
    Back["command"] = lambda : Back_command(root,user,token,id)

    Name=tk.Label(root,highlightbackground = "yellow", highlightcolor= "yellow", highlightthickness=2)
    Name["bg"] = "#393d49"
    Name["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    Name["font"] = ft
    Name["fg"] = "#ffffff"
    Name["justify"] = "center"
    Name["text"] = "Name"
    Name.place(x=320,y=180,width=410,height=45)

    Location=tk.Text(root)
    Location["bg"] = "#ffffff"
    Location["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    Location["font"] = ft
    Location["fg"] = "#000000"
    Location.place(x=320,y=280,width=410,height=90)

    City=tk.Label(root,highlightbackground = "yellow", highlightcolor= "yellow", highlightthickness=2)
    City["bg"] = "#393d49"
    City["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    City["font"] = ft
    City["fg"] = "#ffffff"
    City["justify"] = "center"
    City["text"] = ""
    City.place(x=320,y=232,width=410,height=40)

    Amenities=tk.Text(root)
    Amenities["bg"] = "#ffffff"
    Amenities["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    Amenities["font"] = ft
    Amenities["fg"] = "#000000";    
    Amenities.place(x=320,y=490,width=410,height=90)

    Type=tk.Label(root)
    Type["bg"] = "#ffffff"
    Type["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    Type["font"] = ft
    Type["fg"] = "#000000"
    Type["justify"] = "center"
    Type["text"] = "Rent"
    Type.place(x=370,y=380,width=190,height=45)

    Rent=tk.Label(root)
    Rent["bg"] = "#ffffff"
    Rent["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    Rent["font"] = ft
    Rent["fg"] = "#000000"
    Rent["justify"] = "center"
    Rent["text"] = "Rent"
    Rent.place(x=635,y=380,width=95,height=45)

    RentLabel=tk.Label(root)
    RentLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=13)
    RentLabel["font"] = ft
    RentLabel["fg"] = "#ffffff"
    RentLabel["justify"] = "center"
    RentLabel["text"] = "Rent"
    RentLabel.place(x=575,y=380,width=60,height=45)

    TypeLabel=tk.Label(root)
    TypeLabel["bg"] = "#393d49"
    ft = tkFont.Font(family='Times',size=13)
    TypeLabel["font"] = ft
    TypeLabel["fg"] = "#ffffff"
    TypeLabel["justify"] = "center"
    TypeLabel["text"] = "Type"
    TypeLabel.place(x=320,y=380,width=50,height=45)

    if token == 'S' :
        Book=tk.Button(root)
        Book["bg"] = "#46eb43"
        Book["borderwidth"] = "4px"
        ft = tkFont.Font(family='Times',size=16)
        Book["font"] = ft
        Book["fg"] = "#2e3436"
        Book["justify"] = "center"
        Book["text"] = "Proceed to Book"
        Book.place(x=10,y=500,width=295,height=52)
        Book["command"] = lambda : Book_command(root,user,token,id,Room_ID,Rent["text"])

    img = GM.getImage("D:\Programming\Python\Room_Rental\Images\search.jpg",297,300)
    Photo=tk.Button(root,image=img)
    Photo.image = img
    Photo["bg"] = "#f6f5f4"
    ft = tkFont.Font(family='Times',size=10)
    Photo["font"] = ft
    Photo["fg"] = "#2e3436"
    Photo["justify"] = "center"
    Photo["text"] = "Image of room"
    Photo.place(x=10,y=180,width=300,height=300)

    Owner=tk.Label(root)
    Owner["bg"] = "#393d49"
    Owner["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    Owner["font"] = ft
    Owner["fg"] = "#ffffff"
    Owner["justify"] = "center"
    Owner["text"] = ""
    Owner.place(x=320,y=440,width=240,height=37)

    Contact=tk.Label(root)
    Contact["bg"] = "#393d49"
    Contact["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=14)
    Contact["font"] = ft
    Contact["fg"] = "#ffffff"
    Contact["justify"] = "center"
    Contact["text"] = ""
    Contact.place(x=575,y=440,width=155,height=36)

    FillPage(Room_ID,Name,Location,City,Amenities,Type,Rent,Owner,Contact,Photo)

def Back_command(root,user,token,id):
    if token == 'S' :   import StudentHome as SH; SH.main(root,user,id)
    else : import OwnerHome as OH; OH.main(root,user,id)

def Book_command(root,user,token,id,Room_ID,p):
    answer = askokcancel( title='Booking Confirmation', message='Are you sure about Booking the Room ? (you cannot cancel once booked)', icon=WARNING)
    if answer  :
        import DatabaseConnection as DB
        room_name = DB.runQuery2("select name from Room where r_id = "+str(Room_ID))[0]
        from datetime import datetime;  now = datetime.now();  
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        bid = 1
        try : bid = int(DB.runQuery("select max(b_id) from Booking")[0][0]) + 1
        except : bid = 1
        owner_id = DB.runQuery2("select owner_id from Room where r_id = "+str(Room_ID))[0]
        DB.insertBooking(int(bid),formatted_date,int(p),int(owner_id),int(id),int(Room_ID))
        DB.runQuery2("update Booking set b_date = now() where room_id = "+str(Room_ID))
        messagebox.showinfo("Success !", "Room named {} booked for {}".format(room_name,user))
        import StudentHome as Home; Home.main(root,user,id)

def FillPage(Room_ID,Name,Location,City,Amenities,Type,Rent,Owner,Contact,Photo) :

    import DatabaseConnection as DB
    Tup = DB.runQuery2("select name, location, city, Amenities, type, price, owner_name from Room where r_id = %s" % (Room_ID))
    #contact = str(DB.runQuery2("select mobile from Owner where o_id = (select owner_id from Room where r_id = "+str(Room_ID)+")"))[1:11]
    contact = str(DB.runQuery2("select mobile from Owner where o_id = (select owner_id from Room where r_id = %s)" % (Room_ID)))[1:11]  #cloud

    Name["text"] = Tup[0];    City["text"] = Tup[2];    Type["text"] = Tup[4];    Rent["text"] = Tup[5]
    Owner["text"] = "Owner : "+Tup[6];  Contact["text"] = "(+91) "+contact
    Location.insert(tk.END,Tup[1])
    Amenities.insert(tk.END,Tup[3])

    Location.config(state="disabled")
    Amenities.config(state="disabled")

    import mysql.connector
    from PIL import Image, ImageTk
    from io import BytesIO
    import PIL.Image
    #cnx = mysql.connector.connect(host="localhost", user="root",password="", database="RoomRental")
    #cnx = mysql.connector.connect(user="ugqiri0xcve8arnj", password="W05Xj0GMrQfciurwXyku", host="b1d548joznqwkwny7elp-mysql.services.clever-cloud.com",database="b1d548joznqwkwny7elp")
    cnx = mysql.connector.connect(host = "remotemysql.com", user="o67DNqMxP5",password="JHs8dXYWg4", database="o67DNqMxP5")
    cursor = cnx.cursor(buffered=True)
    cursor.execute("select images from Room where r_id = %s" %(Room_ID))
    data = cursor.fetchall()
    img = data[0][0]
    img1 = Image.open(BytesIO(img))
    render = ImageTk.PhotoImage(img1.resize((297,300),Image.ANTIALIAS))
    Photo.config(image=render)
    Photo.image=render; 