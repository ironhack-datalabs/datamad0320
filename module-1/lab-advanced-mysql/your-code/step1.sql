SELECT 
	tt.title_id,
    ta.au_id,
    round(tt.price * s.qty * tt.royalty / 100 * ta.royaltyper / 100,3) AS sales_royalty
FROM titleauthor AS ta
INNER JOIN titles AS tt
	ON ta.title_id = tt.title_id
INNER JOIN sales AS s
	ON s.title_id = tt.title_id;
    
  