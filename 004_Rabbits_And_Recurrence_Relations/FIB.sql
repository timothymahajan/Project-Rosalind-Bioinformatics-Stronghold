--Rabbits and Recurrence Relations (Problem 4)
--Given: Positive integers n <= 40 and k <= 5.
--Return: The total number of rabbit pairs that will be present after nn months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of kk rabbit pairs (instead of only 1 pair).

declare @k int = 2;
declare @n int = 30;
WITH Data AS
(
SELECT 1 AS m, 1 as bom, 1 as eom
UNION ALL SELECT m+1, eom, eom + bom*@k FROM Data WHERE m < @n
)
SELECT * FROM Data
