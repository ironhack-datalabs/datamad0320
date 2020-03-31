CREATE DATABASE lab_mysql;
USE lab_mysql;
CREATE TABLE lab_mysql.Car (VIN VARCHAR(20), Manufacturer VARCHAR(20), Model VARCHAR(20), `Year` DATE, Color VARCHAR(10));
CREATE TABLE lab_mysql.Customer (`Customer ID` INT, `Name` VARCHAR(40), `Phone` VARCHAR(15), `Email` VARCHAR(40), `Address` VARCHAR(250), `City` VARCHAR(20), `State/Province` VARCHAR(20), `Postal` INT);
CREATE TABLE lab_mysql.Salesperson (`Staff ID` INT, `Name` VARCHAR(40), Store VARCHAR(20));
CREATE TABLE lab_mysql.Invoice (`Invoice Number` INT, `Date` DATE, Car INT, Customer INT, `Sales person` INT);
ALTER TABLE `lab_mysql`.`Car` 
ADD COLUMN `idCar` VARCHAR(45) NOT NULL AFTER `Color`,
CHANGE COLUMN `VIN` `VIN` VARCHAR(20) NOT NULL ,
CHANGE COLUMN `Manufacturer` `Manufacturer` VARCHAR(20) NOT NULL ,
CHANGE COLUMN `Model` `Model` VARCHAR(20) NOT NULL ,
CHANGE COLUMN `Year` `Year` DATE NOT NULL ,
CHANGE COLUMN `Color` `Color` VARCHAR(10) NOT NULL ,
ADD PRIMARY KEY (`idCar`);
;
ALTER TABLE `lab_mysql`.`Car` 
ADD UNIQUE INDEX `VIN_UNIQUE` (`VIN` ASC) VISIBLE;
;
ALTER TABLE `lab_mysql`.`Car` 
CHANGE COLUMN `idCar` `idCar` VARCHAR(45) NOT NULL FIRST;
ALTER TABLE `lab_mysql`.`Customer` 
ADD COLUMN `ID` INT NOT NULL FIRST,
ADD COLUMN `Country` VARCHAR(45) NOT NULL AFTER `State/Province`,
CHANGE COLUMN `Customer ID` `Customer ID` INT NOT NULL ,
CHANGE COLUMN `Name` `Name` VARCHAR(40) NOT NULL ,
CHANGE COLUMN `Phone` `Phone` VARCHAR(15) NOT NULL ,
CHANGE COLUMN `Address` `Address` VARCHAR(250) NOT NULL ,
CHANGE COLUMN `City` `City` VARCHAR(20) NOT NULL ,
CHANGE COLUMN `State/Province` `State/Province` VARCHAR(45) NOT NULL ,
CHANGE COLUMN `Postal` `Postal` INT NOT NULL ,
ADD PRIMARY KEY (`ID`),
ADD UNIQUE INDEX `Customer ID_UNIQUE` (`Customer ID` ASC) VISIBLE;
;
ALTER TABLE `lab_mysql`.`Car` 
CHANGE COLUMN `idCar` `ID` VARCHAR(45) NOT NULL ;
ALTER TABLE `lab_mysql`.`Salesperson` 
ADD COLUMN `ID` VARCHAR(45) NOT NULL FIRST,
CHANGE COLUMN `Staff ID` `Staff ID` INT NOT NULL ,
CHANGE COLUMN `Name` `Name` VARCHAR(40) NOT NULL ,
CHANGE COLUMN `Store` `Store` VARCHAR(20) NOT NULL ,
ADD PRIMARY KEY (`ID`),
ADD UNIQUE INDEX `Staff ID_UNIQUE` (`Staff ID` ASC) VISIBLE;
;
ALTER TABLE `lab_mysql`.`Invoice` 
ADD COLUMN `ID` INT NOT NULL FIRST,
CHANGE COLUMN `Invoice Number` `Invoice Number` INT NOT NULL ,
CHANGE COLUMN `Date` `Date` DATE NOT NULL ,
CHANGE COLUMN `Car` `Car` INT NOT NULL ,
CHANGE COLUMN `Customer` `Customer` INT NOT NULL ,
CHANGE COLUMN `Sales person` `Sales person` INT NOT NULL ,
ADD PRIMARY KEY (`ID`),
ADD UNIQUE INDEX `Invoice Number_UNIQUE` (`Invoice Number` ASC) VISIBLE,
ADD UNIQUE INDEX `Car_UNIQUE` (`Car` ASC) VISIBLE;
;
ALTER TABLE `lab_mysql`.`Invoice` 
ADD CONSTRAINT `Car`
  FOREIGN KEY (`Car`)
  REFERENCES `lab_mysql`.`Invoice` (`ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
ALTER TABLE `lab_mysql`.`Invoice` 
ADD INDEX `Customer_idx` (`Customer` ASC) VISIBLE;
;
ALTER TABLE `lab_mysql`.`Invoice` 
ADD CONSTRAINT `Customer`
  FOREIGN KEY (`Customer`)
  REFERENCES `lab_mysql`.`Invoice` (`ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
ALTER TABLE `lab_mysql`.`Invoice` 
ADD INDEX `Sales person_idx` (`Sales person` ASC) VISIBLE;
;
ALTER TABLE `lab_mysql`.`Invoice` 
ADD CONSTRAINT `Sales person`
  FOREIGN KEY (`Sales person`)
  REFERENCES `lab_mysql`.`Invoice` (`ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
