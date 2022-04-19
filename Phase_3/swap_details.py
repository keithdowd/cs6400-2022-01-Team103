from global_variables import *
from sql import *
from haversine import haversine

def view_item(swapID, userEmail):

  ##############################
  # CONFIGURATION
  ##############################

  # Window
  WINDOW_TITLE = 'Swap Details'

  ##############################
  # SETUP
  ##############################
  def setup(title='My Window', width=800, height=WINDOW_SIZE_HEIGHT):
    window = tk.Tk()
    window.title(title)
    window.geometry(f'{width}x{height}')
    return window

  def window_destroy():
      window.destroy()
  window = setup(title=WINDOW_TITLE, width=1000, height=1000)
  window.resizable(width=False, height=False)
  item_number = 10

  ##############################
  # VIEW ITEM
  ##############################

  ########## DATA
  df = pd.read_sql_query(sql__swap_history_detail(swapID, userEmail), cnx)
  pf = pd.read_sql_query(sql__myrating__fetch(userEmail), cnx)
  df_number = pd.read_sql_query(sql__swap_history_detail(swapID, userEmail), cnx)
  swap_proposed_text = df['swap_date_proposed'][0]
  accepted_rejected_text = df['Accepted_Rejected_Date'][0]
  status_text = df['myrole'][0]
  rating_left_text = pf['user_rating'][0]
  print((df['addr_latitude']))
  print((df['addr_longitude']))
  user_detail_nickname_text = df['other_user'][0]
  distance_text = "lkio"
  user_detail_name_text = df['other_user_name'][0]
  user_detail_email_text = df['other_user_email'][0]
  user_detail_phone_text = df['other_user_phone_number'][0]

  proposed_item_number_text = df['p_item_no'][0]
  proposed_item_title_text = df['ProposedItem'][0]
  proposed_item_type_text = df['c_item_type'][0]
  proposed_item_cond_text = df['p_item_cond'][0]
  proposed_item_des_text = df['p_item_desc'][0]


  desired_item_number_text = df['c_item_no'][0]
  desired_item_title_text = df['DesiredItem'][0]
  desired_item_type_text = df['c_item_type'][0]
  desired_item_type_cond_text = df['c_item_cond'][0]


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

  label_proposed_date = tk.Label(master=frame_left, text='Proposed', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_proposed_date.grid(row=0, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_proposed_date_value = tk.Label(master=frame_left, text=f'{swap_proposed_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_proposed_date_value.grid(row=0, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_accepted_date = tk.Label(master=frame_left, text='Accepted/Rejected', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_accepted_date.grid(row=1, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_accepted_date_value = tk.Label(master=frame_left, text=f'{accepted_rejected_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_accepted_date_value.grid(row=1, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_role = tk.Label(master=frame_left, text='My role', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_role.grid(row=2, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_role_value = tk.Label(master=frame_left, text=f'{status_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_role_value.grid(row=2, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_rating_left = tk.Label(master=frame_left, text='Rating left', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_rating_left.grid(row=3, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_rating_left_value = tk.Label(master=frame_left, text=f'{rating_left_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_rating_left_value.grid(row=3, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')


  # Header
  label_item_countsRight = tk.Label(master=window, text='', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_countsRight.grid(row=0, column=2, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  # Separator
  separator = ttk.Separator(window, orient='horizontal')
  separator.grid(row=1, columnspan=10, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='ew')

#   Right column
  frame_right = tk.Frame(master=window)
  frame_right.grid(row=2, column=2, sticky='nw')

  label_nickname = tk.Label(master=frame_left, text='Nickname', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_nickname.grid(row=0, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_nickname_value = tk.Label(master=frame_left, text=f'{user_detail_nickname_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_nickname_value.grid(row=0, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
   

  label_distance = tk.Label(master=frame_left, text='Distance', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_distance.grid(row=1, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_distance_value = tk.Label(master=frame_left, text=f'{distance_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_distance_value.grid(row=1, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  

  label_name_label = tk.Label(master=frame_left, text='Name', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_name_label.grid(row=2, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_name_label_value = tk.Label(master=frame_left, text=f'{user_detail_name_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_name_label_value.grid(row=2, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  
  label_email_text = tk.Label(master=frame_left, text='Email', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_email_text.grid(row=3, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_email_text_value = tk.Label(master=frame_left, text=f'{user_detail_email_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_email_text_value.grid(row=3, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_phone_text = tk.Label(master=frame_left, text='Phone', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_phone_text.grid(row=4, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_phone_text_value = tk.Label(master=frame_left, text=f'{user_detail_phone_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_phone_text_value.grid(row=4, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')



  # Header
  label_item_countsRight = tk.Label(master=window, text='Proposed Item                Desired Item', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_countsRight.grid(row=6, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  # Separator
  separator = ttk.Separator(window, orient='horizontal')
  separator.grid(row=7, columnspan=4, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='ew')



  # Bottom Left column
  frame_left = tk.Frame(master=window)
  frame_left.grid(row=8, column=0, sticky='nw')

  label_item_number_proposed = tk.Label(master=frame_left, text='Item #', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_item_number_proposed.grid(row=0, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_item_number_proposed_value = tk.Label(master=frame_left, text=f'{proposed_item_number_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_number_proposed_value.grid(row=0, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_item_number_proposed_title = tk.Label(master=frame_left, text='Title', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_item_number_proposed_title.grid(row=1, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_item_number_proposed_title_value = tk.Label(master=frame_left, text=f'{proposed_item_title_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_number_proposed_title_value.grid(row=1, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_item_game_type = tk.Label(master=frame_left, text='Game Type', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_item_game_type.grid(row=2, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_item_game_type_value = tk.Label(master=frame_left, text=f'{proposed_item_type_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_game_type_value.grid(row=2, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  label_condition = tk.Label(master=frame_left, text='Condition', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_condition.grid(row=5, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_condition_value = tk.Label(master=frame_left, text=f'{proposed_item_cond_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_condition_value.grid(row=4, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')


  label_title_des = tk.Label(master=frame_left, text='Description', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_title_des.grid(row=4, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_title_des_value = tk.Label(master=frame_left, text=f'{proposed_item_des_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_title_des_value.grid(row=5, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')


#   Bottom Right column
  frame_right = tk.Frame(master=window)
  frame_right.grid(row=8, column=2, sticky='nw')

  label_item_number_desired= tk.Label(master=frame_left, text='Item #', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_item_number_desired.grid(row=0, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_item_number_desired_value = tk.Label(master=frame_left, text=f'{desired_item_number_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_item_number_desired_value.grid(row=0, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
   

  label_title = tk.Label(master=frame_left, text='Title', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_title.grid(row=1, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_title_value = tk.Label(master=frame_left, text=f'{desired_item_title_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_title_value.grid(row=1, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  

  label_game_type = tk.Label(master=frame_left, text='Game Type', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_game_type.grid(row=2, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_game_type_value = tk.Label(master=frame_left, text=f'{desired_item_type_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_game_type_value.grid(row=2, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')


  label_condition = tk.Label(master=frame_left, text='Condition', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  label_condition.grid(row=5, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
  label_condition_value = tk.Label(master=frame_left, text=f'{desired_item_type_cond_text}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  label_condition_value.grid(row=3, column=5, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  ##############################
  # EVENT LOOP
  ##############################
  # if __name__ == "__main__":
  table_close_btn = tk.Button(master=window, text='Close', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE), command=window_destroy)
  table_close_btn.place(x=500,y=500)
  window.mainloop()

# view_item(1, 'usr001@gt.edu')