SELECT 
    c.company_code
  , c.founder
  , COUNT(DISTINCT lm.lead_manager_code)
  , COUNT(DISTINCT sm.senior_manager_code)
  , COUNT(DISTINCT m.manager_code)
  , COUNT(DISTINCT employee_code)
FROM Company c
INNER JOIN Lead_Manager lm
ON c.company_code = lm.company_code
INNER JOIN Senior_Manager sm
ON c.company_code = sm.company_code
AND lm.lead_manager_code = sm.lead_manager_code
INNER JOIN Manager m
ON c.company_code = m.company_code
AND lm.lead_manager_code = m.lead_manager_code
AND sm.senior_manager_code = m.senior_manager_code
INNER JOIN Employee e
ON c.company_code = e.company_code
AND lm.lead_manager_code = e.lead_manager_code
AND sm.senior_manager_code = e.senior_manager_code
AND m.manager_code = e.manager_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code
