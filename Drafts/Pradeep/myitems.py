import tkinter as tk
from tkinter import ttk

##############################
# CONFIGURATION
##############################

# Window
WINDOW_HEIGHT = 400
WINDOW_PADDING_X = 5
WINDOW_PADDING_Y = 5
WINDOW_TITLE = 'My Items'
WINDOW_WIDTH = 800

# Tables
TABLE_COLUMN_ANCHOR = tk.W
TABLE_COLUMN_STRETCH = tk.NO

# # Item counts
# item_counts = {
#     'Board Games': 0,
#     'Card Games': 0,
#     'Computer Games': 0,
#     'Jigsaw Puzzles': 0,
#     'Video games': 0,
#     'Total': 0
# }

# My items
items_columns = [
    'Item #',
    'Game Type',
    'Title',
    'Condition',
    'Description',
    'User',
    'Postal Code',
    'Swapper rating',
    'Distance(miles)'
    ''
]

items_data = [
    [
        23, 'Video game', 'Tetris', 'Lightly used', '', 'User1', '12345', '4.6', '354'
    ],
    [
        34, 'Board game', 'Monopoly', 'Damaged/Missing parts', '',  'User2', '35245', '4.9', '123'
    ],
    [
        106, 'Card game', 'UNO', 'Mint', 'Never opened!',  'User3', '53214', '4.2', '521'
    ]
]

##############################
# SETUP
##############################


def setup(title='My Window', width=800, height=400):
    window = tk.Tk()
    window.title(title)
    window.geometry(f'{width}x{height}')
    #window.time_var.set('...')
    #window._init_widgets()
    return window


window = setup(title=WINDOW_TITLE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)


# Header
label_item_counts = tk.Label(master=window, text='View Items')
label_item_counts.pack(padx=WINDOW_PADDING_X,
                       pady=WINDOW_PADDING_Y, anchor='w')

# Separator
separator = ttk.Separator(window, orient='horizontal')
separator.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, fill='x')

# Table
frame_items = tk.Frame(window)
frame_items.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, anchor='w')
table_items = ttk.Treeview(frame_items, height=len(items_data))
table_items['columns'] = items_columns
table_items.column('#0', width=0, stretch=TABLE_COLUMN_STRETCH)
table_items.heading('#0', text='')
for column in table_items['columns']:
    table_items.column(column, anchor=TABLE_COLUMN_ANCHOR,
                       width=int(WINDOW_WIDTH/len(table_items['column']))-2)
    table_items.heading(column, text=column, anchor=TABLE_COLUMN_ANCHOR)
for i, row in enumerate(items_data):
    table_items.insert(parent='', index='end', iid=i, text='', values=row)
table_items.pack()

##############################
# EVENT LOOP
##############################
window.mainloop()