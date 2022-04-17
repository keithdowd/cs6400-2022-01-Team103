from global_variables import *
from sql import sql__my_items__count_of_item_type
from sql import sql__my_items__list_of_all_items
from view_item import view_item

def my_items(emailAddr='usr001@gt.edu'):
  ##############################
  # CONFIGURATION
  ##############################

  # Window
  WINDOW_TITLE = 'My Items'


  ##############################
  # SETUP
  ##############################

  def setup(title='My Window', width=800, height=400):
    window = tk.Tk()
    window.title(title)
    window.geometry(f'{width}x{height}')
    return window

  window = setup(
    title=WINDOW_TITLE, 
    width=WINDOW_SIZE_WIDTH+50, 
    height=WINDOW_SIZE_HEIGHT)

  # Create scrollable window for my my items table
  container = ttk.Frame(window)

  canvas = tk.Canvas(
    container, 
    width=WINDOW_SIZE_WIDTH+50, 
    height=200)

  scrollbar = ttk.Scrollbar(
    container, 
    orient='vertical', 
    command=canvas.yview)
    
  scrollable_frame = ttk.Frame(canvas)

  scrollable_frame.bind(
    '<Configure>',
    lambda e: canvas.configure(
      scrollregion=canvas.bbox('all')
    )
  )

  canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
  canvas.configure(yscrollcommand=scrollbar.set)

  container.grid(row=7, column=0, columnspan=9, sticky='nesw')
  canvas.grid(row=0, column=0, sticky='nesw')
  scrollbar.grid(row=0, column=7, sticky='nse')


  ##############################
  # ITEM COUNTS
  ##############################

  ########## DATA
  
  # Item counts
  item_counts = {
    'Board Games': 0,
    'Card Games': 0,
    'Computer Games': 0,
    'Jigsaw Puzzles': 0,
    'Video Games': 0,
    'Total': 0
  }

  df = pd.read_sql_query(sql__my_items__count_of_item_type(emailAddr), cnx)

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
  label_item_counts = tk.Label(
    master=window, 
    text='Item Counts', 
    font=(
      LABEL_FONT_FAMILY,
      LABEL_FONT_SIZE,
      LABEL_FONT_WEIGHT_VALUE
  ))
  label_item_counts.grid(
    row=0, 
    column=0, 
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w')

  # Separator
  separator = ttk.Separator(
    master=window, 
    orient='horizontal')
  separator.grid(
    row=1, 
    columnspan=10, 
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='ew')

  # Table (Header)
  for col_index, item_column in enumerate(item_counts.keys()):
    table_item_counts_header = tk.Label(
      master=window, 
      text=item_column, 
      font=(
        LABEL_FONT_FAMILY,
        LABEL_FONT_SIZE,
        LABEL_FONT_WEIGHT_LABEL),
    width=15)
    table_item_counts_header.grid(
      row=2, 
      column=col_index, 
      padx=WINDOW_PADDING_X, 
      pady=WINDOW_PADDING_Y,
      sticky='ew')

  # Table (Values)
  for col_index, item_count in enumerate(item_counts.values()):
    table_item_counts_value = tk.Label(
      master=window, 
      text=item_count, 
      font=(
        LABEL_FONT_FAMILY,
        LABEL_FONT_SIZE,
        LABEL_FONT_WEIGHT_VALUE),
    width=15)
    table_item_counts_value.grid(
      row=3,
      column=col_index,
      padx=WINDOW_PADDING_X, 
      pady=WINDOW_PADDING_Y,
      sticky='ew')


  ##############################
  # MY ITEMS
  ##############################

  ########## DATA

  my_items_columns = [
    'Item #',
    'Game Type',
    'Title',
    'Condition',
    'Description',
  ]

  df = pd.read_sql_query(sql__my_items__list_of_all_items(emailAddr), cnx)

  my_items_data = []

  for index, row in df.iterrows():
      item_number = row['itemNumber']
      item_type_name = row['itemtype_name']
      item_title = row['item_title']
      item_condition = row['item_condition']
      item_description = row['item_description'][0:100] + '...' if len(row['item_description']) > 100 else row['item_description']
      
      arr = [
          item_number,
          item_type_name,
          item_title,
          item_condition,
          item_description
      ]

      my_items_data.append(arr)

  ########## VIEW

  # Empty row
  empty_row = tk.Label(master=window, text='\n')
  empty_row.grid(row=4, column=0)

  # Header
  label_my_items = tk.Label(
    master=window, 
    text='My Items', 
    font=(
      LABEL_FONT_FAMILY,
      LABEL_FONT_SIZE,
      LABEL_FONT_WEIGHT_VALUE)
  )
  label_my_items.grid(
    row=5, 
    column=0, 
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w')

  # Separator
  separator = ttk.Separator(
    master=window, 
    orient='horizontal')
  separator.grid(
    row=6, 
    columnspan=10, 
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='ew')

  if len(my_items_data) > 0: # Show table view if the user has at least one item
    # Table (Header)
    for col_index, item_column in enumerate(my_items_columns):
      table_my_items_header = tk.Label(
        master=scrollable_frame, 
        text=item_column, 
        font=(
          LABEL_FONT_FAMILY,
          LABEL_FONT_SIZE,
          LABEL_FONT_WEIGHT_LABEL
        ),
        width=18)
      table_my_items_header.grid(
        row=7, 
        column=col_index, 
        padx=WINDOW_PADDING_X, 
        pady=WINDOW_PADDING_Y,
        sticky='ew')

    # Table (Values)
    for row_index, my_item in enumerate(my_items_data):
      row_index += 8 # layout starts at row 8
      
      for col_index, my_item_value in enumerate(my_item):
        # center item number and left justify all other fields
        if col_index == 0:
          anchor = 'center'
        else:
          anchor = 'w'

        table_my_items_value = tk.Label(
          master=scrollable_frame, 
          text=my_item_value, 
          font=(
            LABEL_FONT_FAMILY,
            LABEL_FONT_SIZE,
            LABEL_FONT_WEIGHT_VALUE     
          ), 
          width=18,
          wraplength=125,
          anchor=anchor,
          justify='left')
        table_my_items_value.grid(
          row=row_index,
          column=col_index,
          padx=WINDOW_PADDING_X,
          pady=WINDOW_PADDING_Y,
          sticky='ne'
        )
      table_my_items_details_btn = tk.Button(
        master=scrollable_frame, 
        text='Details',
        font=(
          LABEL_FONT_FAMILY,
          LABEL_FONT_SIZE,
          LABEL_FONT_WEIGHT_VALUE,
        ),
        command=lambda item_number=my_item[0]: view_item(item_number)
      )
      table_my_items_details_btn.grid(
        row=row_index,
        column=col_index+1, # add button after (to the right of) the last my items column
        sticky='ew'
        ) 
    
  else: # Show a message instead of the items table if the user has no items
    label_my_items = tk.Label(
      master=scrollable_frame, 
      text='You have no items.', 
      font=(
        LABEL_FONT_FAMILY,
        LABEL_FONT_SIZE,
        LABEL_FONT_WEIGHT_VALUE
    ))
    label_my_items.grid(
      row=7, 
      column=0, 
      padx=WINDOW_PADDING_X, 
      pady=WINDOW_PADDING_Y, 
      sticky='w')


##############################
# EVENT LOOP
##############################
# window.mainloop()