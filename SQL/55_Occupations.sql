SELECT 
    ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS RN, 
    Name, 
    Occupation
INTO #temp
FROM occupations;

SELECT [Doctor], [Professor], [Singer], [Actor]
FROM #temp
PIVOT (
  MIN(Name)
  FOR [Occupation]
  IN (
    [Doctor],
    [Professor],
    [Singer],
    [Actor]
  )
) AS PivotTable


/*
ID  Name Occupation -->        Doctor  Professor Singer  Actor
1    a     Doctor              a       b         c       d
2    b     Actor
3    c     Professor
4    d     Singer
*/
