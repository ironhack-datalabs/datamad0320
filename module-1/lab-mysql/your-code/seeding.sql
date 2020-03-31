ALTER TABLE `lab_mysql`.`Car` 
CHANGE COLUMN `Year` `Year` INT NOT NULL ;
INSERT INTO `lab_mysql`.`Car` (`ID`, `VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES ('0', '3K096I98581DHSNUP', 'Volkswagen', 'Tiguan', '2019', 'Blue');
INSERT INTO `lab_mysql`.`Car` (`ID`, `VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES (1, 'ZM8G7BEUQZ97IH46V', 'Peugeot', 'Rifter', '2019', 'Red');
INSERT INTO `lab_mysql`.`Car` (`ID`, `VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES (2, 'RKXVNNIHLVVZOUB4M', 'Ford', 'Fusion', '2018', 'White');
INSERT INTO `lab_mysql`.`Car` (`ID`, `VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES (3, 'HKNDGS7CU31E9Z7JW', 'Toyota', 'RAV4', '2018', 'Silver');
INSERT INTO `lab_mysql`.`Car` (`ID`, `VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES (4, 'DAM41UDN3CHU2WVF6', 'Volvo', 'V60', '2019', 'Gray');
ALTER TABLE `lab_mysql`.`Car` 
DROP INDEX `VIN_UNIQUE` ;
;
INSERT INTO `lab_mysql`.`Car` (`ID`, `VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES (5, 'DAM41UDN3CHU2WVF6', 'Volvo', 'V60 Cross Country', '2019', 'Gray');
ALTER TABLE `lab_mysql`.`Customer` 
CHANGE COLUMN `Phone` `Phone` VARCHAR(20) NOT NULL ;
INSERT INTO `lab_mysql`.`Customer` (`ID`, `Customer ID`, `Name`, `Phone`, `Address`, `City`, `State/Province`, `Country`, `Postal`) VALUES ('0', '10001', 'Pablo Picasso', '+34 636 17 63 82', 'Paseo de la Chopera, 14', 'Madrid', 'Madrid', 'Spain', '28945');
INSERT INTO `lab_mysql`.`Customer` (`ID`, `Customer ID`, `Name`, `Phone`, `Address`, `City`, `State/Province`, `Country`, `Postal`) VALUES ('1', '20001', 'Abraham Lincoln', '+1 305 907 7086', '120 SW 8th St', 'Miami', 'Florida', 'United States', '33130');
INSERT INTO `lab_mysql`.`Customer` (`ID`, `Customer ID`, `Name`, `Phone`, `Address`, `City`, `State/Province`, `Country`, `Postal`) VALUES ('2', '30001', 'Napoleón Bonaparte', '+33 1 79 75 40 00', '40 Rue du Colisée', 'Paris', 'Île-de-France', 'France', '75008');
INSERT INTO `lab_mysql`.`Salesperson` (`ID`, `Staff ID`, `Name`, `Store`) VALUES ('0', '00001', 'Petey Cruiser', 'Madrid');
INSERT INTO `lab_mysql`.`Salesperson` (`ID`, `Staff ID`, `Name`, `Store`) VALUES ('1', '00002', 'Anna Sthesia', 'Barcelona');
INSERT INTO `lab_mysql`.`Salesperson` (`ID`, `Staff ID`, `Name`, `Store`) VALUES ('2', '00003', 'Paul Molive', 'Berlin');
INSERT INTO `lab_mysql`.`Salesperson` (`ID`, `Staff ID`, `Name`, `Store`) VALUES ('3', '00004', 'Gail Forcewind', 'Paris');
INSERT INTO `lab_mysql`.`Salesperson` (`ID`, `Staff ID`, `Name`, `Store`) VALUES ('4', '00005', 'Paige Turner', 'Miami');
INSERT INTO `lab_mysql`.`Salesperson` (`ID`, `Staff ID`, `Name`, `Store`) VALUES ('5', '00006', 'Bob Frapples', 'Mexico City');
INSERT INTO `lab_mysql`.`Salesperson` (`ID`, `Staff ID`, `Name`, `Store`) VALUES ('6', '00007', 'Walter Melon', 'Amsterdam');
INSERT INTO `lab_mysql`.`Salesperson` (`ID`, `Staff ID`, `Name`, `Store`) VALUES ('7', '00008', 'Shonda Leer', 'São Paulo');
ALTER TABLE `lab_mysql`.`Car` 
CHANGE COLUMN `ID` `ID` INT NOT NULL ;
ALTER TABLE `lab_mysql`.`Salesperson` 
CHANGE COLUMN `ID` `ID` INT NOT NULL ;
ALTER TABLE `lab_mysql`.`Invoice` 
DROP FOREIGN KEY `Car`,
DROP FOREIGN KEY `Customer`,
DROP FOREIGN KEY `Sales person`;
ALTER TABLE `lab_mysql`.`Invoice` 
ADD INDEX `Car_idx` (`Car` ASC) VISIBLE,
ADD INDEX `Customer_idx` (`Customer` ASC) VISIBLE,
ADD INDEX `Sales person_idx` (`Sales person` ASC) VISIBLE,
DROP INDEX `Sales person_idx` ,
DROP INDEX `Customer_idx` ,
DROP INDEX `Car_UNIQUE` ;
;
ALTER TABLE `lab_mysql`.`Invoice` 
ADD CONSTRAINT `Car`
  FOREIGN KEY (`Car`)
  REFERENCES `lab_mysql`.`Car` (`ID`)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT,
ADD CONSTRAINT `Customer`
  FOREIGN KEY (`Customer`)
  REFERENCES `lab_mysql`.`Customer` (`ID`),
ADD CONSTRAINT `Sales person`
  FOREIGN KEY (`Sales person`)
  REFERENCES `lab_mysql`.`Salesperson` (`ID`);
  ALTER TABLE `lab_mysql`.`Invoice` 
CHANGE COLUMN `Date` `Date` VARCHAR(10) NOT NULL ;
INSERT INTO `lab_mysql`.`Invoice` (`ID`, `Invoice Number`, `Date`, `Car`, `Customer`, `Sales person`) VALUES ('0', '852399038', '22-08-2018', '0', '1', '3');
INSERT INTO `lab_mysql`.`Invoice` (`ID`, `Invoice Number`, `Date`, `Car`, `Customer`, `Sales person`) VALUES ('1', '731166526', '31-12-2018', '3', '0', '5');
INSERT INTO `lab_mysql`.`Invoice` (`ID`, `Invoice Number`, `Date`, `Car`, `Customer`, `Sales person`) VALUES ('2', '271135104', '22-01-2019', '2', '2', '7');
