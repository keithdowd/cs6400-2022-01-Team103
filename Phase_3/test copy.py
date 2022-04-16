import tkinter as tk
from tkinter import ttk, StringVar, OptionMenu, Button
from tkinter.font import BOLD
from global_variables import *
from sql import sql_get_my_unrated_swaps,sql_rate_my_unrated_swaps
import pandas as pd

cnx = mysql.connector.connect(user='team103', password='gatech123',
                            host='127.0.0.1',
                             database='CS6400_spr22_team103')


def rate_swaps(emailAddr, swapID, rating):
    mycursor = cnx.cursor()
    query=sql_rate_my_unrated_swaps(emailAddr, swapID, rating)
    print(query)
    mycursor.execute(query)
    cnx.commit()
    mycursor.close()

# get_unrated_swaps(userEmail='usr071@gt.edu')

rate_swaps('usr121@gt.edu', 258,3)

