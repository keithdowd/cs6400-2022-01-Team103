from global_variables import *
import search
from sql import sql__propose_swap_confirm__insert_swap


def propose_swap_insert(
  proposer_email,
  counterparty_email,
  proposer_itemNumber,
  counterparty_itemNumber,
  swap_status,
  swap_date_proposed
):


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

  window = setup(
    title=WINDOW_TITLE, 
    width=700, 
    height=WINDOW_SIZE_HEIGHT)


  ##############################
  # PROPOSE SWAP (INSERT)
  ##############################

  ########## DATA

  def return_exec():
    search.search(proposer_email)
    window.destroy()

  proposer_email = proposer_email
  counterparty_email = counterparty_email
  proposer_itemNumber = proposer_itemNumber
  counterparty_itemNumber = counterparty_itemNumber
  swap_status = swap_status
  swap_date_proposed = swap_date_proposed

  try:
    mycursor = cnx.cursor()
    mycursor.execute(sql__propose_swap_confirm__insert_swap(
      proposer_email,
      swap_date_proposed,
      swap_status,
      counterparty_email,
      proposer_itemNumber,
      counterparty_itemNumber
    ))
    cnx.commit()

    message = 'Your proposal was submitted. Please return to the main menu.'
  except:
    message = 'Your proposal failed to submit. Please return to the main menu and try again.'

  ########## VIEW

  # Header
  label_propose_swap = tk.Label(
    master=window, 
    text='Propose Swap', 
    font=(
      LABEL_FONT_FAMILY,
      LABEL_FONT_SIZE,
      LABEL_FONT_WEIGHT_VALUE
  ))
  label_propose_swap.grid(
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
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='ew')
  
  # Message
  label_message = tk.Label(
    master=window, 
    text=message, 
    font=(
      LABEL_FONT_FAMILY,
      LABEL_FONT_SIZE,
      LABEL_FONT_WEIGHT_VALUE
  ))
  label_message.grid(
    row=3, 
    column=0, 
    padx=WINDOW_PADDING_X, 
    pady=WINDOW_PADDING_Y, 
    sticky='w')

# Confirm button
  return_btn = tk.Button(
    master=window, 
    text='Return to Search',
    font=(
      LABEL_FONT_FAMILY,
      LABEL_FONT_SIZE,
      LABEL_FONT_WEIGHT_VALUE,
    ),
    command=return_exec
  )
  return_btn.grid(
    row=4,
    column=0,
    pady=20,
    padx=WINDOW_PADDING_X,
    sticky='w') 

##############################
# EVENT LOOP
##############################
# window.mainloop()