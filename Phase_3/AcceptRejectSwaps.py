from global_variables import *
from sql import *

def accept_swap(index):
    print('accept swap: index :'+str(index))
    #TBD : Create queries to insert
def reject_swap(index):
    print('reject swap: index :'+str(index))
    #TBD : Create queries to insert


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
        proposed_item[index] = pd.read_sql_query(sql__accept_reject_get_item_name(proposer_itemNumber),cnx)
        proposer_name[index] = pd.read_sql_query(sql__accept_reject_get_user_name(proposer_email),cnx)
        rating[index] = pd.read_sql_query(sql__accept_reject_get_user_rating(proposer_email),cnx)
    
        # TODO: need formula here
        # need formula or location
        # distance[index] = 1*myLocation*proposer_location[index]
        
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
    
    index_num=0
    index=0
    for i,swapID_iter in enumerate(swapID):
        label_date = tk.Label(master=frame_left, text=swap_date_proposed[index], font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        label_date.grid(row=index+1, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        label_desiredItem = tk.Label(master=frame_left, text=desired_item[index], font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        label_desiredItem.grid(row=index+1, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        label_proposer = tk.Label(master=frame_left, text=proposer_name[index], font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        label_proposer.grid(row=index+1, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        label_rating = tk.Label(master=frame_left, text=rating[index], font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        label_rating.grid(row=index+1, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        label_dist = tk.Label(master=frame_left, text=distance[index], font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        label_dist.grid(row=index+1, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        label_proposedItem = tk.Label(master=frame_left, text=proposed_item[index], font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        label_proposedItem.grid(row=index+1, column=0, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        
        btn_accept = tk.Button(master=frame_left, text='Accept',command=lambda index_num=i:accept_swap(index_num), font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        btn_accept.grid(row=i+1, column=7, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        btn_reject = tk.Button(master=frame_left, text='Reject',command=lambda index_num=i:accept_swap(index_num), font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        btn_reject.grid(row=i+1, column=8, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        index+=1

    window.mainloop()


##############################
# MAIN
##############################
if __name__ == "__main__":
    accept_reject_swaps('asd@dsa.com')
    
    #window.mainloop()