WITH minWands (W_age, W_coins, W_power)
AS
(
select p.age, min(w.coins_needed), W.power from Wands W INNER JOIN Wands_Property P ON W.code = P.code WHERE P.is_evil = 0 GROUP BY P.age, W.power
)

SELECT W.id, P.age, W.coins_needed, W.power 
FROM Wands W INNER JOIN Wands_Property P ON W.code = P.code
WHERE 
CONCAT(P.age, W.coins_needed, W.power) in 
(SELECT CONCAT(W_age, W_coins, W_power) FROM minWands)
ORDER BY W.power DESC, P.age DESC;
