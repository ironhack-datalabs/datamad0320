UPDATE SalesPerson 
SET Store = REPLACE(Store, 'El despropósito', 'EL Despropósito') 
WHERE full_name = '2';

UPDATE Customer
SET email = CASE 
				WHEN FullName = 'David' THEN 'david"david'
				WHEN FullName = 'Pepe' THEN 'pepe@pepe'
				WHEN FullName = 'Maria' THEN 'maria@maria'
			END;