create database studentDB;
use studentDB;
create table Enrollments(
    student_id int PRIMARY KEY,
    course_id int PRIMARY KEY,
    grade int
);
insert into Enrollments (student_id, course_id, grade)
VALUES
(2,2,95),
(2,3,95),
(1,1,90),
(1,2,99),
(3,1,80),
(3,2,75),
(3,3,82);
--answer here
-- Top N per Group
with rankedEnrollment as (
    select *
    row_number() over (
        partition by student_id
        order by grade desc, course_id asc
    ) as rn
    from Enrollments
)
select * 
from rankedEnrollment
where rn = 1
order by student_id
-- three commonly used window function 
-- RANK, ROW_NUMBER & DENSE_RANK
-- given dataset ->
-- Student	Score
-- A	    100
-- B	    90
-- C	    90
-- D	    80
-- E	    70
-- SELECT
--     Student,
--     Score,
--     ROW_NUMBER() OVER (ORDER BY Score DESC) AS row_num,
--     RANK() OVER (ORDER BY Score DESC) AS rank_num,
--     DENSE_RANK() OVER (ORDER BY Score DESC) AS dense_rank_num
-- FROM Students;
-- Student	Score	ROW_NUMBER()	RANK()	DENSE_RANK()
-- A	    100	        1	        1	        1
-- B	    90	        2	        2	        2
-- C	    90	        3	        2	        2
-- D	    80	        4	        4	        3
-- E	    70	        5	        5	        4
-- ROW_NUMBER = Unique numbering.
-- RANK = Same rank for ties, skips numbers.
-- DENSE_RANK = Same rank for ties, no skipped numbers.