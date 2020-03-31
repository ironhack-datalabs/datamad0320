SELECT * FROM LAB.Cars;
INSERT INTO `LAB`.`Cars` (`VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES ('3K096I98581DHSNUP', 'Volkswagen', 'Tiguan', '2019', 'Blue');
INSERT INTO `LAB`.`Cars` (`VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES ('ZM8G7BEUQZ97IH46V','Peugeot','Rifter','2019','Red');
INSERT INTO `LAB`.`Cars` (`VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES ('RKXVNNIHLVVZOUB4M','Ford','Fusion','2018','White');
INSERT INTO `LAB`.`Cars` (`VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES ('HKNDGS7CU31E9Z7JW','Toyota','RAV4','2018','Silver');
INSERT INTO `LAB`.`Cars` (`VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES ('DAM41UDN3CHU2WVF6','Volvo','V60','2019', 'Gray');
INSERT INTO `LAB`.`Cars` (`VIN`, `Manufacturer`, `Model`, `Year`, `Color`) VALUES ('DAM41UDN3CHU2WVF6','Volvo','V60 Cross Country','2019','Gray');

SELECT * FROM LAB.Customers;
INSERT INTO `LAB`.`Customers` (`Customer ID`, `Name`, `Phone`, `Email`, `Address`, `City`, `State/Province`, `Country`, `Postal`) VALUES ('10001', 'Pablo Picasso', '+34 636 17 63 82','-',  'Paseo de la Chopera, 14', 'Madrid', 'Madrid', 'Spain', '28045');
INSERT INTO `LAB`.`Customers` (`Customer ID`, `Name`,`Phone` ,`Email`, `Address`, `City`, `State/Province`, `Country`, `Postal`) VALUES ('20001', 'Abraham Lincoln', '+1 305 907 7086','-',  '120 SW 8th St', 'Miami', 'Florida', 'United States', '33130');
INSERT INTO `LAB`.`Customers` (`Customer ID`, `Name`, `Phone`,`Email`, `Address`, `City`, `State/Province`, `Country`, `Postal`) VALUES ('30001', 'Napoléon Bonaparte', '+33 1 79 75 40 00','-',  '40 Rue du Colisée', 'Paris', 'Île-de-France', 'France', '75008');

SELECT * FROM LAB.Salespersons;
INSERT INTO `LAB`.`Salespersons` (`Staff ID`, `Name`, `Store`) VALUES ('0001', 'Petey Cruiser', 'Madrid');
INSERT INTO `LAB`.`Salespersons` (`Staff ID`, `Name`, `Store`) VALUES ('0002', 'Anna Sthesia', 'Barcelona');
INSERT INTO `LAB`.`Salespersons` (`Staff ID`, `Name`, `Store`) VALUES ('0003', 'Paul Molive', 'Berlin');
INSERT INTO `LAB`.`Salespersons` (`Staff ID`, `Name`, `Store`) VALUES ('0004', 'Gail Forcewind', 'Paris');
INSERT INTO `LAB`.`Salespersons` (`Staff ID`, `Name`, `Store`) VALUES ('0005', 'Paige Turner', 'Mimia');
INSERT INTO `LAB`.`Salespersons` (`Staff ID`, `Name`, `Store`) VALUES ('0006', 'Bob Frapples', 'Mexico City');
INSERT INTO `LAB`.`Salespersons` (`Staff ID`, `Name`, `Store`) VALUES ('0007', 'Walter Melon', 'Amsterdam');
INSERT INTO `LAB`.`Salespersons` (`Staff ID`, `Name`, `Store`) VALUES ('0008', 'Shonda Leer', 'São Paulo');

SELECT * FROM LAB.Invoices;
INSERT INTO `LAB`.`Invoices` (`Invoice Number`, `Date`, `Car`, `Customer`, `Sales Person`) VALUES ('852399038', '22-08-2018', '3K096I98581DHSNUP', '20001', '00004');
INSERT INTO `LAB`.`Invoices` (`Invoice Number`, `Date`, `Car`, `Customer`, `Sales Person`) VALUES ('731166526', '31-12-2018', 'HKNDGS7CU31E9Z7JW', '10001', '00006');
INSERT INTO `LAB`.`Invoices` (`Invoice Number`, `Date`, `Car`, `Customer`, `Sales Person`) VALUES ('271135104', '22-01-2019', 'RKXVNNIHLVVZOUB4M', '30001', '00008');