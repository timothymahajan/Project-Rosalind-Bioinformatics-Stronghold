--Problem 20- Calculating Protein Mass
--Given: A protein string PP of length at most 1000 amino acids.
--Return: The total weight of PP. Consult the monoisotopic mass table.

declare @input varchar(max) = 'IKTPQCDLTFRDHSHGQHRFFNTSDGHYFWVCIAPNSCRKCNMIMEGTQANWMMAFNDKFMWVPCIVEHIAEMYIMAGYFAKWHVHWACHCSLECVAMMEVMWELEHQRMGMHVGMGNHTGKAMNLNDLPRTYVRAHQTMFTIWIHKNAPHSYCLFYYASQQLNWCWSDGIAWKYMRMYNYKIMIQPFARNPRLETWQAWLNMRCKYNAKQFDFKWFFMNWPFSYAAHCHNMNLYHVFVWADVGDDAGLILWYTKIMHWKPIHHWTIKGCYFDAWIHSNQDCEALQNFQDGEYRDLFFISTNKMMRNWMWTGAHVTHWVWWCFIEGVAFDWTYYSWLSYWIIFKCYALPTRVMFQIHNVQWKRNLWDNEGTQHHMWHKNHLTGLECAITCNVCATINSVVMDCGNATHCRLIIGDRHWLCQLLECWVMCWRPQTDLFHSRDKGTRRQIKSDKCIWYVHYLEIFRNQKAKWPRYENIVVAQYELLSIMYIFARVWWEGSDECSPKMMTMVHMRVWRSNGYYDWFMTEVTCGNIELCVFMCDPFWWLCEYNSRIPWITPTEGDAQQLYCMDQNWANLIWRVVTSMNLVRADVLINGCCFDKYDPHGITAQTHLWGRNGNQRVPLQLHTWGRCKMEKPDQKDLMPNGDSHLLCHVLQFKFNIKLPHKIANVLMRWHMIQDVRQKTINLIAQKERARECSDSTLHTEGDIVICVKEWKFVQFMRLFKNAMAFYMAFFLFLVQQVMAPEHWHWCNDVYESTPRRFQADYTINLFFYQEWMGGQTTDVALHQRDECYWITSWTEARSWHVEEMAWRRERLIIQNLGEASWNVCVYYYASGADPYMEYLPNHRTADNYRRHGGEYCDHDTTIMCGKAWCWDVPTHEMPQNRRCLCYC';

declare @mass_table varchar(max) =
'A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333
';
declare @mass_table_length int = (len(@mass_table)  - len(replace(@mass_table, ' ', '')))/3;

with 

mass_table_  as
(
select 
	1 as num,
	left(@mass_table, 1) as letter, cast(left(stuff(@mass_table, 1, 4, ''), 
	CHARINDEX(CHAR(13), @mass_table) - 5) as float)  as mass, 
	right(@mass_table, len(@mass_table) - CHARINDEX(CHAR(13), @mass_table) - 1) as leftover
union all 
select 
	num + 1,
	left(leftover, 1), 
	cast(left(stuff(leftover, 1, 4, ''), CHARINDEX(CHAR(13), leftover) - 5) as float), 
	right(leftover, len(leftover) - CHARINDEX(CHAR(13), leftover) - 1) from mass_table_ where num <= @mass_table_length - 1	
),

mass_table as
(
select letter, mass from mass_table_ 
),

numbers as
(
select 1 as num
union all select  num + 1 from numbers where num < 2000
),

final
as
(
select 
substring(@input, numbers.num, 1) as letter, mass
from numbers
left outer join mass_table on substring(@input, numbers.num, 1) = letter
where num <= len(@input)
)

select sum(mass) from final

option(maxrecursion 0)
