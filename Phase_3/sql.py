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
     WHERE counterparty_email='{userEmail}'
     and swap_date_responded is null
     ORDER BY swap_date_proposed DESC
    '''
  return sql__accept_reject_swaps_all

def sql__accept_reject_get_item_name(itemNumberParam):
  sql__accept_reject_get_item_name = f'''
    SELECT
        item_title
      FROM {DATABASE}.item
     WHERE itemNumber={itemNumberParam}
    '''
  return sql__accept_reject_get_item_name

def sql__accept_reject_get_user_name(emailAddr):
  sql__accept_reject_get_user_name = f'''
    SELECT
        user_nickname
      FROM {DATABASE}.user
     WHERE {DATABASE}.user.email='{emailAddr}'
    '''
  return sql__accept_reject_get_user_name

def sql__accept_reject_get_user_rating(emailAddr):
  sql__accept_reject_get_user_rating = f'''
    SELECT
        user_rating
      FROM {DATABASE}.user
     WHERE {DATABASE}.user.email='{emailAddr}'
    '''
  return sql__accept_reject_get_user_name

def sql__accept_reject_getmypostalcode(emailAddr):
  sql__accept_reject_getmypostalcode = f''' 
  SELECT postalcode
    FROM {DATABASE}.User
    WHERE email='{emailAddr}'
'''
  return sql__accept_reject_getmypostalcode


def sql__accept_reject_getmylat(postalCode):
  sql__accept_reject_getmylat = f'''
  SELECT
        addr_latitude
    FROM {DATABASE}.UserAddress
    WHERE postalcode={postalCode}
'''
  return sql__accept_reject_getmylat

def sql__accept_reject_getmylong(postalCode):
  sql__accept_reject_getmylong = f'''
  SELECT
        addr_longitude
    FROM {DATABASE}.UserAddress
    WHERE postalcode={postalCode}
'''
  return sql__accept_reject_getmylong

def sql__respond_swap(swapID,response_date,status):
  sql__respond_swap  = f'''
  UPDATE {DATABASE}.Swap
  SET
        swap_date_responded=current_date,
        swap_status='{status}'
  WHERE swapID={swapID}
  '''
  return sql__respond_swap

##############################
# my_items.py
##############################

def sql__my_items__count_of_item_type(emailAddr):
  sql__my_items__count_of_item_type = f'''
    SELECT 
          itemtype_name, 
          count(*) as count
      FROM {DATABASE}.item
     WHERE email='{emailAddr}'
      AND itemNumber NOT IN ( 
          SELECT
            DISTINCT counterparty_itemNumber
            FROM
              {DATABASE}.swap
          WHERE
              swap_status='Accepted' or swap_status = ''
          UNION
          SELECT
          DISTINCT proposer_itemNumber
          FROM
            {DATABASE}.swap
          WHERE
            swap_status='Accepted' or swap_status = ''
        )
  GROUP BY itemtype_name
  '''
  return sql__my_items__count_of_item_type

def sql__my_items__list_of_all_items(emailAddr):
   sql__my_items__list_of_all_items = f'''
    SELECT 
        itemNumber,
        itemtype_name,
        item_title,
        item_condition,
        item_description
      FROM {DATABASE}.item
     WHERE email='{emailAddr}'
      AND itemNumber NOT IN ( 
          SELECT
            DISTINCT counterparty_itemNumber
            FROM
              {DATABASE}.swap
          WHERE
              swap_status='Accepted' or swap_status = ''
          UNION
          SELECT
          DISTINCT proposer_itemNumber
          FROM
            {DATABASE}.swap
          WHERE
            swap_status='Accepted' or swap_status = ''
        )
ORDER BY itemNumber ASC 
'''
   return sql__my_items__list_of_all_items
   
##############################
# UpdateMyInfo.py
##############################
def sql__pull_nick(userEmail):
  sql__pull_nick = f'''
      SELECT
        user_nickname
      FROM {DATABASE}.user
     WHERE email='{userEmail}'
