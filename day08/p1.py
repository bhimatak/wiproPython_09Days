'''
test mysql-connector
'''
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "bhima",
    password = "Bhima@123456"
)

mycur = mydb.cursor()

mycur.execute('create database testdb')