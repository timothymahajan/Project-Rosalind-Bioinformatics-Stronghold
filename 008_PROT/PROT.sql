--Translating RNA into Protein (Problem 8)
--Given: An RNA string ss corresponding to a strand of mRNA (of length at most 10 kbp).
--Return: The protein string encoded by ss.

declare @s varchar(max) = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA';
declare @result varchar(max) = '';
with 
codon as
(
select 'UUU' as codon, 'F' as amino     
union all select 'CUU', 'L'      
union all select 'AUU', 'I'
union all select 'GUU', 'V'
union all select 'UUC', 'F'
union all select 'CUC', 'L'      
union all select 'AUC', 'I'      
union all select 'GUC', 'V'
union all select 'UUA', 'L'      
union all select 'CUA', 'L'      
union all select 'AUA', 'I'      
union all select 'GUA', 'V'
union all select 'UUG', 'L'      
union all select 'CUG', 'L'      
union all select 'AUG', 'M'      
union all select 'GUG', 'V'
union all select 'UCU', 'S'      
union all select 'CCU', 'P'     
union all select 'ACU', 'T'      
union all select 'GCU', 'A'
union all select 'UCC', 'S'      
union all select 'CCC', 'P'      
union all select 'ACC', 'T'      
union all select 'GCC', 'A'
union all select 'UCA', 'S'      
union all select 'CCA', 'P'      
union all select 'ACA', 'T'      
union all select 'GCA', 'A'
union all select 'UCG', 'S'      
union all select 'CCG', 'P'      
union all select 'ACG', 'T'      
union all select 'GCG', 'A'
union all select 'UAU', 'Y'    
union all select 'CAU', 'H'      
union all select 'AAU', 'N'      
union all select 'GAU', 'D'
union all select 'UAC', 'Y'      
union all select 'CAC', 'H'      
union all select 'AAC', 'N'     
union all select 'GAC', 'D'
union all select 'UAA', 'Stop'   
union all select 'CAA', 'Q'      
union all select 'AAA', 'K'      
union all select 'GAA', 'E'
union all select 'UAG', 'Stop'   
union all select 'CAG', 'Q'      
union all select 'AAG', 'K'      
union all select 'GAG', 'E'
union all select 'UGU', 'C'   
union all select 'CGU', 'R'      
union all select 'AGU', 'S'      
union all select 'GGU', 'G'
union all select 'UGC', 'C'    
union all select 'CGC', 'R'      
union all select 'AGC', 'S'      
union all select 'GGC', 'G'
union all select 'UGA', 'Stop'   
union all select 'CGA', 'R'      
union all select 'AGA', 'R'      
union all select 'GGA', 'G'
union all select 'UGG', 'W'      
union all select 'CGG', 'R'     
union all select 'AGG', 'R'      
union all select 'GGG', 'G'
),

data as
(
select @s as data, case when len(@s)  >= 3 then SUBSTRING(@s, 1, 3) else '' end as codon, right(@s, len(@s)  - 3) as leftover
union all select leftover, case when len(leftover)  >= 3 then SUBSTRING(leftover, 1, 3) else '' end, right(leftover, len(leftover)  - 3) from data where len(leftover) >= 3
),

translated_data as
(
select coalesce(codon.amino, '') as amino
from data
left outer join codon on data.codon = codon.codon
)

select @result = @result + amino from translated_data;
select LEFT(@result, case when CHARINDEX('Stop', @result) > 0 then CHARINDEX('Stop', @result) else len(@result) end);
