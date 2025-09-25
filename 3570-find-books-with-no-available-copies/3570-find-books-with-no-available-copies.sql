select a.book_id,title,author,genre,publication_year,a.total_copies as current_borrowers 
from library_books a join (select book_id,count(book_id) cbi
from borrowing_records
where return_date is NULL
group by book_id) b
on a.book_id = b.book_id
where a.total_copies = b.cbi
order by a.total_copies desc,a.title;