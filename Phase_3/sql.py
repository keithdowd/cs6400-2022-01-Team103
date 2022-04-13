from global_variables import DATABASE

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