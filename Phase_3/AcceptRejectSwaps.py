from global_variables import *
from sql import *
import math

def accept_reject_swaps(userEmail):    

    def accept_swap(swapID,date):
        # print('accept swap: index :'+str(index))
        #TBD : Create queries to insert
        pd.read_sql_query(sql__respond_swap(swapID,date,"Accepted"), cnx)

    def reject_swap(swapID,date):
        # print('reject swap: index :'+str(index))
        #TBD : Create queries to insert
        pd.read_sql_query(sql__respond_swap(swapID,date,"Rejected"), cnx)

    def haversine(lat1, lat2,long1,long2):
        R = 6371*1000
        lat1_conv = lat1*math.pi/180
        lat2_conv = lat2*math.pi/180
        chg_lat = (lat2-lat1)*math.pi/180
        chg_long = (long2-long1)*math.pi/180
        a=math.sin(chg_lat/2)*math.sin(chg_lat/2)+math.cos(lat1_conv)*math.cos(lat2_conv)*math.sin(chg_long/2)*math.sin(chg_long/2)
        c = (2 * (math.atan2(math.sqrt(a), math.sqrt(1-a))))
        d = (R * c) / 1000    # kilometers
        return d

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
    # for testing purposes:
    # data_raw = {(1,'asd@dsa.com','123@dsa.com','11','21','1/1/2020'),
    #             (2,'asd@dsa.com','234@dsa.com','12','22','1/11/2020'),
    #             (3,'asd@dsa.com','345@dsa.com','13','23','1/21/2020'),
    #             (4,'asd@dsa.com','456@dsa.com','14','24','1/31/2020')
    # }

    data_raw = pd.read_sql_query(sql__view_items__item_details(userEmail), cnx)
    df=pd.DataFrame(data_raw,columns=['swapID','counterparty_email','proposer_email','counterparty_itemNumber','proposer_itemNumber','swap_date_proposed'])
    #query_list=df.values.tolist()
        
    # assign to new list
    swapID = []
    counterparty_email = []
    proposer_email = []
    counterparty_itemNumber = []
    proposer_itemNumber = []
    swap_date_proposed = []

    desired_item = []
    proposer_name = []
    rating=[]
    
    distance=[]
    proposed_item=[]
    myLat = 0
    myLong = 0
    their_postal=[]
    their_lat=[]
    their_long=[]
    
    postal_code=pd.read_sql_query(sql__accept_reject_getmypostalcode(counterparty_email[0]),cnx)
    myLat = pd.read_sql_query(sql__accept_reject_getmylat(postal_code),cnx)
    myLong = pd.read_sql_query(sql__accept_reject_getmylong(postal_code),cnx)

    swapID=df['swapID'].to_list()
    counterparty_email=df['counterparty_email'].to_list()
    proposer_email=df['proposer_email'].to_list()
    counterparty_itemNumber=df['counterparty_itemNumber'].to_list()
    proposer_itemNumber=df['proposer_itemNumber'].to_list()
    swap_date_proposed=df['swap_date_proposed'].to_list()

    # getting from other tables
    index=0
    for swapID_iter in swapID:
        desired_item[index] = str(pd.read_sql_query(sql__accept_reject_get_item_name(counterparty_itemNumber[index]),cnx))
        proposed_item[index] = str(pd.read_sql_query(sql__accept_reject_get_item_name(proposer_itemNumber[index]),cnx))
        proposer_name[index] = str(pd.read_sql_query(sql__accept_reject_get_user_name(proposer_email[index]),cnx))
        rating[index] = round(float(pd.read_sql_query(sql__accept_reject_get_user_rating(proposer_email[index]),cnx)),2)
        their_postal[index] = str(pd.read_sql_query(sql__accept_reject_getmypostalcode(proposer_email[index]),cnx))
        their_lat[index] = float(pd.read_sql_query(sql__accept_reject_getmylat(their_postal[index]),cnx))
        their_long[index] = float(pd.read_sql_query(sql__accept_reject_getmylong(their_postal[index]),cnx))
        
        distance[index] = str(round(float(haversine(abs(myLat-their_lat[index]),abs(myLong-their_long[index]))),1))+' kilometers'
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
        
        btn_accept = tk.Button(master=frame_left, text='Accept',command=lambda index_num=i:accept_swap(swapID[index],"4/19/2022"), font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        btn_accept.grid(row=i+1, column=7, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        btn_reject = tk.Button(master=frame_left, text='Reject',command=lambda index_num=i:reject_swap(swapID[index],"4/19/2022"), font=(LABEL_FONT_FAMILY, LABEL_FONT_SIZE, LABEL_FONT_WEIGHT_LABEL))
        btn_reject.grid(row=i+1, column=8, padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y, sticky='w')
        index+=1

    window.mainloop()


##############################
# MAIN
##############################
# if __name__ == "__main__":
#     #accept_reject_swaps('asd@dsa.com')
#     print (accept_reject_swaps.haversine(10,20))
    
    #window.mainloop()