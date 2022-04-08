import tkinter as tk
import sys
import os
from tkinter import *
import global_variables

from tkinter import ttk
from tkmacosx import Button
import pandas as pd
from functools import partial

from IPython.display import display
import mysql.connector

cnx = mysql.connector.connect(user='team103', password='gatech123',
                             host='127.0.0.1',
                              database='CS6400_spr22_team103')

import pandas as pd

# creates a Tk() object
master = Tk()
master.title("GameSwap")
master.resizable(width=False, height=False)
#clickvalue=''
# sets the geometry of main
# root window
master.geometry("500x500")


def logout():
    master.destroy()
label_title = Label(master,text="GameSwap")
label_title.place(width=100,height=35,x=50,y=50)
label_title.config(font=("Courier", 15,'bold'))
label_underline = Label(master,text="----------------------------------------------------------------------------------------------------------------")
label_underline.place(width=400,height=50,x=50,y=85)
label_underline.config(font=("Courier", 5,'bold'))

logout_button = Button(master,
             text="Logout", bg='blue',fg='white', borderless=1,command=logout)
logout_button.place(x=400,y=30)
print(global_variables.email_text)
login_fetch_query="Select concat(user_firstname, ',' , user_lastname) name,user_rating,unrated_swaps,unaccepted_swaps  from  CS6400_spr22_team103.user where email=  " + "'" + global_variables.email_text+ "'"
user_data = []
user_data = pd.read_sql_query(login_fetch_query, cnx)
print(str(user_data['name']))
def myitems():
    os.system('MyItems.py')
    #import MyItems
def acceptorrejectswaps():
    if int(user_data['unaccepted_swaps'][0]) > 0:
        os.system('GameSwapIntail.py')

def propose_swaps():
    os.system('propose_swap.py')

def unrated_swaps():
    if int(user_data['unrated_swaps'][0]) > 0:
        os.system('propose_swap.py')
        

label_logged_user = Label(master,text="Welcome " + str(user_data['name'][0]))
label_logged_user.place(width=300,height=35,x=50,y=125)
label_logged_user.config(font=("Times Roman", 10,'bold'))
myrating_text=StringVar()
myrating_text.set("My Rating-"+str(user_data['user_rating'][0]))
myrating_button = Button(master,
             text=myrating_text.get(), bg='white',fg='blue', borderless=1,height=50,width=150)
myrating_button.place(x=50,y=150)
listitem_button = Button(master,
             text="List Item", bg='blue',fg='white', borderless=1,height=50,width=150)
listitem_button.place(x=210,y=150)
unacceptedswaps_text=StringVar()
unacceptedswaps_text.set("Unaccepted Swaps-"+str(user_data['unaccepted_swaps'][0]))
unacceptedswaps_button = Button(master,
             text=unacceptedswaps_text.get(), bg='white',fg='blue', borderless=1,height=50,width=150,command=acceptorrejectswaps)
unacceptedswaps_button.place(x=50,y=200)
myitems_button = Button(master,text="My Item", bg='blue',fg='white', borderless=1,height=50,width=150,command=myitems)
myitems_button.place(x=210,y=200)
unratedswaps_text=StringVar()
unratedswaps_text.set("Unrated Swaps-"+str(user_data['unrated_swaps'][0]))
unacceptedswaps_button = Button(master,
             text=unratedswaps_text.get(), bg='white',fg='blue', borderless=1,height=50,width=150)
unacceptedswaps_button.place(x=50,y=250)


searchitems_button = Button(master,
             text="Search Items", bg='blue',fg='white', borderless=1,height=50,width=150)
searchitems_button.place(x=210,y=250)
swaphistory_button = Button(master,
             text="Swap History", bg='blue',fg='white', borderless=1,height=50,width=150,command=acceptorrejectswaps)
swaphistory_button.place(x=210,y=300)
updatemyinfo_button = Button(master,
             text="Update my info", bg='blue',fg='white', borderless=1,height=50,width=150)
updatemyinfo_button.place(x=210,y=350)


mainloop()