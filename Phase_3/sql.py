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


def sql__gameswap__email_fetch(input):
  sql__gameswap__email_fetch = f'''
      Select email  from  {DATABASE}.user where email='{input}' or phone_number=  '{input}' 
'''
  return sql__gameswap__email_fetch


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
      Select count(1) cnt from  CS6400_spr22_team103.user where user_password=  '{password}' and  (email= '{input}' or phone_number=  '{input}' ) 
'''
  return sql__gameswap__user_password__check

##############################
# ManinMenu.py
##############################
def sql__firstlastname__fetch(emailAddr):
   sql__firstlastname__fetch = f'''
      Select concat(user_firstname, ',' , user_lastname) name from  {DATABASE}.user where email='{emailAddr}'
'''
   return sql__firstlastname__fetch


def sql__myrating__fetch(emailAddr):
   sql__myrating__fetch= f'''
        Select
    avg(rating)
    user_rating, email
    from
    (Select sum(coalesce(swap_proposer_rating, 0)) rating, proposer_email
    email
    from CS6400_spr22_team103.swap where
    proposer_email = '{emailAddr}'
    union
    all
    Select
    sum(coalesce(swap_counterparty_rating, 0)), counterparty_email
    from CS6400_spr22_team103.swap where
    counterparty_email = '{emailAddr}') a
    group
    by
    email
         '''
   return sql__myrating__fetch


def sql__unacceptedswaps__fetch(emailAddr):
  sql__unacceptedswaps__fetch = f'''
        Select count(1) unaccepted_swaps from (Select 1 from CS6400_spr22_team103.swap where counterparty_email='{emailAddr}' and swap_date_responded is null) A
         '''
  return sql__unacceptedswaps__fetch

def sql__fivedayoldswap__fetch(emailAddr):
  sql__fivedayoldswap__fetch = f'''
        Select count(1) fivedayoldswaps from (Select 1 from CS6400_spr22_team103.swap where counterparty_email='{emailAddr}' and swap_date_responded is null and current_date-swap_date_proposed >4) A      '''
  return sql__fivedayoldswap__fetch

def sql__unratedswaps__fetch(emailAddr):
  sql__unratedswaps__fetch = f'''
        Select count(1) unrated_swaps from (Select swap_date_responded as acceptancedatee, 'Proposer' my_role,p_item.item_title ProposedItem, c_item.item_title DesiredItem,d_user.user_nickname other_user from CS6400_spr22_team103.swap s join CS6400_spr22_team103.item p_item on s.proposer_itemNumber=p_item.itemNumber
join CS6400_spr22_team103.item c_item on s.counterparty_itemNumber=c_item.itemNumber
join CS6400_spr22_team103.user d_user on s.counterparty_email=d_user.email
 where proposer_email='{emailAddr}' and swap_status='Accepted' and swap_proposer_rating is null 
Union
Select swap_date_responded as acceptancedatee, 'Counterparty',p_item.item_title ProposedItem, c_item.item_title DesiredItem,d_user.user_nickname from CS6400_spr22_team103.swap s join CS6400_spr22_team103.item p_item on s.proposer_itemNumber=p_item.itemNumber
join CS6400_spr22_team103.item c_item on s.counterparty_itemNumber=c_item.itemNumber
join CS6400_spr22_team103.user d_user on s.counterparty_email=d_user.email
 where counterparty_email='{emailAddr}'and swap_counterparty_rating is null and swap_status='Accepted') a   '''
  return sql__unratedswaps__fetch

##############################
# additem.py
##############################

def sql__itemnumber__fetch(emailAddr):
  sql__itemnumber__fetch = f'''
        Select max(itemnumber) from  CS6400_spr22_team103.item  where email=  '{emailAddr}'
'''
  return sql__itemnumber__fetch


##############################
# RateSwaps.py
##############################
def sql_get_my_unrated_swaps(emailAddr):
  sql_get_my_unrated_swaps = f'''
  SELECT * from {DATABASE}.swap 
  WHERE (swap_status="accepted" and swap_counterparty_rating is null and proposer_email={emailAddr})
  OR (swap_status="accepted"  and swap_proposer_rating is null and counterparty_email={emailAddr})
  '''

  return sql_get_my_unrated_swaps

def sql_rate_my_unrated_swaps(emailAddr, swapID, rating):
  sql_get_my_unrated_swaps = f'''
  UPDATE {DATABASE}.swap 
  SET swap_counterparty_rating =
  CASE when proposer_email={emailAddr} then {rating} end,
	    swap_proposer_rating =
  CASE when counterparty_email={emailAddr} then {rating} end
  where swapID = {swapID}
  ;
  '''
  return sql_rate_my_unrated_swaps
