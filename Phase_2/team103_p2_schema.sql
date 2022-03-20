-- DATABASE

CREATE USER IF NOT EXISTS team103@localhost IDENTIFIED BY 'gatech123';

DROP DATABASE IF EXISTS CS6400_spr22_team103;
SET default_storage_engine='INNODB';
SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE DATABASE IF NOT EXISTS CS6400_spr22_team103
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;
USE CS6400_spr22_team103;

GRANT SELECT,INSERT,UPDATE,DELETE,FILE ON *.* TO 'team103'@'localhost';
GRANT ALL PRIVILEGES ON 'CS6400_spr22_team103'.* TO 'team103'@'localhost';
FLUSH PRIVILEGES;

-- TABLES
CREATE TABLE IF NOT EXISTS CS6400_spr22_team103.UserAddress (
    postalcode varchar(255),
    addr_city varchar(255),
    addr_state varchar(255),
    addr_latitude varchar(255),
    addr_longitude varchar(255),
    PRIMARY KEY (postalcode)
);

CREATE TABLE IF NOT EXISTS CS6400_spr22_team103.Phone (
    phone_number varchar(255),
    phone_share varchar(255),
    phone_type varchar(255),
    PRIMARY KEY (phone_number)
);

CREATE TABLE IF NOT EXISTS CS6400_spr22_team103.User(
    userID int(16) unsigned NOT NULL AUTO_INCREMENT,
    email varchar(255),
    user_firstname varchar(255),
    user_lastname varchar(255),
    user_nickname varchar(255),
    user_password varchar(255),
    unrated_swaps varchar(255),
    unaccepted_swaps varchar(255),
    user_rating float,
      
    -- foreign key(s):
    postalcode varchar(255),
    constraint fk_User_postalcode_UserAddress_postalcode FOREIGN KEY (postalcode)
        REFERENCES UserAddress(postalcode),
    phone_number varchar(255),
    constraint fk_User_phone_number_Phone_phone FOREIGN KEY (phone_number)
        REFERENCES Phone(phone_number),

    -- key(s):
    PRIMARY KEY (userID),
    UNIQUE KEY email (email)

);

CREATE TABLE IF NOT EXISTS CS6400_spr22_team103.Item (
    itemNumber int(16) unsigned NOT NULL AUTO_INCREMENT ,
    item_title varchar(255),
    item_condition varchar(255),
    item_description varchar(255),
    itemtype_name varchar(255),
    itemtype_description varchar(255),
    itemtype_platform varchar(255),
    itemtype_media varchar(255),
    itemtype_piece_count int,

    -- foreign key(s):
    email varchar(255),
    constraint fk_Item_email_User_email FOREIGN KEY (email)
        REFERENCES User(email),

    -- key(s):
    PRIMARY KEY (itemNumber)
    
);

CREATE TABLE IF NOT EXISTS CS6400_spr22_team103.Swap(
    swapID int(16) unsigned NOT NULL AUTO_INCREMENT,
    swap_counterparty_rating float,
    swap_proposer_rating float,
    swap_date_responded date,
    swap_date_proposed date,
    swap_status varchar(255),
    
    -- foreign key(s):
    counterparty_email varchar(255),
    constraint fk_Swap_counterparty_User_email FOREIGN KEY (counterparty_email)
        REFERENCES User(email),

    proposer_email varchar(255),
    constraint fk_Swap_proposer_User_email FOREIGN KEY (proposer_email)
        REFERENCES User(email),

    counterparty_itemNumber int(16),
    constraint fk_Swap_counterparty_item_Item_item_number FOREIGN KEY (counterparty_itemNumber)
        REFERENCES Item(itemNumber),

    proposer_itemNumber int(16),
    constraint fk_Swap_proposed_item_Item_item_number FOREIGN KEY (proposer_itemNumber)
        REFERENCES Item(itemNumber),

    -- key(s):
    PRIMARY KEY (swapID)

);