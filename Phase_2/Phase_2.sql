-- DATABASE
DROP DATABASE IF EXISTS 'CS6400_spr18_team103'
SET default_storage_engine=''
SET NAMES -- todo

CREATE DATABASE IF NOT EXISTS CS6400_spr18_team103
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;
USE CS6400_spr18_team103;

GRANT SELECT,INSERT,UPDATE,DELETE,FILE ON *.* TO 'admin'@'localhost';
GRANT ALL PRIVILEGES ON 'CS6400_spr18_team103'.* TO 'admin'@'localhost';

-- TABLES
CREATE TABLE User (
    PRIMARY KEY email varchar('255'),
    user_firstname varchar('255'),
    user_lastname varchar('255'),
    user_nickname varchar('255'),
    user_password varchar('255'),
    unrated_swaps varchar('255'),
    unaccepted_swaps varchar('255'),
    
    user_rating float,
    -- foreign key(s):
    key fk_User_postalcode_UserAddress_postalcode REFERENCES UserAddress(addr_postal_code)
    key fk_User_phone_Phone_phone REFERENCES Phone(phone_number)

    
)

CREATE TABLE UserAddress (
    PRIMARY KEY postalcode varchar('255'),
    addr_city varchar('255'),
    addr_state varchar('255'),
    addr_latitude varchar('255'),
    addr_longitude varchar('255')
)

CREATE TABLE Phone (
    PRIMARY KEY phone_number varchar('255'),
    phone_share varchar('255'),
    phone_type varchar('255')
)

CREATE TABLE Item (
    KEY fk_Item_email_User_email REFERENCES User(email),
    PRIMARY KEY item_number int,    -- auto gen
    item_title varchar('255'),
    item_condition varchar('255'),
    item_description varchar('255')
)

CREATE TABLE ItemType (
    KEY fk_Swap_item_number_Item_item_number REFERENCES Item(item_number),
    itemtype_name varchar('255'),
    itemtype_description varchar('255'),
    itemtype_platform varchar('255'),
    itemtype_media varchar('255'),
    itemtype_piece_count int
)

CREATE TABLE Swap (
    PRIMARY KEY swapId int, -- auto gen
    swap_counterparty_rating float,
    swap_proposer_rating float,
    swap_date_responded date,
    swap_date_proposed date,
    swap_status varchar('255'),
    KEY fk_Swap_counterparty_User_email REFERENCES User(email),
    KEY fk_Swap_proposer_User_email REFERENCES User(email),
    KEY fk_Swap_proposed_item_Item_item_number REFERENCES Item(item_number),
    KEY fk_Swap_counterparty_item_Item_item_number REFERENCES Item(item_number)

)

-- CONSTRAINTS
-- Foreign Keys : fk_
--                fk_     
--                fk_
--                fk_
--                fk_




