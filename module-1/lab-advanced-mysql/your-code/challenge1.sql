CREATE TEMPORARY TABLE step_1
SELECT 
	titles.title_id,
    titleauthor.au_id,
    (titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) AS sales_royalty
FROM titleauthor
INNER JOIN titles
	ON titleauthor.title_id = titles.title_id
INNER JOIN sales
	ON sales.title_id = titles.title_id;


CREATE TEMPORARY TABLE step_2
SELECT
	title_id,
    au_id,
    SUM(sales_royalty) as au_title_royalty
FROM step_1
GROUP BY title_id, au_id;


SELECT
	step_2.au_id AS 'AUTHOR ID',
    ROUND(SUM(step_2.au_title_royalty + titles.advance),2) AS 'PROFITS'
FROM step_2
INNER JOIN titles
	ON titles.title_id = step_2.title_id
GROUP BY titles.title_id, step_2.au_id
ORDER BY SUM(step_2.au_title_royalty + titles.advance) desc
LIMIT 3;


