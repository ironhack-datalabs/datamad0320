USE lab_mysql;

CREATE TABLE lab_mysql.Cars (
  `VIN` VARCHAR(45) NOT NULL, 
  `manufacturer` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` INT NOT NULL,
  `color` VARCHAR(45) NOT NULL
);
CREATE TABLE lab_mysql.Customers (
  `idCustomers` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `phoneNumber` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state_province` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `zip_postalCode` INT NULL,
  PRIMARY KEY (`idCustomers`));

CREATE TABLE lab_mysql.Salespersons (
  `staffID` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `store` VARCHAR(45) NOT NULL,
PRIMARY KEY (`staffID`));

CREATE TABLE lab_mysql.Invoices (
  `invoiceNumber` INT NOT NULL,
  `date` VARCHAR(45) NOT NULL,
  `car` VARCHAR(45) NOT NULL,
  `customer`  VARCHAR(45) NOT NULL,
  `salesperson` VARCHAR(45) NOT NULL
  );