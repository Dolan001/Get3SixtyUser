import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dolan",
  passwd="dolan159320"
)
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE Get2")
print("Database Created....")

cursor.execute("USE Get2")
cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY,firstname VARCHAR(255), lastname VARCHAR(255),"
               "email VARCHAR (100), password VARCHAR (1000),phone_no INT(50), address VARCHAR (100),"
               "city VARCHAR (100), state VARCHAR (100), country varchar (100), postal_code varchar (50))")
print("Database table created...")
