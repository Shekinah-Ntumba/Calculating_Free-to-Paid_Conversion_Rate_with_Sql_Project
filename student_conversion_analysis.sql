CREATE DATABASE db_course_conversions;
USE db_course_conversions;
CREATE DATABASE db_course_conversions;
USE db_course_conversions;
describe `student_engagement`;
describe `student_info`;
describe `student_purchases`;

select 
i.student_id,
i.date_registered,
MIN(e.date_watched) AS first_date_watched,
min(p.date_purchased) AS first_date_purchased,
datediff(MIN(e.date_watched), i.date_registered) AS days_diff_reg_watch,
datediff(min(p.date_purchased), MIN(e.date_watched)) AS days_diff_watch_purch
from student_engagement e
join student_info i on e.student_id = i.student_id
join student_purchases p on i.student_id = p.student_id
group by i.student_id, i.date_registered
having min(e.date_watched) <=min(p.date_purchased);

SELECT COUNT(*) as total_students
FROM (
select 
i.student_id,
i.date_registered,
MIN(e.date_watched) AS first_date_watched,
min(p.date_purchased) AS first_date_purchased,
datediff(MIN(e.date_watched), i.date_registered) AS days_diff_reg_watch,
datediff(min(p.date_purchased), MIN(e.date_watched)) AS days_diff_watch_purch
from student_engagement e
join student_info i on e.student_id = i.student_id
join student_purchases p on i.student_id = p.student_id
group by i.student_id, i.date_registered
HAVING first_date_watched <= first_date_purchased
) as subquery;

select 
i.student_id,
i.date_registered,
MIN(e.date_watched) AS first_date_watched,
min(p.date_purchased) AS first_date_purchased,
datediff(MIN(e.date_watched), i.date_registered) AS days_diff_reg_watch,
datediff(min(p.date_purchased), MIN(e.date_watched)) AS days_diff_watch_purch
from student_engagement e
join student_info i on e.student_id = i.student_id
join student_purchases p on i.student_id = p.student_id
group by i.student_id, i.date_registered
HAVING first_date_watched <= first_date_purchased;
select
round(
     (count(distinct case when first_date_watched<= first_date_purchased then student_id end)*100.0)/(SELECT COUNT(DISTINCT student_id) 
         FROM student_engagement), 2) as conversion_rate,
round(
   avg(days_diff_reg_watch),2
) as av_reg_watch,
round(avg(days_diff_watch_purch),2
) as av_watch_purch
from(
select 
i.student_id,
i.date_registered,
MIN(e.date_watched) AS first_date_watched,
min(p.date_purchased) AS first_date_purchased,
datediff(MIN(e.date_watched), i.date_registered) AS days_diff_reg_watch,
datediff(min(p.date_purchased), MIN(e.date_watched)) AS days_diff_watch_purch
from student_engagement e
join student_info i on e.student_id = i.student_id
join student_purchases p on i.student_id = p.student_id
group by i.student_id, i.date_registered
HAVING first_date_watched <= first_date_purchased
) as subquery;

