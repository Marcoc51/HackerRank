SELECT 
  ROW_NUMBER() OVER(ORDER BY Start_Date) AS RN, 
  Start_Date
INTO #start
FROM Projects
WHERE Start_Date NOT IN (SELECT End_Date FROM Projects);

SELECT 
  ROW_NUMBER() OVER(ORDER BY End_Date) AS RN, 
  End_Date
INTO #end
FROM Projects
WHERE End_Date NOT IN (SELECT Start_Date FROM Projects);

SELECT 
  s.Start_Date, 
  e.End_Date
FROM #start AS s
INNER JOIN #end AS e
ON s.RN = e.RN
ORDER BY DATEDIFF(DAY, s.Start_Date, e.End_Date), s.Start_Date;
