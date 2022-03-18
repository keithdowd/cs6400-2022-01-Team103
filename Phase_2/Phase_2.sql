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
    firstname varchar('255'),
    lastname varchar('255'),
    nickname varchar('255'),
    password varchar('255'),
    city varchar('255'),
    my_rating float,

    -- foreign key(s):
    key fk_User_unaccepted_Swap_swap_id REFERENCES Swap(SwapId),
    key fk_User_unrated_Swap_swap_id REFERENCES Swap(SwapId)

    -- surrogate key(s):
    
)

CREATE TABLE UserAddress (
    KEY fk_UserAddress_email_User_email REFERENCES User(email),
    PRIMARY KEY addr+postal_code varchar('255'),
    addr_city varchar('255'),
    addr_state varchar('255'),
    addr_latitude varchar('255'),
    addr_longitude varchar('255')
)

CREATE TABLE Phone (
    KEY fk_Phone_email_User_email REFERENCES User(email),
    PRIMARY KEY phone_number varchar('255'),
    phone_share varchar('255'),
    phone_type varchar('255')
)

CREATE TABLE Item (
    KEY fk_Item_email_User_email REFERENCES User(email),
    PRIMARY KEY item_number int,
    item_title varchar('255'),
    item_condition varchar('255'),
    item_description varchar('255')
)

CREATE TABLE ItemType (
    itemtype_name varchar('255'),
    itemtype_description varchar('255'),
    itemtype_platform varchar('255'),
    itemtype_media varchar('255'),
    itemtype_piece_count int
)

CREATE TABLE Swap (
    PRIMARY KEY swapId int,
    swap_counterparty_rating float,
    swap_proposer_rating float,
    swap_date_responded date,
    swap_date_proposed date,
    swap_status varchar('255')
)

-- CONSTRAINTS
-- Foreign Keys : fk_User_unaccepted_Swap_swap_id,
--                fk_User_unrated_Swap_swap_id     
--                fk_UserAddress_email_User_email
--                fk_Phone_email_User_email
--                fk_Item_email_User_email




