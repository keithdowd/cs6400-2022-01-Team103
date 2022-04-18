from global_variables import *
from sql import sql__view_items__item_details

def view_item(swapID):

  ##############################
  # CONFIGURATION
  ##############################

  # Window
  WINDOW_TITLE = 'Swap Details'

  ##############################
  # SETUP
  ##############################
  def setup(title='My Window', width=800, height=400):
    window = tk.Tk()
    window.title(title)
    window.geometry(f'{width}x{height}')
    return window

  window = setup(title=WINDOW_TITLE, width=WINDOW_SIZE_WIDTH, height=WINDOW_SIZE_HEIGHT)
  item_number = 10

  ##############################
  # VIEW ITEM
  ##############################

  ########## DATA
  df = pd.read_sql_query(sql__view_items__item_details(item_number), cnx)
#   proposed_item_text = pd.read_sql_query(sql__pull_itemname(proposed_item), cnx)
# desired_item_text = pd.read_sql_query(sql__pull_itemname(desired_item), cnx)
# counterparty_email_text = pd.read_sql_query(sql__accept_reject_get_user_name(counterparty_email),cnx)
# pd.read_sql_query(sql_swap_title(userEmail), cnx)

  print(swapID)
  itemNumber = df['itemNumber'].values[0]
  item_title = df['item_title'].values[0]
  itemtype_name = df['itemtype_name'].values[0]
  itemtype_platform = df['itemtype_platform'].values[0]
  itemtype_media = df['itemtype_media'].values[0]
  item_condition = df['item_condition'].values[0]

  ########## VIEW

  # Header
  label_item_counts = tk.Label(master=window, text='Swap Details                User Details', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_counts.grid(row=0, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  # Separator
  separator = ttk.Separator(window, orient='horizontal')
  separator.grid(row=1, columnspan=4, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='ew')

  # Left column
  frame_left = tk.Frame(master=window)
  frame_left.grid(row=2, column=0, sticky='nw')

  label_item_number = tk.Label(master=frame_left, text='Proposed', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_item_number.grid(row=0, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_item_number_value = tk.Label(master=frame_left, text=f'{itemNumber}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_number_value.grid(row=0, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_title = tk.Label(master=frame_left, text='Accepted/Rejected', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_title.grid(row=1, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_title_value = tk.Label(master=frame_left, text=f'{item_title}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_title_value.grid(row=1, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_game_type = tk.Label(master=frame_left, text='My role', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_game_type.grid(row=2, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_game_type_value = tk.Label(master=frame_left, text=f'{itemtype_name}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_game_type_value.grid(row=2, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_platform = tk.Label(master=frame_left, text='Rating left', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_platform.grid(row=3, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_platform_value = tk.Label(master=frame_left, text=f'{itemtype_platform}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_platform_value.grid(row=3, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')


  # Header
  label_item_countsRight = tk.Label(master=window, text='', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_countsRight.grid(row=0, column=2, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  # Separator
  separator = ttk.Separator(window, orient='horizontal')
  separator.grid(row=1, columnspan=10, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='ew')

#   Right column
  frame_right = tk.Frame(master=window)
  frame_right.grid(row=2, column=2, sticky='nw')

  label_item_number = tk.Label(master=frame_left, text='Nickname', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_item_number.grid(row=0, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_item_number_value = tk.Label(master=frame_left, text=f'{itemNumber}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_number_value.grid(row=0, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
   

  label_title = tk.Label(master=frame_left, text='Distance', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_title.grid(row=1, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_title_value = tk.Label(master=frame_left, text=f'{item_title}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_title_value.grid(row=1, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  

  label_game_type = tk.Label(master=frame_left, text='Name', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_game_type.grid(row=2, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_game_type_value = tk.Label(master=frame_left, text=f'{itemtype_name}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_game_type_value.grid(row=2, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  
  label_platform = tk.Label(master=frame_left, text='Email', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_platform.grid(row=3, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_platform_value = tk.Label(master=frame_left, text=f'{itemtype_platform}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_platform_value.grid(row=3, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_media = tk.Label(master=frame_left, text='Phone', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_media.grid(row=4, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_media_value = tk.Label(master=frame_left, text=f'{itemtype_media}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_media_value.grid(row=4, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')



  # Header
  label_item_countsRight = tk.Label(master=window, text='Proposed Item                Desired Item', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_countsRight.grid(row=6, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  # Separator
  separator = ttk.Separator(window, orient='horizontal')
  separator.grid(row=7, columnspan=4, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='ew')



  # Bottom Left column
  frame_left = tk.Frame(master=window)
  frame_left.grid(row=8, column=0, sticky='nw')

  label_item_number = tk.Label(master=frame_left, text='Item #', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_item_number.grid(row=0, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_item_number_value = tk.Label(master=frame_left, text=f'{itemNumber}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_number_value.grid(row=0, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_title = tk.Label(master=frame_left, text='Title', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_title.grid(row=1, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_title_value = tk.Label(master=frame_left, text=f'{item_title}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_title_value.grid(row=1, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_game_type = tk.Label(master=frame_left, text='Game Type', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_game_type.grid(row=2, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_game_type_value = tk.Label(master=frame_left, text=f'{itemtype_name}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_game_type_value.grid(row=2, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_condition = tk.Label(master=frame_left, text='Condition', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_condition.grid(row=5, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_condition_value = tk.Label(master=frame_left, text=f'{item_condition}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_condition_value.grid(row=4, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')


  label_media = tk.Label(master=frame_left, text='Description', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_media.grid(row=4, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_media_value = tk.Label(master=frame_left, text=f'{itemtype_media}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_media_value.grid(row=5, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')


#   Bottom Right column
  frame_right = tk.Frame(master=window)
  frame_right.grid(row=8, column=2, sticky='nw')

  label_item_number = tk.Label(master=frame_left, text='Item #', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_item_number.grid(row=0, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_item_number_value = tk.Label(master=frame_left, text=f'{itemNumber}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_number_value.grid(row=0, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
   

  label_title = tk.Label(master=frame_left, text='Title', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_title.grid(row=1, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_title_value = tk.Label(master=frame_left, text=f'{item_title}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_title_value.grid(row=1, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  

  label_game_type = tk.Label(master=frame_left, text='Game Type', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_game_type.grid(row=2, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_game_type_value = tk.Label(master=frame_left, text=f'{itemtype_name}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_game_type_value.grid(row=2, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')


  label_condition = tk.Label(master=frame_left, text='Condition', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_condition.grid(row=5, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_condition_value = tk.Label(master=frame_left, text=f'{item_condition}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_condition_value.grid(row=3, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  ##############################
  # EVENT LOOP
  ##############################
  # if __name__ == "__main__":
  #   window.mainloop()