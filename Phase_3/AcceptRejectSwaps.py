from global_variables import *
from sql import sql__view_items__item_details

def accept_reject_swaps(userEmail):

    
    ##############################
    # CONFIGURATION
    ##############################

    # Window
    WINDOW_TITLE = 'Accept or Reject Swaps'

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
  # Accept / Reject Swaps
  ##############################

  ########## DATA
    data_raw = {(1,'asd@dsa.com','123@dsa.com','11','21','1/1/2020'),
                (2,'asd@dsa.com','234@dsa.com','12','22','1/11/2020'),
                (3,'asd@dsa.com','345@dsa.com','13','23','1/21/2020'),
                (4,'asd@dsa.com','456@dsa.com','14','24','1/31/2020')
    }

    df=pd.DataFrame(data_raw,columns=['swapID','counterparty_email','proposer_email','counterparty_itemNumber','proposer_itemNumber','swap_date_proposed'])
    #query_list=df.values.tolist()

    # df = pd.read_sql_query(sql__view_items__item_details(userEmail), cnx)
    # query_list=df.values.tolist()

        
    # assign to new list
    swapID = []
    counterparty_email = []
    proposer_email = []
    counterparty_itemNumber = []
    proposer_itemNumber = []
    swap_date_proposed = []

    desired_item = []
    proposer_name = []
    proposer_location = []
    rating=[]
    distance=[]
    proposed_item=[]
    myLocation = 'tbd'

    swapID=df['swapID'].to_list()
    counterparty_email=df['counterparty_email'].to_list()
    proposer_email=df['proposer_email'].to_list()
    counterparty_itemNumber=df['counterparty_itemNumber'].to_list()
    proposer_itemNumber=df['proposer_itemNumber'].to_list()
    swap_date_proposed=df['swap_date_proposed'].to_list()

    # getting from other tables
    index=0
    for swapID_iter in swapID:
        desired_item[index] = pd.read_sql_query(sql__accept_reject_get_item_name(counterparty_itemNumber),cnx)
        proposed_item[index] = pd.read_sql_quer(sql__accept_reject_get_item_name(proposer_itemNumber),cnx)
        proposer_name[index] = pd.read_sql_quer(sql__accept_reject_get_item_name(proposer_itemNumber),cnx)
        rating[index] = pd.read_sql_quer(sql__accept_reject_get_item_name(proposer_itemNumber),cnx)
        
        # need formula or location
        distance[index] = 1*myLocation*proposer_location[index]
        
        
        index+=1

    #
    # VIEW
    #

    frame_left = tk.Frame(master=window)
    frame_left.grid(row=0, column=0, sticky='nw')

    label_date = tk.Label(master=frame_left, text='Date', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_date.grid(row=0, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
    label_desiredItem = tk.Label(master=frame_left, text='Desired Item', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_desiredItem.grid(row=0, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
    label_proposer = tk.Label(master=frame_left, text='Proposer', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_proposer.grid(row=0, column=2, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
    label_rating = tk.Label(master=frame_left, text='Rating', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_rating.grid(row=0, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
    label_dist = tk.Label(master=frame_left, text='Distance', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_dist.grid(row=0, column=4, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
    label_proposedItem = tk.Label(master=frame_left, text='Proposed Item', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_proposedItem.grid(row=0, column=6, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
    label_acceptorreject = tk.Label(master=frame_left, text='', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
    label_acceptorreject.grid(row=0, column=6, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')


    index=0
    for swapID_iter in swapID:
        label_date = tk.Label(master=frame_left, text=swap_date_proposed[index], font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        label_date.grid(row=index+1, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        label_desiredItem = tk.Label(master=frame_left, text=swap_date_proposed[index], font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        label_desiredItem.grid(row=index+1, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        label_proposer = tk.Label(master=frame_left, text=swap_date_proposed[index], font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        label_proposer.grid(row=index+1, column=2, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        label_rating = tk.Label(master=frame_left, text=swap_date_proposed[index], font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        label_rating.grid(row=index+1, column=3, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        label_dist = tk.Label(master=frame_left, text=swap_date_proposed[index], font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        label_dist.grid(row=index+1, column=4, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        label_proposedItem = tk.Label(master=frame_left, text=swap_date_proposed[index], font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        label_proposedItem.grid(row=index+1, column=6, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        label_acceptorreject = tk.Label(master=frame_left, text=swap_date_proposed[index], font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        label_acceptorreject.grid(row=index+1, column=6, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

        index+=1


    # swapID = df['swapID'].values[0]
    # counterparty_email = df['item_title'].values[0]
    # proposer_email = df['itemtype_name'].values[0]
    # counterparty_itemNumber = df['itemtype_platform'].values[0]
    # proposer_itemNumber = df['itemtype_media'].values[0]
    # swap_date_proposed = df['item_condition'].values[0]

  ########## VIEW

  # Header
#     label_item_counts = tk.Label(master=window, text='Item Details', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
#     label_item_counts.grid(row=0, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

#   # Separator
#     separator = ttk.Separator(window, orient='horizontal')
#     separator.grid(row=1, columnspan=4, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='ew')

#   # Left column
#     frame_left = tk.Frame(master=window)
#     frame_left.grid(row=2, column=0, sticky='nw')

#     label_item_number = tk.Label(master=frame_left, text='Item #', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
#     label_item_number.grid(row=0, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
#     label_item_number_value = tk.Label(master=frame_left, text=f'{swapID}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
#     label_item_number_value.grid(row=0, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

#     label_title = tk.Label(master=frame_left, text='Title', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
#     label_title.grid(row=1, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
#     label_title_value = tk.Label(master=frame_left, text=f'{item_title}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
#     label_title_value.grid(row=1, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

#     label_game_type = tk.Label(master=frame_left, text='Game Type', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
#     label_game_type.grid(row=2, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
#     label_game_type_value = tk.Label(master=frame_left, text=f'{itemtype_name}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
#     label_game_type_value.grid(row=2, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

#     label_platform = tk.Label(master=frame_left, text='Platform', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
#     label_platform.grid(row=3, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
#     label_platform_value = tk.Label(master=frame_left, text=f'{itemtype_platform}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
#     label_platform_value.grid(row=3, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

#     label_media = tk.Label(master=frame_left, text='Media', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
#     label_media.grid(row=4, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
#     label_media_value = tk.Label(master=frame_left, text=f'{itemtype_media}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
#     label_media_value.grid(row=4, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

#     label_condition = tk.Label(master=frame_left, text='Condition', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
#     label_condition.grid(row=5, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
#     label_condition_value = tk.Label(master=frame_left, text=f'{item_condition}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
#     label_condition_value.grid(row=5, column=1, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')

  # Right column
  # frame_right = tk.Frame(master=window)
  # frame_right.grid(row=2, column=1, sticky='nw')

  # label_offered_by = tk.Label(master=frame_right, text='Offered by', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  # label_offered_by.grid(row=0, column=0, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')
  # label_offered_by_value = tk.Label(master=frame_right, text=f'{OFFERED_BY}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  # label_offered_by_value.grid(row=0, column=1, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')

  # label_location = tk.Label(master=frame_right, text='Location', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  # label_location.grid(row=1, column=0, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')
  # label_location_value = tk.Label(master=frame_right, text=f'{LOCATION}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  # label_location_value.grid(row=1, column=1, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')

  # label_rating = tk.Label(master=frame_right, text='Rating', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
  # label_rating.grid(row=2, column=0, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')
  # label_rating_value = tk.Label(master=frame_right, text=f'{RATING}', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE))
  # label_rating_value.grid(row=2, column=1, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')

  # label_distance = tk.Label(master=frame_right, text='Distance', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL), bg='red')
  # label_distance.grid(row=3, column=0, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')
  # label_distance_value = tk.Label(master=frame_right, text=f'{DISTANCE} miles', font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_VALUE), bg='red')
  # label_distance_value.grid(row=3, column=1, padx=WINDOW_PADDING_X+WINDOW_PADDING_X_OFFSET, pady=WINDOW_PADDING_Y, sticky='w')

  # button_propose_swap = tk.Button(master=frame_right, text='Propose Swap', height=2, font=(BUTTON_FONT_FAMILY, BUTTON_FONT_SIZE, BUTTON_FONT_WEIGHT), fg='white', bg='blue')
  # button_propose_swap.grid(row=4, columnspan=2, pady=25)
    window.mainloop()
##############################
# EVENT LOOP
##############################
if __name__ == "__main__":
    accept_reject_swaps('asd@dsa.com')
    
    #window.mainloop()