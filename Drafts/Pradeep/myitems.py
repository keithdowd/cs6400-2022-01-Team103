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

# Item counts
item_counts = {
  'Board Games': 0,
  'Card Games': 0,
  'Computer Games': 0,
  'Jigsaw Puzzles': 0,
  'Video games': 0,
  'Total': 0
}

# My items
my_items_columns = [
  'Item #',
  'Game Type',
  'Title',
  'Condition',
  'Description',
  ''
]

my_items_data = [
  [
    23, 'Video game', 'Tetris', 'Lightly used', '', 'Detail'
  ],
  [
    34, 'Board game', 'Monopoly', 'Damaged/Missing parts', 'We used to play this game heavily, and started losing some of the figurines, the cards, and finally...', 'Detail'
  ],
  [
    106, 'Card game', 'UNO', 'Mint', 'Never opened!', 'Detail'
  ]
]

##############################
# SETUP
##############################
def setup(title='My Window', width=800, height=400):
  window = tk.Tk()
  window.title(title)
  window.geometry(f'{width}x{height}')
  return window

window = setup(title=WINDOW_TITLE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

##############################
# ITEM COUNTS
##############################
# Header
label_item_counts = tk.Label(master=window, text='Item Counts')
label_item_counts.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, anchor='w')

# Separator
separator = ttk.Separator(window, orient='horizontal')
separator.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, fill='x')

# Table
frame_item_counts = tk.Frame(window)
frame_item_counts.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, anchor='w')
table_item_counts = ttk.Treeview(frame_item_counts, height=1)
table_item_counts['columns'] = tuple(item_counts.keys())
table_item_counts.column('#0', width=0, stretch=TABLE_COLUMN_STRETCH)
table_item_counts.heading('#0', text='')
for column in table_item_counts['columns']:
  table_item_counts.column(column, anchor=TABLE_COLUMN_ANCHOR, width=int(WINDOW_WIDTH/len(table_item_counts['column']))-2)
  table_item_counts.heading(column, text=column, anchor=TABLE_COLUMN_ANCHOR)
table_item_counts.insert(parent='', index='end', iid=0, text='', values=tuple(item_counts.values()))
table_item_counts.pack()

##############################
# MY ITEMS
##############################

# Header
label_item_counts = tk.Label(master=window, text='My Items')
label_item_counts.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, anchor='w')

# Separator
separator = ttk.Separator(window, orient='horizontal')
separator.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, fill='x')

# Table
frame_my_items = tk.Frame(window)
frame_my_items.pack(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, anchor='w')
table_my_items = ttk.Treeview(frame_my_items, height=len(my_items_data))
table_my_items ['columns'] = my_items_columns
table_my_items.column('#0', width=0, stretch=TABLE_COLUMN_STRETCH)
table_my_items.heading('#0', text='')
for column in table_my_items['columns']:
  table_my_items.column(column, anchor=TABLE_COLUMN_ANCHOR, width=int(WINDOW_WIDTH/len(table_my_items['column']))-2)
  table_my_items.heading(column, text=column, anchor=TABLE_COLUMN_ANCHOR)
for i, row in enumerate(my_items_data):
  table_my_items.insert(parent='', index='end', iid=i, text='', values=row)
table_my_items.pack()

##############################
# EVENT LOOP
##############################
window.mainloop()