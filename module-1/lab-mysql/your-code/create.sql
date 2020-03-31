-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


-- -----------------------------------------------------
-- Schema LAB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `LAB` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `LAB` ;

-- -----------------------------------------------------
-- Table `LAB`.`Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LAB`.`Cars` (
  `VIN` VARCHAR(45) NOT NULL,
  `Manufacturer` VARCHAR(45) NOT NULL,
  `Model` VARCHAR(45) NOT NULL,
  `Year` INT NOT NULL,
  `Color` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`VIN`, `Manufacturer`, `Model`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LAB`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LAB`.`Customers` (
  `Customer ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Phone` VARCHAR(45) NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(45) NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `State/Province` VARCHAR(45) NOT NULL,
  `Country` VARCHAR(45) NOT NULL,
  `Postal` INT NOT NULL,
  PRIMARY KEY (`Customer ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LAB`.`Salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LAB`.`Salespersons` (
  `Staff ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Store` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Staff ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LAB`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LAB`.`Invoices` (
  `Invoice Number` INT NOT NULL,
  `Date` VARCHAR(45) NOT NULL,
  `Car` VARCHAR(45) NOT NULL,
  `Customer` INT NOT NULL,
  `Sales Person` INT NOT NULL,
  PRIMARY KEY (`Invoice Number`),
  INDEX `fk_Invoices_Cars1_idx` (`Car` ASC) VISIBLE,
  INDEX `fk_Invoices_Customers1_idx` (`Customer` ASC) VISIBLE,
  INDEX `fk_Invoices_Salespersons1_idx` (`Sales Person` ASC) VISIBLE,
  CONSTRAINT `fk_Invoices_Cars1`
    FOREIGN KEY (`Car`)
    REFERENCES `LAB`.`Cars` (`VIN`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Customers1`
    FOREIGN KEY (`Customer`)
    REFERENCES `LAB`.`Customers` (`Customer ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Salespersons1`
    FOREIGN KEY (`Sales Person`)
    REFERENCES `LAB`.`Salespersons` (`Staff ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
