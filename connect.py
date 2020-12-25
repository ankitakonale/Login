import tkinter as tk
from tkinter import *

import mysql.connector


def submitact():
    user = Username.get()
    passw = password.get()
    finge = fingerprint.get()
    print(user + " " + passw + " " + finge)

    print("The name entered by you is {user}{passw}{finge}")

    logintodb(user, passw, finge)


def logintodb(user, passw, finge):
    # If paswword is enetered by the
    # user
    if passw:
        db = mysql.connector.connect(host="localhost",
                                     user=user,
                                     password=passw,
                                     db="bankData"
                                     )
        cursor = db.cursor()

        # If no password is enetered by the
    # user
    else:
        db = mysql.connector.connect(host="localhost",
                                     user=user,
                                     db="bankData")
        cursor = db.cursor()

        # A Table in the database
    savequery = "select * from bank"

    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()

        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        print("Query Excecuted successfully")

    except Exception as e:
        db.rollback()
        print(e)
        print("Error occured")


root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")

C = Canvas(root, bg="blue", height=250, width=300)

# Definging the first row
lblfrstrow = tk.Label(root, text="Username -", )
lblfrstrow.place(x=50, y=20)

Username = tk.Entry(root, width=35)
Username.place(x=150, y=20, width=100)

lblsecrow = tk.Label(root, text="Password -")
lblsecrow.place(x=50, y=50)

password = tk.Entry(root, width=35)
password.place(x=150, y=50, width=100)

lblsecrow = tk.Label(root, text="Fingerprint-")
lblsecrow.place(x=50, y=80)

fingerprint = tk.Entry(root, width=35)
fingerprint.place(x=150, y=80, width=100)

submitbtn = tk.Button(root, text="Login",
                      bg='blue', command=submitact)
submitbtn.place(x=150, y=135, width=55)

root.mainloop()
