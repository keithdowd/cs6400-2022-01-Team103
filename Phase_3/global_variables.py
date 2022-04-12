import pandas as pd
import mysql.connector
import tkinter as tk
from tkinter import ttk

##############################
# DATABASE
##############################

# Credentials
USER = 'team103'
PASSWORD = 'gatech123'
HOST = '127.0.0.1'
DATABASE = 'CS6400_spr22_team103'

# Connection string
cnx = mysql.connector.connect(
  user=USER, 
  password=PASSWORD,
  host=HOST,
  database=DATABASE)

##############################
# GLOBALS
##############################

global email_text