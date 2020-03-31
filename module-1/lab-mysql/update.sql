
/*update 1 specific cell*/
UPDATE `lab-mysql`.`Salesperson` SET `store`="Miami" WHERE `ID`=4;


/
/
/


/*update multiple cells (it didn work at all, Idk why...)*/
UPDATE `lab-mysql`.`Customers` SET `email`= case `ID`
when `ID`= 0 then "ppicasso@gmail.com"
when `ID`= 1 then "lincoln@us.gov"
when `ID`= 2 then "hello@napoleon.me"
end
WHERE `ID` in (0,1,2);