import mysql.connector
import uuid
import sys
from PIL import Image
import base64
import io
from tkinter import *
import PIL.Image
from mysql.connector.errors import _ERROR_EXCEPTIONS, custom_error_exception
from datetime import datetime

#cnx = mysql.connector.connect(user="ugqiri0xcve8arnj", password="W05Xj0GMrQfciurwXyku", host="b1d548joznqwkwny7elp-mysql.services.clever-cloud.com",database="b1d548joznqwkwny7elp") #cloud database
#cnx = mysql.connector.connect(host="localhost", user="root",password="", database="RoomRental")
#cnx = mysql.connector.connect(host = "remotemysql.com", user="IcJwidzu9e",password="9NUoukBVoK", database="IcJwidzu9e")
#cnx = mysql.connector.connect(host = "remotemysql.com", user="o67DNqMxP5",password="JHs8dXYWg4", database="o67DNqMxP5")
cnx = mysql.connector.connect(host = "remotemysql.com", user="EwmqQ4IUIL",password="v1HmeI6k2s", database="EwmqQ4IUIL")
cursor = cnx.cursor(buffered=True)

def runQuery(query) :
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def runQuery2(query) :
    cursor.execute(query)
    data = cursor.fetchone()
    cnx.commit()
    return data

def createTables () :

    query = ("CREATE TABLE Owner (o_id int(10) primary key , name VARCHAR(40) NOT NULL ,gender VARCHAR(10) NOT NULL ,mobile double(10,0) NOT NULL , email VARCHAR(40)NOT NULL, password VARCHAR(20) NOT NULL, CONSTRAINT UC_owner UNIQUE(password,email))")
    cursor.execute(query)
    query = ("CREATE TABLE Room (r_id int(10) primary key ,type VARCHAR(10) NOT NULL, city VARCHAR(20) NOT NULL , owner_id int(10) NOT NULL, owner_name VARCHAR(40) NOT NULL ,price int NOT NULL ,Amenities VARCHAR(40)NOT NULL, images BLOB, location VARCHAR(20), name VARCHAR(50)  NOT NULL, FOREIGN KEY(owner_id) references Owner(o_id))")
    cursor.execute(query)
    query = ("CREATE TABLE Student (s_id int(10) primary key , name VARCHAR(40) NOT NULL, address VARCHAR(40)NOT NULL ,gender VARCHAR(10) NOT NULL ,DOB date NOT NULL, email VARCHAR(40) NOT NULL, mobile double(10,0) NOT NULL, password VARCHAR(20) NOT NULL, CONSTRAINT UC_student UNIQUE(password,email))")
    cursor.execute(query)
    query = ("CREATE TABLE Booking (b_id int(10) primary key, b_date date NOT NULL, Amount int(5) NOT NULL, owner_id int(10) NOT NULL, student_id int(10) NOT NULL, room_id int(10) NOT NULL, FOREIGN KEY(student_id) references Student(s_id), FOREIGN KEY(room_id) references Room(r_id))")
    cursor.execute(query)

def encodeimage (F) :        
    
    with open(F, 'rb') as f:
        photo = f.read()
    #encodestring = base64.b64encode(photo)
    #return encodestring
    return photo

def insertRoom(r_id,type,city,owner_id,owner_name,price,amenities,img,location,name) :
    valuetuple = (r_id,type,city,owner_id,owner_name,price,amenities,encodeimage(img),location,name)
    query = ("insert into Room values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(query,valuetuple)
    cnx.commit()

def insertOwner(id,name,gender,mobile,email,password) :
    try :
        valuetuple = (id,name,gender,mobile,email,password)
        query = ("insert into Owner values (%s, %s, %s, %s, %s, %s)")
        cursor.execute(query,valuetuple)
        cnx.commit()
        return True
    except : return False

def insertStudent (student_id,n,a,g,d,e,m,p) :
    try :
        valuetuple = (student_id,n,a,g,d,e,m,p)
        query = ("insert into Student values (%s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(query,valuetuple)
        cnx.commit()
        return True
    except : return False

def insertBooking(i,d,a,t,s,r) :
    valuetuple = (i,d,a,t,s,r)
    query = ("insert into Booking values (%s,%s,%s,%s,%s,%s)")
    cursor.execute(query,valuetuple)
    cnx.commit()

def deletion(whom,col,id) :
    try :
        query = (f"delete from {whom} where {col} = {id}")
        cursor.execute(query)
        cnx.commit()
        return True
    except : return False

def show (IDcol, ID, who, what) :

    if ID is not None and IDcol is not None : forone =  " where {} = ".format(IDcol) + str(ID)
    else : forone = ''
    if what is not None : cols = ''.join(what)
    else : cols = '*'
    query =  ("select {} from {}".format(cols, who) + forone)
    cursor.execute(query)
    data = cursor.fetchall()

    if what == 'images' :
        
        image = data[0][0]          # Image if any
        """binary_data = base64.b64decode(image)
        image = Image.open(io.BytesIO(binary_data))
        image = image.open(io.BytesIO(image))
        image.show()
        """
        import tkinter as tk
        from PIL import Image, ImageTk
        from io import BytesIO
        root = tk.Tk()
        root.geometry("700x2000")
        img = Image.open(BytesIO(image))
        render = ImageTk.PhotoImage(img.resize((700,500),PIL.Image.ANTIALIAS))
        img = Label(root,image=render)
        img.image=render; 
        img.place(x=0,y=0)
        root.mainloop()
    else :
        for i in data :
            print(i)

def deleteRecord (Table, key, keyval) :
    if key is not None and keyval is not None :
        query = ("delete from {} where {} = {}".format(Table, key, keyval))
    else :
        query = ("truncate table {}".format(Table))   
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()

def deleteTables (Which) :
    if Which != 'All' : query = ("drop table {}".format(Which)); cursor.execute(query); cnx.commit()
    elif Which == 'All' :  
        query = ("drop table Booking"); cursor.execute(query); cnx.commit()
        query = ("drop table Room"); cursor.execute(query); cnx.commit()
        query = ("drop table Owner"); cursor.execute(query); cnx.commit()
        query = ("drop table Student"); cursor.execute(query); cnx.commit()
    cursor.close()
    cnx.close()

#createTables()
#insertRoom()
#insertOwner()
#insertStudent()
#addBooking()
#print("Owners : ");     show('o_id', 1, 'owner', None)
#print("Rooms : ");      show(None, None, 'Room', 'r_id, type, city, owner_name, price, Amenities')
#print("Students : ");   show(None, None, 'student_dataset', None)
#show ('r_id', 1, 'Room', 'images')
#deleteRecord('owner', 'o_id', 1)
#deleteTables('All')