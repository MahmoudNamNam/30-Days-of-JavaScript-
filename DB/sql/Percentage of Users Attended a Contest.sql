SELECT r.contest_id, 
       ROUND(COUNT(r.user_id) * 100.0 / (select count(*) from Users), 2) AS percentage 
FROM Register r 
INNER JOIN Users u ON u.user_id = r.user_id
GROUP BY r.contest_id
order by percentage desc , r.contest_id;
