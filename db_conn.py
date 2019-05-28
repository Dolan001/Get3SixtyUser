import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="dolan",
    passwd="dolan159320",
    db="Get2"
)
cursor = mydb.cursor()