'''
  return sql__pull_nick

def sql__pull_city(postalCode):
  if {postalCode} !={None}:
      print({postalCode})
      sql__pull_city = f'''
      SELECT
        addr_city
      FROM {DATABASE}.UserAddress
     WHERE postalcode={postalCode} 
     '''
  else:
      sql__pull_city = f'''
           SELECT
             addr_city
           FROM {DATABASE}.UserAddress
          WHERE 1=2 
          '''
  return sql__pull_city

def sql__pull_first_name(userEmail):
  sql__pull_first_name = f'''
      SELECT
        user_firstname
      FROM {DATABASE}.user
     WHERE email='{userEmail}'
'''
  return sql__pull_first_name

def sql__pull_state(postalCode):
    if {postalCode} != {None}:
        print({postalCode})
        sql__pull_state = f'''
        SELECT
          addr_state
        FROM {DATABASE}.UserAddress
       WHERE postalcode={postalCode} 
       '''
    else:
        sql__pull_state = f'''
             SELECT
               addr_state
             FROM {DATABASE}.UserAddress
            WHERE 1=2 
            '''
    return sql__pull_state


def sql__pull_last_name(userEmail):
  sql__pull_last_name = f'''
      SELECT
        user_lastname
      FROM {DATABASE}.user
     WHERE email='{userEmail}'
'''
  return sql__pull_last_name

def sql__pull_password(userEmail):
  sql__pull_last_name = f'''
      SELECT
        user_password
      FROM {DATABASE}.user
     WHERE email='{userEmail}'
'''
  return sql__pull_last_name

def sql__pull_zip(userEmail):
  sql__pull_zip = f'''
      SELECT
        postalcode
      FROM {DATABASE}.user
     WHERE email='{userEmail}'
'''
  return sql__pull_zip

def sql__pull_phone(userEmail):
  sql__pull_phone = f'''
      SELECT
        phone_number
      FROM {DATABASE}.user
     WHERE email='{userEmail}'
'''
  return sql__pull_phone

##############################
# propose_swap.py
##############################
def sql__propose_swap__item_details(emailAddr, item_number):
  sql__propose_swap__item_details = f'''
  SELECT
    item.itemNumber,
    item.item_title,
    item.itemtype_name,
    item.itemtype_platform,
    item.itemtype_media,
    item.item_condition,
    item.item_description,
    item.itemtype_piece_count,
    CONCAT(user.user_firstname, ' ', SUBSTRING(user.user_lastname, 1, 1), '.') AS offered_by,
    user.email AS offered_by_email,
    CONCAT(useraddress.addr_city, ', ', useraddress.addr_state, ' ', useraddress.postalcode) AS location,
    useraddress.addr_latitude AS other_addr_lat,
    useraddress.addr_longitude AS other_addr_lon,
    (
      SELECT 
            useraddress.addr_latitude
        FROM 
            {DATABASE}.user AS user 
  INNER JOIN 
            {DATABASE}.useraddress AS useraddress
          ON
            user.postalcode = useraddress.postalcode
       WHERE
            user.email = '{emailAddr}'
    ) AS user_addr_lat,
    (
      SELECT 
            useraddress.addr_longitude
        FROM 
            {DATABASE}.user AS user 
 INNER JOIN 
            {DATABASE}.useraddress AS useraddress
         ON
            user.postalcode = useraddress.postalcode
      WHERE
            user.email = '{emailAddr}'
    ) AS user_addr_lon  
  FROM
    {DATABASE}.item AS item
INNER JOIN
    {DATABASE}.user AS user
    ON
    item.email = user.email
