import mysql.connector
import uuid

cnx = mysql.connector.connect(user="ugqiri0xcve8arnj",
password="W05Xj0GMrQfciurwXyku",host="bmdimdcqducjlo3jzyii-mysql.services.clever-cloud.com",database="b1d548joznqwkwny7elp")

#import mysql.connector
#import uuid
#cnx = mysql.connector.connect(user="uprrqljln2zkcgtq",
#password="UBKHGqi4XGkGAb1Zy4En",host="b1d548joznqwkwny7elp-mysql.services.clever-cloud.com",database="bmdimdcqducjlo3jzyii")

cursor = cnx.cursor(buffered=True)

query = ("delete from DEMO where ID = 2")
cursor.execute(query)
cnx.commit()
query = ("delete from DEMO where ID = 3")
cursor.execute(query)
cnx.commit()
#query = ("CREATE TABLE DEMO (ID INT, NAME VARCHAR(20))")
#query = ("insert into DEMO values (1, 'Shreyash Yewale')")
query = ("insert into DEMO values (2, 'Sanket Salunke')")
cursor.execute(query)
cnx.commit()
query = ("insert into DEMO values (3, 'Sameer Patil')")
cursor.execute(query)
cnx.commit()

query = ("select * from DEMO")
cursor.execute(query)
data = cursor.fetchall()
print(data)

cursor.close()
cnx.close()