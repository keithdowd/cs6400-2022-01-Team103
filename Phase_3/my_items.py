from global_variables import *
from sql import sql__my_items__count_of_item_type
from sql import sql__my_items__list_of_all_items
from view_item import view_item

def my_items():
  ##############################
  # CONFIGURATION
  ##############################

  # Window
  WINDOW_TITLE = 'My Items'

  # Tables
  TABLE_COLUMN_ANCHOR = tk.W
  TABLE_COLUMN_STRETCH = tk.NO

  # Item counts
  item_counts = {
    'Board Games': 0,
    'Card Games': 0,
    'Computer Games': 0,
    'Jigsaw Puzzles': 0,
    'Video Games': 0,
    'Total': 0
  }

  # My items
  my_items_columns = [
    'Item #',
    'Game Type',
    'Title',
    'Condition',
    'Description',
  ]

  my_items_data = []


  ##############################
  # SETUP
  ##############################

  def setup(title='My Window', width=800, height=400):
    window = tk.Tk()
    window.title(title)
    window.geometry(f'{width}x{height}')
    return window

  window = setup(title=WINDOW_TITLE, width=WINDOW_SIZE_WIDTH, height=WINDOW_SIZE_HEIGHT)


  ##############################
  # ITEM COUNTS
  ##############################

  ########## DATA
  df = pd.read_sql_query(sql__my_items__count_of_item_type, cnx)

  board_games_cnt = 0 if df[df['itemtype_name'] == 'Board Game'].empty else df[df['itemtype_name'] == 'Board Game']['count'].reset_index(drop=True)[0]
  card_games_cnt = 0 if df[df['itemtype_name'] == 'Card Game'].empty else df[df['itemtype_name'] == 'Card Game']['count'].reset_index(drop=True)[0]
  computer_games_cnt = 0 if df[df['itemtype_name'] == 'Computer Game'].empty else df[df['itemtype_name'] == 'Computer Game']['count'].reset_index(drop=True)[0]
  jigsaw_puzzles_cnt = 0 if df[df['itemtype_name'] == 'Jigsaw Puzzle'].empty else df[df['itemtype_name'] == 'Jigsaw Puzzle']['count'].reset_index(drop=True)[0]
  video_games_cnt = 0 if df[df['itemtype_name'] == 'Video Game'].empty else df[df['itemtype_name'] == 'Video Game']['count'].reset_index(drop=True)[0]
  total = board_games_cnt + card_games_cnt + computer_games_cnt + jigsaw_puzzles_cnt + video_games_cnt

  item_counts['Board Games'] = board_games_cnt
  item_counts['Card Games'] = card_games_cnt
  item_counts['Computer Games'] = computer_games_cnt
  item_counts['Jigsaw Puzzles'] = jigsaw_puzzles_cnt
  item_counts['Video Games'] = video_games_cnt
  item_counts['Total'] = total

  ########## VIEW

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
    table_item_counts.column(column, anchor=TABLE_COLUMN_ANCHOR, width=int(WINDOW_SIZE_WIDTH/len(table_item_counts['column']))-2)
    table_item_counts.heading(column, text=column, anchor=TABLE_COLUMN_ANCHOR)
  table_item_counts.insert(parent='', index='end', iid=0, text='', values=tuple(item_counts.values()))
  table_item_counts.pack()


  ##############################
  # MY ITEMS
  ##############################

  ########## DATA

  df = pd.read_sql_query(sql__my_items__list_of_all_items, cnx)

  for index, row in df.iterrows():
      item_number = row['itemNumber']
      item_type_name = row['itemtype_name']
      item_title = row['item_title']
      item_condition = row['item_condition']
      item_description = row['item_description']
      
      arr = [
          item_number,
          item_type_name,
          item_title,
          item_condition,
          item_description
      ]

      my_items_data.append(arr)

  ########## VIEW

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
    table_my_items.column(column, anchor=TABLE_COLUMN_ANCHOR, width=int(WINDOW_SIZE_WIDTH * 0.15))
    table_my_items.heading(column, text=column, anchor=TABLE_COLUMN_ANCHOR)
  for i, row in enumerate(my_items_data):
    table_my_items.insert(parent='', index='end', iid=i, text='', values=row)
    tk.Button(window, text="Details", command=lambda item_number=my_items_data[i][0]: view_item(item_number)).pack(side=tk.RIGHT)
  table_my_items.pack()


##############################
# EVENT LOOP
##############################
# window.mainloop()