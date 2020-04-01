SELECT step2.au_id, sum(tt.advance+tt.royalty)
	FROM step2 
    INNER JOIN titleauthor AS ta
    ON ta.au_id = ta.au_id
	INNER JOIN titles AS tt
	ON ta.title_id = tt.title_id
GROUP BY tt.title_id,step2.au_id