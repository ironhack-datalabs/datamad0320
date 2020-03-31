USE lab_mysql;

CREATE TABLE lab_mysql.Customer(
	idCustomer INT NOT NULL AUTO_INCREMENT, 
    FullName VARCHAR(45),
    Phone_number INT NOT NULL UNIQUE,
    email VARCHAR(45),
    Address VARCHAR(45),
    City VARCHAR(20),
    Province VARCHAR(20),
    Country VARCHAR(20),
    Zip_code int,
    PRIMARY KEY (idCustomer)
    );
	
CREATE TABLE lab_mysql.Car(
	idCar INT NOT NULL AUTO_INCREMENT,
    VIN VARCHAR(45) NOT NULL,
    Manufacturer VARCHAR(45),
    Model VARCHAR(45),
    Fabrication_year INT,
    Color VARCHAR(20),
    PRIMARY KEY (idCar)
    );
  
CREATE TABLE lab_mysql.SalesPerson(
	idSalesPerson INT NOT NULL AUTO_INCREMENT,
    full_name VARCHAR(45),
    Staff_id INT NOT NULL,
    Store VARCHAR(45),
    PRIMARY KEY (idSalesPerson)
    );
    
CREATE TABLE lab_mysql.Invoices(
	idInvoice INT NOT NULL AUTO_INCREMENT,
    invoice_nr INT NOT NULL,
    date_time DATE,
    Amount INT,
    Car_idCar INT UNIQUE NOT NULL,
    SalesPerson_idSalesPerson INT NOT NULL,
    Customer_idCustomer INT NOT NULL,
    PRIMARY KEY (idInvoice),
    FOREIGN KEY (Car_idCar) REFERENCES Car(idCar)
    ON DELETE CASCADE,
    FOREIGN KEY (SalesPerson_idSalesPerson) REFERENCES SalesPerson(idSalesPerson)
    ON DELETE NO ACTION,
    FOREIGN KEY (Customer_idCustomer) REFERENCES Customer(idCustomer)
    ON DELETE NO ACTION
    );
