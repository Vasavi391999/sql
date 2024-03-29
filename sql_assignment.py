# -*- coding: utf-8 -*-
"""sql assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17mSwvmyxnpgwmV2wFMx0-U25275AzPcS

Scenario 1: Candidates and Skills
Assuming that the first part is about candidates and their skills, and you want to find candidates who possess all the required skills (DS, Tableau, Python, SQL), you can use a query like this:
"""

SELECT ID
FROM [ATS]
WHERE Techn IN ('DS', 'Tableau', 'Python', 'SQL')
GROUP BY ID
HAVING COUNT(DISTINCT Techn) = 4;

"""This query selects the candidate IDs from the [ATS] table where the technology matches the required skills and ensures that the candidate possesses all four required skills.

Scenario 2: Product Info and Likes
Assuming the second part is about product information and likes, and you want to retrieve the IDs of products with 0 likes, you can use the following query:
"""

SELECT Pr-Id
FROM [Product Info Likes]
GROUP BY Pr-Id
HAVING COUNT(User fr-Id) = 0;

"""This query selects the product IDs from the [Product Info Likes] table where the count of likes is 0"""