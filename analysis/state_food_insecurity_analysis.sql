</> SQL

-- 1. Test
SELECT * FROM state_data;

-- 2. Highest Food Insecurity
SELECT
	State,
	[Food Insecurity Rate]
FROM state_data
ORDER BY [Food Insecurity Rate] DESC
LIMIT 10;

-- 3. Highest Poverty
SELECT
	State,
	[Poverty Rate]
FROM state_data
ORDER BY [Poverty Rate] DESC
LIMIT 10;

-- 4. Participation vs Need
SELECT
	State,
	[Food Insecurity Rate],
	[SNAP Participants]
FROM state_data
ORDER BY [Food Insecurity Rate] DESC;

-- 5. SNAP Benefits vs Food Insecurity
SELECT
	State,
	[Food Insecurity Rate],
	[SNAP Benefits]
FROM state_data
ORDER BY [Food Insecurity Rate] DESC;

-- 6. Combined View (Key Analysis)
SELECT
	State,
	[Food Insecurity Rate],
	[Poverty Rate],
	[SNAP Participants]
FROM state_data
ORDER BY [Food Insecurity Rate] DESC;
