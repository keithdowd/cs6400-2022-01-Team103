from global_variables import *
from haversine import haversine
from propose_swap_confirm import propose_swap_confirm
from sql import sql__propose_swap__item_details
from sql import sql__myrating__fetch
from sql import sql_get_my_unrated_swaps
from sql import sql__unacceptedswaps__fetch

def propose_swap(emailAddr, item_number):

  ##############################
  # CONFIGURATION
  ##############################

  # Window
  WINDOW_TITLE = 'Propose Swap'

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
  # VIEW ITEM
  ##############################

  ########## DATA

  def propose_swap_confirm_exec():
    propose_swap_confirm(emailAddr, item_title, distance)
    window.destroy()

  df = pd.read_sql_query(sql__propose_swap__item_details(emailAddr, item_number), cnx)

  itemNumber = df['itemNumber'].values[0]
  item_title = df['item_title'].values[0]
  itemtype_name = df['itemtype_name'].values[0]
  itemtype_platform = df['itemtype_platform'].values[0]
  itemtype_media = df['itemtype_media'].values[0]
  item_condition = df['item_condition'].values[0]
  item_description = df['item_description'].values[0]
  itemtype_piece_count = df['itemtype_piece_count'].values[0]
  offered_by = df['offered_by'].values[0]
  offered_by_email = df['offered_by_email'].values[0]
  location = df['location'].values[0]
  other_rating = pd.read_sql_query(sql__myrating__fetch(offered_by_email), cnx)
  other_rating = 'None' if other_rating is None else other_rating['user_rating'].values[0]  
  other_addr_lat = float(df['other_addr_lat'])
  other_addr_lon = float(df['other_addr_lon'])
  user_addr_lat = float(df['user_addr_lat'])
  user_addr_lon = float(df['user_addr_lon'])
  distance = round(haversine(user_addr_lat, other_addr_lat, user_addr_lon, other_addr_lon), 1)

  def get_distance_bgcolor(distance):
    if distance <= 25.0:
      return 'green'
    elif distance > 25.0 and distance <= 50.0:
      return 'yellow'
    elif distance > 50.0 and distance <= 100.0:
      return 'orange'
    else:
      return 'red'

  distance_bgcolor = get_distance_bgcolor(distance)

  df_unrated_swaps = pd.read_sql_query(sql_get_my_unrated_swaps(emailAddr), cnx)
  count_unrated_swaps = df_unrated_swaps.shape[0]
  
  df_unaccepted_swaps = pd.read_sql_query(sql__unacceptedswaps__fetch(emailAddr), cnx)
  count_unaccepted_swaps = df_unaccepted_swaps.shape[0]

  ########## VIEW

  # Header
  label_item_counts = tk.Label(master=window, text='Item Details', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_counts.grid(row=0, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  # Separator
  separator = ttk.Separator(window, orient='horizontal')
  separator.grid(row=1, columnspan=4, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='ew')

  # Left column
  frame_left = tk.Frame(master=window)
  frame_left.grid(row=2, column=0, sticky='nw')

  label_item_number = tk.Label(master=frame_left, text='Item #', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_item_number.grid(row=0, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_item_number_value = tk.Label(master=frame_left, text=f'{itemNumber}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_number_value.grid(row=0, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_title = tk.Label(master=frame_left, text='Title', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_title.grid(row=1, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_title_value = tk.Label(master=frame_left, text=f'{item_title}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_title_value.grid(row=1, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  if itemtype_name:
    label_game_type = tk.Label(master=frame_left, text='Game Type', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_game_type.grid(row=2, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
    label_game_type_value = tk.Label(master=frame_left, text=f'{itemtype_name}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
    label_game_type_value.grid(row=2, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  if itemtype_platform:
    label_platform = tk.Label(master=frame_left, text='Platform', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_platform.grid(row=3, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
    label_platform_value = tk.Label(master=frame_left, text=f'{itemtype_platform}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
    label_platform_value.grid(row=3, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  if itemtype_media:
    label_media = tk.Label(master=frame_left, text='Media', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_media.grid(row=4, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
    label_media_value = tk.Label(master=frame_left, text=f'{itemtype_media}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
    label_media_value.grid(row=4, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  if item_condition:
    label_condition = tk.Label(master=frame_left, text='Condition', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_condition.grid(row=5, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
    label_condition_value = tk.Label(master=frame_left, text=f'{item_condition}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
    label_condition_value.grid(row=5, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  
  if item_description:
    label_description = tk.Label(master=frame_left, text='Description', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_description.grid(row=6, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
    label_description_value = tk.Label(master=frame_left, text=f'{item_description}', wraplength=125, justify='left', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
    label_description_value.grid(row=6, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  
  if itemtype_piece_count:
    label_piece_count = tk.Label(master=frame_left, text='Piece Count', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_piece_count.grid(row=7, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
    label_piece_count_value = tk.Label(master=frame_left, text=f'{itemtype_piece_count}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
    label_piece_count_value.grid(row=7, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  # Right column
  frame_right = tk.Frame(master=window)
  frame_right.grid(row=2, column=1, sticky='nw')

  label_offered_by = tk.Label(master=frame_right, text='Offered by', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_offered_by.grid(row=0, column=0, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')
  label_offered_by_value = tk.Label(master=frame_right, text=f'{offered_by}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_offered_by_value.grid(row=0, column=1, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')

  label_location = tk.Label(master=frame_right, text='Location', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_location.grid(row=1, column=0, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')
  label_location_value = tk.Label(master=frame_right, text=f'{location}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_location_value.grid(row=1, column=1, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')

  label_rating = tk.Label(master=frame_right, text='Rating', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_rating.grid(row=2, column=0, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')
  label_rating_value = tk.Label(master=frame_right, text=f'{other_rating}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_rating_value.grid(row=2, column=1, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')

  if distance > 0:
    label_distance = tk.Label(master=frame_right, text='Distance', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL), bg=distance_bgcolor)
    label_distance.grid(row=3, column=0, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')
    label_distance_value = tk.Label(master=frame_right, text=f'{distance} miles', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE), bg=distance_bgcolor)
    label_distance_value.grid(row=3, column=1, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')

  if count_unrated_swaps <= 2 and count_unaccepted_swaps <= 5:
    button_propose_swap = tk.Button(master=frame_right, text='Propose Swap', command=propose_swap_confirm_exec, height=2, font=(BUTTON_FONT_FAMILY, BUTTON_FONT_SIZE, BUTTON_FONT_WEIGHT), fg='white', bg='blue')
    button_propose_swap.grid(row=4, columnspan=2, pady=25)

  ##############################
  # EVENT LOOP
  ##############################
  # if __name__ == "__main__":
  #   window.mainloop()