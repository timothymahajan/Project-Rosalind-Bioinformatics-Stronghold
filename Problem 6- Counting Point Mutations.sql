--Counting Point Mutations (Problem 6)
--Given: Two DNA strings ss and tt of equal length (not exceeding 1 kbp).
--Return: The Hamming distance dH(s,t).

DECLARE @s varchar(max) = 'GAGCCTACTAACGGGAT';
DECLARE @t varchar(max) = 'CATCGTAATGACGGCCT';
with 
data as
(select 1 as num, 0 as dis
union all select num + 1, case when SUBSTRING(@s, num, 1) = SUBSTRING(@t, num, 1) then 0 else 1 end from data where num  <= len(@s)
)
select sum(dis) from data;