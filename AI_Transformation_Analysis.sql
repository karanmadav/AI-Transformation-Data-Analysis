CREATE DATABASE ai_workforce_project;
USE ai_workforce_project;
CREATE TABLE ai_workforce (
    Occupation_Code VARCHAR(20),
    Occupation_Title VARCHAR(255),
    Employment_2024 FLOAT,
    Employment_2034 FLOAT,
    Job_Change FLOAT,
    Growth_Percent FLOAT,
    Annual_Openings FLOAT,
    Median_Wage FLOAT,
    Education VARCHAR(255),
    Automation_Risk_Score FLOAT,
    Career_Resilience_Score FLOAT,
    Economic_Value FLOAT,
    Reskilling_Emergency_Index FLOAT
);

#Checking Dataset Uploaded or Not
SELECT *
FROM ai_workforce_final_dataset;

#Counting Rows
SELECT COUNT(*)
FROM ai_workforce_final_dataset;

#Top 10 Automation Risk Occupations
SELECT
Occupation_Title,
Automation_Risk_Score
FROM ai_workforce_final_dataset
ORDER BY Automation_Risk_Score DESC
LIMIT 10;

#Highest Paying Occupations
SELECT
Occupation_Title,
Median_Wage
FROM ai_workforce_final_dataset
ORDER BY Median_Wage DESC
LIMIT 10;

#Future-Proof Careers
SELECT
Occupation_Title,
Career_Resilience_Score
FROM ai_workforce_final_dataset
ORDER BY Career_Resilience_Score DESC
LIMIT 10;

#Highest Reskilling Need
SELECT
Occupation_Title,
Reskilling_Emergency_Index
FROM ai_workforce_final_dataset
ORDER BY Reskilling_Emergency_Index DESC
LIMIT 10;

#Average Salary By Education
SELECT
Education,
ROUND(AVG(Median_Wage),2) AS Avg_Salary
FROM ai_workforce_final_dataset
GROUP BY Education
ORDER BY Avg_Salary DESC;

#Occupations Growing Fastest
SELECT
Occupation_Title,
Growth_Percent
FROM ai_workforce_final_dataset
ORDER BY Growth_Percent DESC
LIMIT 10;

#Occupations Declining Most
SELECT
Occupation_Title,
Growth_Percent
FROM ai_workforce_final_dataset
ORDER BY Growth_Percent ASC
LIMIT 10;

#High Salary + High Growth
SELECT
Occupation_Title,
Median_Wage,
Growth_Percent
FROM ai_workforce_final_dataset
WHERE Median_Wage > 100000
AND Growth_Percent > 10
ORDER BY Growth_Percent DESC;

#Workforce Impact
SELECT
SUM(Employment_2024) AS Current_Workforce,
SUM(Employment_2034) AS Future_Workforce
FROM ai_workforce_final_dataset;

#Top Economic Value Occupations
SELECT
Occupation_Title,
Economic_Value
FROM ai_workforce_final_dataset
ORDER BY Economic_Value DESC
LIMIT 10;

#Rank Occupations By Salary
SELECT
Occupation_Title,
Median_Wage,
RANK() OVER(
ORDER BY Median_Wage DESC
) AS Salary_Rank
FROM ai_workforce_final_dataset;

#Top Occupation In Each Education Group
SELECT *
FROM
(
SELECT
Education,
Occupation_Title,
Median_Wage,
ROW_NUMBER() OVER(
PARTITION BY Education
ORDER BY Median_Wage DESC
) AS rn
FROM ai_workforce_final_dataset
) x
WHERE rn = 1;

#Create AI Risk Category
SELECT
Occupation_Title,
Automation_Risk_Score,
CASE
WHEN Automation_Risk_Score >= 75 THEN 'High Risk'
WHEN Automation_Risk_Score >= 50 THEN 'Medium Risk'
ELSE 'Low Risk'
END AS Risk_Level
FROM ai_workforce_final_dataset;