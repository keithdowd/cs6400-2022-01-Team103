import tkinter as tk
from tkinter import *
import mysql.connector

# cnx = mysql.connector.connect(user='team103', password='gatech123',
#                              host='127.0.0.1',
#                               database='CS6400_spr22_team103')

label_width=242
label_height=35
table_width=14
font_name='Courier'
font_size=10
font_color='blue'

class SwapTable():
    
    def __init__(self,root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=table_width, fg=font_color,font=(font_name,font_size))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
    
# data for table, first row are titles:
lst = [('Date','Desired Item','Proposer','Rating','Distance','Proposed Item',' '),
('1/15/2020','Cards Against Humanity','HeroOfTime','4.99','8.2 miles','Super Mario Maker','TBD')]

total_rows = len(lst)
total_columns = len(lst[0])

# create GUI window:
root = Tk()
root.title("Accept/reject swaps")
root.resizable(width=True,height=True)
root.geometry("800x700")

t = SwapTable(root)
# label = Label(root,text="Accept/reject swaps")
root.mainloop()
