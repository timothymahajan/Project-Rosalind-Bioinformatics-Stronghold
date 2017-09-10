--Finding a Motif in DNA (Problem 9)
--Given: Two DNA strings ss and tt (each of length at most 1 kbp).
--Return: All locations of tt as a substring of ss.

declare @s varchar(max)  = 'GATATATGCATATACTT';
declare @t varchar(max)  = 'ATAT';
declare @result varchar(max) = '';

with 
data as
(
select 1 as num, case when substring(@s, 1, len(@t)) = @t then 1 else 0 end as pos
union all select num + 1, case when substring(@s, num + 1, len(@t)) = @t then num + 1 else 0 end from data where num + len(@t) <= len(@s)
)

select @result = @result + ' ' + cast(pos as varchar(max)) from data where pos <> 0;
select stuff(@result, 1, 1, '');
