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
# VIEW
##############################

# Buttons
BUTTON_FONT_FAMILY = 'Courier'
BUTTON_FONT_SIZE = 14
BUTTON_FONT_WEIGHT = 'bold'

# Labels
LABEL_FONT_FAMILY = 'Courier'
LABEL_FONT_SIZE = 10
LABEL_FONT_WEIGHT_LABEL = 'bold'
LABEL_FONT_WEIGHT_VALUE = 'normal'

# Windows
WINDOW_PADDING_X = 5
WINDOW_PADDING_X_OFFSET = 42
WINDOW_PADDING_Y = 5
WINDOW_SIZE_HEIGHT = 400
WINDOW_SIZE_WIDTH = 800

global email_text