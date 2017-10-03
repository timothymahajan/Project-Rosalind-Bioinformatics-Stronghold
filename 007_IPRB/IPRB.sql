--Mendel's First Law (Problem 7)
--Given: Three positive integers kk, mm, and nn, representing a population containing k+m+nk+m+n organisms: kk individuals are homozygous dominant for a factor, mm are heterozygous, and nn are homozygous recessive.
--Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

declare @k int = 2; --homozygous dominant
declare @m int = 2; --heterozygous
declare @n int = 2; --homozygous recessive
declare @pop int = @k + @m + @n;
--let's denote first mate A and second mate B
select	
	cast(@k as float)/@pop													--A is homozygous dominant 
	+ cast(@m as float)/@pop * 0.5											--A is heterozygous, passes dominant allele
	+ cast(@m as float)/@pop * 0.5 * cast(@k as float)/(@pop - 1)			--A is heterozygous, passes recessive allele, B is homozygous dominant
	+ cast(@m as float)/@pop * 0.5 * cast(@m - 1 as float)/(@pop - 1) * 0.5	--A is heterozygous, passes recessive allele, B is heterozygous, passes dominant allele
	+ cast(@n as float)/@pop * cast(@k as float)/(@pop - 1)					--A is homozygous resessive, B is homozygous dominant
	+ cast(@n as float)/@pop * cast(@m as float)/(@pop - 1) * 0.5			--A is homozygous resessive, B is heterozygous, passes dominant allele
