--Given: A collection of kk (k <= 100 <= 100) DNA strings of length at most 1 kbp each in FASTA format.
--Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

declare @input varchar(max) = 
'
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
';

set @input = replace(replace(@input, char(13), ''), char(10), '');
set @input = 
REPLACE
(REPLACE
(REPLACE
(REPLACE
(REPLACE
(REPLACE
(REPLACE
(REPLACE
(REPLACE
(REPLACE(@input, '0', ''),
'1', ''),
'2', ''),
'3', ''),
'4', ''),
'5', ''),
'6', ''),
'7', ''),
'8', ''),
'9', '');
set @input = stuff(replace(@input, '>Rosalind_', '@'), 1, 1, '') + '@';



with 

input_table as
(
select
	1 as num, 
	left(@input, CHARINDEX('@', @input) - 1) as word,
	stuff(@input, 1, CHARINDEX('@', @input), '') as leftover
union all select 
	num + 1, 
	left(leftover, CHARINDEX('@', leftover) - 1) as word,
	stuff(leftover, 1, CHARINDEX('@', leftover), '') as leftover
	from input_table where num < len(@input) - len(replace(@input, '@', ''))
),

clean_input_table as
(
select replace(word, char(13), '') as word from input_table
),

one_word as
(
select top 1 word from clean_input_table order by word
),

numbers as
(
select 1 as num
union all select num + 1 from numbers where num < len((select word from one_word))
),

possible_substrings as
(
select distinct
SUBSTRING((select word from one_word), n1.num, n2.num - n1.num + 1) as subs
from numbers n1 
cross join numbers n2
where n1.num <= n2.num
),

data as
(select 
clean_input_table.word,
possible_substrings.subs,
case when CHARINDEX(possible_substrings.subs, clean_input_table.word) > 0 then 1 else 0 end as is_substring
from clean_input_table
cross join possible_substrings
), 

final as
(
select 
subs,
sum(is_substring) as cnt
from data
group by subs
)

select top 1
subs
from final
where cnt = (select count(word) from clean_input_table)
order by len(subs) desc


option(maxrecursion 0)
