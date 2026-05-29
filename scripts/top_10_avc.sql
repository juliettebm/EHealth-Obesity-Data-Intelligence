SELECT TOP 10
    Hospital_Name,
    State,
    City,
    AVG(CAST(Score AS FLOAT)) AS ScoreMoyenAVC,
    SUM(CAST(Sample AS INT)) AS TotalPatientsEvalues
FROM 
    hospitals
WHERE 
    Condition LIKE '%Stroke%'
    -- Grâce à TRY_CAST, on peut directement filtrer sur le chiffre !
    AND TRY_CAST(Sample AS INT) > 100   
    
GROUP BY 
    Hospital_Name, 
    State, 
    City
ORDER BY 
    ScoreMoyenAVC DESC;                  -- 5. On classe du meilleur au moins bon
