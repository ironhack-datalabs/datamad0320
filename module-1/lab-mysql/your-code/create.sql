# Create table one by one
CREATE SCHEMA `lab-mysql` ;

CREATE TABLE `lab-mysql`.`cars` (
  `VIN` CHAR(17) NOT NULL,
  `manufacturer` TINYTEXT NULL,
  `model` VARCHAR(45) NULL,
  `year` INT NULL, 
  `color` TINYTEXT NULL,
  PRIMARY KEY (`VIN`));
  
CREATE TABLE `lab-mysql`.`customers` (
  `idcustomers` INT(5) NOT NULL,
  `customername` TINYTEXT NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `email` VARCHAR(45) NULL,
  `address` TINYTEXT NOT NULL,
  `city` TINYTEXT NOT NULL,
  `state/province` TINYTEXT NOT NULL,
  `country` TINYTEXT NOT NULL,
  `ZIP` VARCHAR(5) NULL,
  PRIMARY KEY (`idcustomers`));
    
CREATE TABLE `lab-mysql`.`invoices` (
  `invoicenumber` INT(9) NOT NULL,
  `date` DATE NOT NULL,
  `car` INT(11) NOT NULL,
  `customers` INT NOT NULL,
  `salesman` INT NOT NULL,
  PRIMARY KEY (`invoicenumber`));
  
CREATE TABLE `lab-mysql`.`salespersons` (
  `idstaff` CHAR(5) NOT NULL,
  `staffname` TINYTEXT NOT NULL,
  `store` TINYTEXT NOT NULL,
  PRIMARY KEY (`idstaff`));