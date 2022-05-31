SELECT CASE
        WHEN G.Grade >= 8 AND G.Grade <= 10 THEN S.Name
        ELSE NULL
        END
, G.Grade, S.Marks
FROM Students S, Grades G 
WHERE
S.Marks >= G.Min_Mark AND S.Marks <= G.Max_Mark
ORDER BY 
G.Grade DESC, S.Name ASC;
