SELECT DISTINCT f1.X, f1.Y
-- Add the ROW_NUMBER() function to generate an ID for the pairs to control it.
FROM (SELECT X, Y, ROW_NUMBER() OVER(ORDER BY X, Y) AS RN FROM Functions) AS f1
INNER JOIN (SELECT X, Y, ROW_NUMBER() OVER(ORDER BY X, Y) AS RN FROM Functions) AS f2
ON f1.X = f2.Y
AND f2.X = f1.Y
AND f1.RN <> f2.RN -- To prevent comparing the pair with itself during the self join, but with the other pairs.
WHERE f1.X <= f1.Y
ORDER BY f1.X;
