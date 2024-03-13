DECLARE @res VARCHAR(MAX) = '2';
DECLARE @outerCounter INT = 3;

WHILE @outerCounter <= 1000
BEGIN
    DECLARE @prime INT = 1;
    DECLARE @innerCounter INT = 2;
    WHILE @innerCounter < @outerCounter
    BEGIN
        IF (@outerCounter % @innerCounter = 0)
        BEGIN
            SET @prime = 0;
            BREAK;
        END
        SET @innerCounter += 1
    END
    IF (@prime = 1)
    BEGIN
        SET @res = @res + '&' + CONVERT(VARCHAR, @outerCounter);
    END
    SET @outerCounter += 1;
END

PRINT @res;
