from global_variables import DATABASE

##############################
# accept_reject_swaps.py
##############################
def sql__accept_reject_swaps_all(userEmail):
  sql__accept_reject_swaps_all = f'''
    SELECT
        swapID,
        counterparty_email,
        proposer_email,
        counterparty_itemNumber,
        proposer_itemNumber,
        swap_date_proposed
      FROM {DATABASE}.Swap
     WHERE counterparty_email={userEmail}
    '''
  return sql__accept_reject_swaps_all

def sql__accept_reject_get_item_name(itemNumberParam):
  sql__accept_reject_get_item_name = f'''
    SELECT
        item_title
      FROM {DATABASE}.item
     WHERE {DATABASE}.item.itemNumber={itemNumberParam}
    '''
  return sql__accept_reject_get_item_name

def sql__accept_reject_get_user_name(emailAddr):
  sql__accept_reject_get_user_name = f'''
    SELECT
        user_nickname
      FROM {DATABASE}.user
     WHERE {DATABASE}.user.email={emailAddr}
    '''
  return sql__accept_reject_get_user_name

def sql__accept_reject_get_user_rating(emailAddr):
  sql__accept_reject_get_user_rating = f'''
    SELECT
        user_rating
      FROM {DATABASE}.user
     WHERE {DATABASE}.user.email={emailAddr}
    '''
  return sql__accept_reject_get_user_name

##############################
# my_items.py
##############################

sql__my_items__count_of_item_type = f'''
  SELECT 
        itemtype_name, 
        count(*) as count
    FROM {DATABASE}.item
GROUP BY itemtype_name
'''

sql__my_items__list_of_all_items = f'''
  SELECT
        itemNumber,
        itemtype_name,
        item_title,
        item_condition,
        item_description
    FROM {DATABASE}.item
ORDER BY itemNumber ASC 
'''

##############################
# view_items.py
##############################
def sql__view_items__item_details(itemNumber):
  sql__view_items__item_details = f'''
    SELECT
        itemNumber,
        item_title,
        itemtype_name,
        itemtype_platform,
        itemtype_media,
        item_condition
      FROM {DATABASE}.item
     WHERE itemNumber={itemNumber}
    '''
  return sql__view_items__item_details
##############################
# GameSwap.py
##############################
def sql__gameswap__user_check(emailAddr):
   sql__gameswap__user_check = f'''
      Select count(1) cnt from  {DATABASE}.user where email='{emailAddr}'
'''
   return sql__gameswap__user_check


def sql__gameswap__postalcode_check(postalcode):
  sql__gameswap__postalcode_check = f'''
      Select count(1) cnt from   {DATABASE}.UserAddress where postalcode='{postalcode}'
'''
  return sql__gameswap__postalcode_check

def sql__gameswap__getcitystate(postalcode):
  sql__gameswap__getcitystate = f'''
      Select addr_City,addr_State  from   {DATABASE}.UserAddress where postalcode= '{postalcode}'
'''
  return sql__gameswap__getcitystate

def sql__gameswap__phonenumber_check(phonenumber):
  sql__gameswap__phonenumber_check = f'''
      Select count(1) cnt from  {DATABASE}.Phone where phone_number='{phonenumber}'
'''
  return sql__gameswap__phonenumber_check


def sql__gameswap__user_email_phonenumber__check(input):
  sql__gameswap__user_email_phonenumber__check = f'''
      Select email,phone_number,count(1) cnt from  CS6400_spr22_team103.user where email='{input}' or phone_number=  '{input}' group by email,phone_number
'''
  return sql__gameswap__user_email_phonenumber__check


def sql__gameswap__user_password__check(input,password):
  sql__gameswap__user_password__check = f'''
      Select email,phone_number,count(1) cnt from  CS6400_spr22_team103.user where user_password=  '{password}' and  (email= '{input}' or phone_number=  '{input}' ) group by email,phone_number
'''
  return sql__gameswap__user_password__check
