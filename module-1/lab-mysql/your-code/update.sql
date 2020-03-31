USE lab_mysql;
UPDATE Salespersons SET store = "Miami" WHERE staffID = 00005;
ALTER TABLE Salespersons ADD email varchar(60);
INSERT INTO Salespersons(staffID,name,store,email)
	VALUES (00009,"Pablo Picasso","-","ppicasso@gmail.com"),
    (00010,"Abraham Lincoln","-","lincoln@us.gov"),
    (00011,"Napoleón Bonaparte","-","hola@napoleon.me");
