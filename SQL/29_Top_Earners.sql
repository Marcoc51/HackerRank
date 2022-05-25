SELECT TOP 1 (salary * months), COUNT((salary * months)) FROM Employee GROUP BY (salary * months) ORDER BY 1 DESC;