INNER JOIN
    {DATABASE}.useraddress AS useraddress
    ON
    user.postalcode = useraddress.postalcode
 WHERE
    item.itemNumber={item_number}
  '''
  return sql__propose_swap__item_details

##############################
# propose_swap_confirm.py
##############################
def sql__propose_swap_confirm__items_for_swap(emailAddr):
  sql__propose_swap_confirm__items_for_swap = f'''
    SELECT
      itemNumber,
      itemtype_name,
      item_title,
      item_condition
      FROM
        {DATABASE}.item
     WHERE
      email = '{emailAddr}'
      AND itemNumber NOT IN (
        SELECT
          DISTINCT counterparty_itemNumber
          FROM
            {DATABASE}.swap
         WHERE
            swap_status='Accepted' or swap_status = ''
         UNION
        SELECT
        DISTINCT proposer_itemNumber
        FROM
          {DATABASE}.swap
        WHERE
          swap_status='Accepted' or swap_status = ''
      )
  ORDER BY itemNumber ASC
  '''
  return sql__propose_swap_confirm__items_for_swap

##############################
# propose_swap_confirm_insert.py
##############################

def sql__propose_swap_confirm__insert_swap(
  proposer_email,
  swap_date_proposed,
  swap_status,
  counterparty_email,
  proposer_itemNumber,
  counterparty_itemNumber
):
  sql__propose_swap_confirm__insert_swap = f'''
  INSERT INTO {DATABASE}.swap (proposer_email, swap_date_proposed, swap_status, counterparty_email, proposer_itemNumber, counterparty_itemNumber)
    VALUES ('{proposer_email}', '{swap_date_proposed}', '{swap_status}', '{counterparty_email}', '{proposer_itemNumber}', '{counterparty_itemNumber}')
  '''
  return sql__propose_swap_confirm__insert_swap

##############################
# view_items.py
##############################
def sql__view_items__item_details(item_number):
  sql__view_items__item_details = f'''
    SELECT
        itemNumber,
        item_title,
        itemtype_name,
        itemtype_platform,
        itemtype_media,
        item_condition,
        item_description,
        itemtype_piece_count
      FROM {DATABASE}.item
     WHERE itemNumber='{item_number}'
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

def sql__gameswap__phonenumber_withemail_check(input):
  sql__gameswap__phonenumber_withemail_check = f'''
      Select phone_number from  CS6400_spr22_team103.user where email='{input}'
'''
  return sql__gameswap__phonenumber_withemail_check
def sql__gameswap__user_password__check(input,password):
  sql__gameswap__user_password__check = f'''
      Select count(1) cnt from  CS6400_spr22_team103.user where user_password=  '{password}' and  (email= '{input}' or phone_number=  '{input}' ) 
'''
  return sql__gameswap__user_password__check

def sql__phonetable__insert(phonenumber,phoneshareflag,phonetype):
    sql__phonetable__insert = f'''
    insert into CS6400_spr22_team103.Phone (phone_number,phone_share,phone_type) values  ('{phonenumber},'{phoneshareflag}','{phonetype}')
    '''
    return sql__phonetable__insert

def sql__usertable__insert(email,user_firstname,user_lastname,user_nickname,user_password,postalcode,phone_number):
    sql__usertable__insert = f'''
    insert into CS6400_spr22_team103.user (email,user_firstname,user_lastname,user_nickname,user_password,postalcode,phone_number) values  ('{email},'{user_firstname}','{user_lastname}','{user_password}','{postalcode}','{phone_number}')
    '''

    return sql__usertable__insert

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
        Select max(itemnumber) itemnumber from  CS6400_spr22_team103.item  where email=  '{emailAddr}'
