-- DATABASE

CREATE USER IF NOT EXISTS team103@localhost IDENTIFIED BY 'gatech123';

DROP DATABASE IF EXISTS 'CS6400_spr22_team103';
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

CREATE TABLE User (
    userID int(16) unsigned NOT NULL AUTO_INCREMENT,
    email varchar('255'),
    user_firstname varchar('255'),
    user_lastname varchar('255'),
    user_nickname varchar('255'),
    user_password varchar('255'),
    unrated_swaps varchar('255'),
    unaccepted_swaps varchar('255'),
    user_rating float,
      
    -- foreign key(s):
    constraint fk_User_postalcode_UserAddress_postalcode FOREIGN KEY (postalcode)
        REFERENCES UserAddress(postalcode),
    constraint fk_User_phone_Phone_phone FOREIGN KEY (phone_number)
        REFERENCES UserAddress(phone_number),

    -- key(s):
    PRIMARY KEY (userID),
    UNIQUE KEY email (email)

);

CREATE TABLE UserAddress (
    PRIMARY KEY postalcode varchar('255'),
    addr_city varchar('255'),
    addr_state varchar('255'),
    addr_latitude varchar('255'),
    addr_longitude varchar('255')
);

CREATE TABLE Phone (
    PRIMARY KEY phone_number varchar('255'),
    phone_share varchar('255'),
    phone_type varchar('255')
);

CREATE TABLE Item (
    itemNumber int(16) unsigned NOT NULL AUTO_INCREMENT ,
    item_title varchar('255'),
    item_condition varchar('255'),
    item_description varchar('255'),
    itemtype_name varchar('255'),
    itemtype_description varchar('255'),
    itemtype_platform varchar('255'),
    itemtype_media varchar('255'),
    itemtype_piece_count int,

    -- foreign key(s):
    constraint fk_Item_email_User_email FOREIGN KEY (email)
        REFERENCES User(email),

    -- key(s):
    PRIMARY KEY (itemNumber)

);

CREATE TABLE Swap (
    swapID int(16) unsigned NOT NULL AUTO_INCREMENT,
    swap_counterparty_rating float,
    swap_proposer_rating float,
    swap_date_responded date,
    swap_date_proposed date,
    swap_status varchar('255'),
    
    -- foreign key(s):
    constraint fk_Swap_counterparty_User_email FOREIGN KEY (email)
        REFERENCES User(email),
    constraint fk_Swap_proposer_User_email FOREIGN KEY (email)
        REFERENCES User(email),
    constraint fk_Swap_counterparty_item_Item_item_number FOREIGN KEY (itemNumber)
        REFERENCES Item(itemNumber),
    constraint fk_Swap_proposed_item_Item_item_number FOREIGN KEY (itemNumber)
        REFERENCES Item(itemNumber),

    -- key(s):
    PRIMARY KEY (swapID)

);

-- CONSTRAINTS
-- Foreign Keys : fk_User_postalcode_UserAddress_postalcode 
--                fk_User_phone_Phone_phone                 
--                fk_Item_email_User_email                        
--                fk_Swap_counterparty_User_email
--                fk_Swap_proposer_User_email
--                fk_Swap_proposed_item_Item_item_number
--                fk_Swap_counterparty_item_Item_item_number

ALTER TABLE User
    ADD CONSTRAINT fk_User_postalcode_UserAddress_postalcode FOREIGN KEY(postalcode) 
    REFERENCES UserAddress(postalcode) ON DELETE CASCADE ON UPDATE CASCADE,
    ADD CONSTRAINT fk_User_phone_Phone_phone_number FOREIGN KEY(phone_number) 
    REFERENCES Phone(phone_number) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Item
    ADD CONSTRAINT fk_Item_email_User_email FOREIGN KEY (email) 
    REFERENCES User(email) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Swap
    ADD CONSTRAINT fk_Swap_counterparty_User_email FOREIGN KEY(email) 
    REFERENCES User(email) ON UPDATE CASCADE,
    ADD CONSTRAINT fk_Swap_proposer_User_email FOREIGN KEY(email) 
    REFERENCES User(email) ON UPDATE CASCADE,
    ADD CONSTRAINT fk_Swap_proposed_item_Item_item_number FOREIGN KEY(item_number) 
    REFERENCES Item(item_number) ON UPDATE CASCADE,
    ADD CONSTRAINT fk_Swap_counterparty_item_Item_item_number FOREIGN KEY(item_number) 
    REFERENCES Item(item_number) ON UPDATE CASCADE;