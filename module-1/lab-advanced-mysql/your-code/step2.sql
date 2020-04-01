CREATE TEMPORARY TABLE  step2(
SELECT step1.title_id,step1.au_id,round(sum(sales_royalty),2) 
FROM step1
GROUP BY step1.title_id,step1.au_id
);

