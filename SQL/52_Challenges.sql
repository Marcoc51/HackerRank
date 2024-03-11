SELECT 
  h.hacker_id, 
  h.name, 
  COUNT(c.challenge_id) AS Total
INTO #temp
FROM Hackers AS h
INNER JOIN Challenges AS c
ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name;

DECLARE @maxcounts INT = (SELECT MAX(Total) FROM #temp);

SELECT 
  hacker_id, 
  name, 
  Total
FROM #temp
WHERE Total NOT IN (
  SELECT Total 
  FROM #temp
  GROUP BY Total 
  Having Count(Total) > 1 
  AND Total < @maxcounts
)
ORDER BY Total DESC, hacker_id;
