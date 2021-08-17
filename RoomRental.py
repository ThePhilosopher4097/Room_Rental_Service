import mysql.connector
import uuid
import sys
from PIL import Image
import base64
import io
import PIL.Image
from mysql.connector.errors import custom_error_exception
from datetime import datetime

cnx = mysql.connector.connect(user="ugqiri0xcve8arnj", password="W05Xj0GMrQfciurwXyku", host="b1d548joznqwkwny7elp-mysql.services.clever-cloud.com",database="b1d548joznqwkwny7elp")
cursor = cnx.cursor(buffered=True)

def createTables () :

    query = ("CREATE TABLE Booking (Booking_id int(10) primary key, b_date date NOT NULL, Amount int(5) NOT NULL, Transaction_id int(10) NOT NULL)")
    cursor.execute(query)
    query = ("CREATE TABLE Room (room_id int(10) primary key ,type VARCHAR(10) NOT NULL, city VARCHAR(20) NOT NULL , owner_name VARCHAR(40) NOT NULL ,price int NOT NULL ,Amenities VARCHAR(40)NOT NULL, images BLOB, loaction VARCHAR(20))")
    cursor.execute(query)
    query = ("CREATE TABLE owner (o_id int(10) primary key ,name VARCHAR(40) NOT NULL ,gender VARCHAR(10) NOT NULL ,mobile double(10,0) NOT NULL ,email VARCHAR(40)NOT NULL ,Booking_id int(10) NOT NULL ,room_id int(10) NOT NULL,FOREIGN KEY(room_id) references Room(room_id))")
    cursor.execute(query)
    query = ("CREATE TABLE student_dataset (s_id int(10) primary key ,name VARCHAR(40) NOT NULL, address VARCHAR(40)NOT NULL ,gender VARCHAR(10)NOT NULL ,DOB date NOT NULL, Email VARCHAR(40) NOT NULL, mobile double(10,2) NOT NULL, Booking_id int(10) NOT NULL, FOREIGN KEY(Booking_id) references Booking(Booking_id))")
    cursor.execute(query)

def encodeimage (F) :        
    
    with open(F, 'rb') as f:
        photo = f.read()
    encodestring = base64.b64encode(photo)
    return encodestring

def insertRoom() :
    
    valuetuple = (3, '2 BHK', 'Pune', 'Prajwal Gandhi', 10000, 'Wifi 24x7 Water and Electricity', encodeimage("D:\Programming\Python\Room Rental\Room3.jpg"), 'Katraj')
    query = ("insert into Room values (%s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(query,valuetuple)
    cnx.commit()

def insertOwner() :
    
    valuetuple = (3, 'Prajwal Gandhi', 'Male', 8798120156, 'gandhi.prajwal@gmail.com', 1002, 3)
    query = ("insert into owner values (%s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(query,valuetuple)
    cnx.commit()

def insertStudent () :

    valuetuple = (1, 'Kishor Sawant', 'Pune', 'Male', datetime(2001,1,1), 'rajendra.patil@gmail.com', 7498173960, None)
    query = ("insert into student_dataset values (%s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(query,valuetuple)
    cnx.commit()

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
        binary_data = base64.b64decode(image)
        image = Image.open(io.BytesIO(binary_data))
        image.show()
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

#createTables()
#insertRoom()
#insertOwner()
#insertStudent()
#addBooking()
print("Owners : ");     show('o_id', 1, 'owner', None)
print("Rooms : ");      show(None, None, 'Room', 'room_id, type, city, owner_name, price, Amenities')
print("Students : ");   show(None, None, 'student_dataset', None)
show ('room_id', 1, 'Room', 'images')
#deleteRecord('owner', 'o_id', 1)
cursor.close()
cnx.close()