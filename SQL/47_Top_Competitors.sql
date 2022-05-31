SELECT H.hacker_id, H.name 
FROM Hackers H INNER JOIN Submissions S ON H.hacker_id = S.hacker_id
INNER JOIN Challenges C ON S.challenge_id = C.challenge_id
INNER JOIN Difficulty D ON C.difficulty_level = D.difficulty_level
WHERE D.score = S.score
GROUP BY H.hacker_id, H.name HAVING COUNT(S.submission_id) > 1
ORDER BY COUNT(S.submission_id) DESC, H.hacker_id ASC;