'''
  return sql__itemnumber__fetch

def sql__itemtable__insert(item_title, item_condition, item_description, itemtype_name, itemtype_platform,
                              itemtype_media, itemtype_piece_count, email):
    sql__itemtable_insert = f'''
    insert into CS6400_spr22_team103.item(item_title, item_condition, item_description, itemtype_name, itemtype_platform,itemtype_media, itemtype_piece_count, email)
    values  ('{item_title},'{item_condition}','{item_description}','{itemtype_name}','{itemtype_platform}','{itemtype_media}',{itemtype_piece_count},'{email}')
    '''

    return sql__itemtable__insert
##############################
# RateSwaps.py
##############################
def sql_get_my_unrated_swaps(emailAddr):
  sql_get_my_unrated_swaps = f'''
    SELECT 
      swapID, 
      swap_date_proposed, 
      swap_date_responded, 
      user_email, 
      item_number, 
      item_title, 
      item_condition, 
      item_description 
    FROM
      (SELECT * 
      FROM
        (SELECT swapID, swap_date_proposed, swap_date_responded, counterparty_email as user_email, counterparty_itemNumber as item_number from {DATABASE}.swap
          WHERE swap_status="Accepted" AND swap_proposer_rating is null AND proposer_email='{emailAddr}') 
          AS table1 
        UNION
        (SELECT swapID, swap_date_proposed, swap_date_responded, proposer_email as user_email, proposer_itemNumber 
          AS item_number from {DATABASE}.swap
          WHERE swap_status="Accepted" AND swap_counterparty_rating is null AND counterparty_email='{emailAddr}')) 
      AS unrated_swaps 
      JOIN
      (SELECT * FROM {DATABASE}.item) 
      AS items
    ON item_number = itemNumber;
  '''
  return sql_get_my_unrated_swaps

def sql_rate_my_unrated_swaps(emailAddr, swapID, rating):
  sql_rate_my_unrated_swaps = f'''
  UPDATE {DATABASE}.swap 
  SET swap_proposer_rating =
  CASE when proposer_email='{emailAddr}' then {rating} end,
	    swap_counterparty_rating =
  CASE when counterparty_email='{emailAddr}' then {rating} end
  where swapID = {swapID};
  '''
  return sql_rate_my_unrated_swaps

##############################
# swap_history.py
#############################

#pull all swapID in database.
#if the user, useremail = counterparty_email, or proser_email
#add to the list
#pull all swapID in database.
#if the user, useremail = counterparty_email, or proser_email
#add to the list
def sql_get_swap_history(userEmail):
  sql_get_swap_history = f'''
    SELECT
        swapID,
        swap_counterparty_rating,
        swap_proposer_rating,
        swap_date_responded,
        swap_date_proposed,
        swap_status,
        counterparty_email,
        proposer_email,
        counterparty_itemNumber,
        proposer_itemNumber
      FROM {DATABASE}.swap
     WHERE counterparty_email='{userEmail}' OR proposer_email='{userEmail}'
     ORDER BY swap_date_proposed DESC
    '''
  return sql_get_swap_history
##############################
# search.py
##############################
def sql__search__items_by_keyword(keyword):
  sql__search__items_by_keyword = f'''
    SELECT
      itemNumber
      FROM {DATABASE}.item as item
     WHERE 
      (item_title like '%{keyword}%' 
        OR lower(item_description) like '%{keyword}%'
        OR lower(item_condition) like '%{keyword}%'
        OR lower(itemtype_name) like '%{keyword}%')
      AND itemNumber NOT IN ( 
        SELECT
          DISTINCT counterparty_itemNumber
          FROM
            {DATABASE}.swap
         WHERE
            swap_status='Accepted' or swap_status = ''
         UNION
        SELECT
        DISTINCT proposer_itemNumber
        FROM
          {DATABASE}.swap
        WHERE
          swap_status='Accepted' or swap_status = ''
      )
  '''
  return sql__search__items_by_keyword

def sql__search__get_postal_code_by_email(email):
  sql__search__get_postal_code_by_email = f'''
    SELECT 
      DISTINCT postalcode 
      FROM {DATABASE}.user
     WHERE email = '{email}'
  '''
  return sql__search__get_postal_code_by_email

def sql__search__items_by_my_postal_code(email):
  sql__search__items_by_my_postal_code = f'''
    WITH a as (
	    SELECT
		    email
	      FROM {DATABASE}.user
	     WHERE 
          postalcode = (
		        SELECT 
              DISTINCT postalcode 
              FROM {DATABASE}.user
             WHERE email = '{email}'
	        )
          AND email <> '{email}'
    ),
    b as (
	        SELECT
            itemNumber
	          FROM {DATABASE}.item as z
      INNER JOIN a
              ON a.email = z.email
    )
    SELECT itemNumber 
      FROM b
      wHERE itemNumber NOT IN (
        SELECT
          DISTINCT counterparty_itemNumber
          FROM
            {DATABASE}.swap
         WHERE
            swap_status='Accepted' or swap_status = ''
         UNION
        SELECT
        DISTINCT proposer_itemNumber
        FROM
          {DATABASE}.swap
        WHERE
          swap_status='Accepted' or swap_status = ''
      )
  '''
  return sql__search__items_by_my_postal_code

def sql__search__get_lat_lon_by_postal_code(postal_code):
  sql__search__get_lat_lon_by_postal_code = f''' 
    SELECT
      addr_latitude,
      addr_longitude
      FROM
        {DATABASE}.useraddress
     WHERE
      postalcode = {postal_code}
  '''
  return sql__search__get_lat_lon_by_postal_code

def sql__search__items_by_other_postal_code(postal_code):
  sql__search__items_by_other_postal_code = f'''
    SELECT
	    itemNumber
      FROM
        {DATABASE}.item
     WHERE
      email IN (
        SELECT
	        email
          FROM
	          {DATABASE}.user 
         WHERE
          postalcode in ({postal_code})
      )
      AND itemNumber NOT IN (
        SELECT
          DISTINCT counterparty_itemNumber
          FROM
            {DATABASE}.swap
         WHERE
            swap_status='Accepted' or swap_status = ''
         UNION
        SELECT
        DISTINCT proposer_itemNumber
        FROM
          {DATABASE}.swap
        WHERE
          swap_status='Accepted' or swap_status = ''
      )
  '''
  return sql__search__items_by_other_postal_code

def sql__search__get_all_postal_codes_lat_lon():
  sql__search__get_all_postal_codes_lat_lon = f'''
     SELECT
      postalcode,
      addr_latitude,
      addr_longitude
        FROM
        {DATABASE}.useraddress
    ORDER BY
      postalcode asc
  '''
  return sql__search__get_all_postal_codes_lat_lon

##############################
# search_results.py
##############################

# This function return all necessary fields except distance
# Distance must be computed separately
def sql__search_results__get_item_data_from_item_numbers(item_number):
    sql__search_results__get_item_data_from_item_numbers = f'''
    SELECT
	    itemNumber,
      itemtype_name,
      item_title,
      item_condition,
      item_description
      FROM
        {DATABASE}.item
     WHERE
      itemNumber = {item_number}
  '''
    return sql__search_results__get_item_data_from_item_numbers


def sql__search_results__get_lat_lon_from_item_number(item_number):
    sql__search_results__get_lat_lon_from_item_number = f'''
      SELECT
        useraddress.addr_latitude,
        useraddress.addr_longitude
        FROM
          {DATABASE}.item AS item
  INNER JOIN
          {DATABASE}.user AS user
          ON 
          item.email=user.email
  INNER JOIN
          {DATABASE}.useraddress AS useraddress
          ON
          user.postalcode=useraddress.postalcode
       WHERE
          item.itemNumber={item_number};
  '''
    return sql__search_results__get_lat_lon_from_item_number


def sql_swap_title(userEmail):
    sql_swap_title = f'''
select
    swapID, swap_date_proposed, swap_counterparty_rating, swap_proposer_rating, swap_date_responded, swap_status, counterparty_itemNumber, item.item_title, item.itemNumber, proposer_itemNumber, proposer_email, counterparty_email
from
    CS6400_spr22_team103.swap as swap
inner join
    CS6400_spr22_team103.item as item
on
    swap.proposer_itemNumber = item.itemNumber 
where counterparty_email ='{userEmail}' or proposer_email = '{userEmail}'
    '''
    return sql_swap_title


def sql_rating_count_proposer(userEmail):
    sql_rating_count_proposer = f'''
select COUNT(CASE WHEN swap_status="Accepted" or swap_status="Rejected" then 1 end) as total, COUNT(CASE WHEN swap_status = "Accepted" then 1 end) as accepted_count, COUNT(CASE when swap_status="Rejected" then 1 end) as rejected_count
from CS6400_spr22_team103.swap
where proposer_email ='{userEmail}'
    '''
    return sql_rating_count_proposer


def sql_rating_count_counter(userEmail):
    sql_rating_count_counter = f'''
select COUNT(CASE WHEN swap_status="Accepted" or swap_status="Rejected" then 1 end) as total, COUNT(CASE WHEN swap_status = "Accepted" then 1 end) as accepted_count, COUNT(CASE when swap_status="Rejected" then 1 end) as rejected_count
from CS6400_spr22_team103.swap
where counterparty_email ='{userEmail}'
    '''
    return sql_rating_count_counter

def sql__pull_itemname(itemNum):
  sql__pull_itemname = f'''
      SELECT
        item_title
      FROM {DATABASE}.Item
     WHERE itemNumber='{itemNum}'
'''
  return sql__pull_itemname
