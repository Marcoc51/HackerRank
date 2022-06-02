SELECT S.hacker_id, H.name, SUM(S.scr) 
FROM Hackers H 
INNER JOIN 
(SELECT hacker_id, MAX(score) as scr FROM Submissions GROUP BY hacker_id, challenge_id) S 
ON H.hacker_id = S.hacker_id
GROUP BY S.hacker_id, H.name
HAVING SUM(S.scr) > 0
ORDER BY 3 DESC, 1 ASC;
