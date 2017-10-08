--Problem 5: Computing GC Content
--Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
--Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

declare @input varchar(max) = 
'
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
';

set @input = replace(replace(@input, char(13), ''), char(10), '') + '>';

with 

input_table1 as 
(
select charindex('>', @input, 0) as position, @input as input
union all
select charindex('>', @input, position + 1), @input from input_table1 where position > 0
),

input_table2 as
(
select 
replace(substring(@input, position, charindex('>', @input, position + 1)), '>', '') as input
from input_table1
where input <> ''
),

input_table3 as
(
select  
left(input, 13)  as Name,
right(input, len(input)- 13) as String,
cast(len(replace(replace(right(input, len(input)- 13), 'A', ''), 'T', '')) as float)/len(right(input, len(input)- 13)) as Percentage
from input_table2
where len(input) >= 13
),

input_table4 as
(
select 
Name,
Percentage,
row_number() over (order by Percentage desc) as rn
from input_table3
)

select Name, Percentage*100 from input_table4 where rn = 1

option(maxrecursion 0)
