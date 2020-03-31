INSERT INTO lab_mysql.Customer(FullName, Phone_number, Address, City, Province, Country, Zip_code)
VALUES ('David', '9321654', 'C/los suspiros', 'Orce', 'Graná', 'espain', '3215'),
		('Pepe', '9586225', 'C/pepones', 'Madrid', 'Madrid', 'Alemania', '2589'),
        ('María',  '9862564', 'c/las tres marias', 'Maria', 'Almeria', 'espain', '3657');

INSERT INTO lab_mysql.Car(VIN, Manufacturer, Model, Fabrication_year, Color)
VALUES ('9874JLS', 'Fiat', 'Punto', '2006', 'Gray'),
		('5891KFS', 'Subaru', 'Justy', '2002', 'Blue'),
        ('1367ADE', 'Nissan', 'X-trail', '2006', 'Black'),
        ('1367ADE', 'Kia', 'Carens', '2016', 'Gray');

INSERT INTO lab_mysql.SalesPerson(Staff_id, full_name, Store)
VALUES ('1', 'Pedro Vendemotos', 'La Cacharreria'),
		('2', 'Vendehumos Joe', 'El despropósito');

INSERT INTO lab_mysql.Invoices(Invoice_nr, date_time, Amount, Car_idCar, SalesPerson_idSalesPerson, Customer_idCustomer)
VALUES ('101', '2020-01-03', '8000', '1', '1', '2'),
		('102', '2019-12-05', '12000', '2', '2', '3'),
        ('103', '2019-11-05', '20000', '3', '1', '1'),
        ('104', '2020-03-20', '17000', '4', '1', '3');