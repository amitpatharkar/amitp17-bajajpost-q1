import requests

webhook_url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
access_token = "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdBTDIyMTAxNyIsIm5hbWUiOiJBbWl0IFBhdGhhcmthciIsImVtYWlsIjoiYW1pdHBhdGhhcmthcjIyMDg2MEBhY3JvcG9saXMuaW4iLCJzdWIiOiJ3ZWJob29rLXVzZXIiLCJpYXQiOjE3NDY5NjI3MzksImV4cCI6MTc0Njk2MzYzOX0.lXPCSJ1O16o274TWxBIf0MMQQJE0xAfg9C2n0nLB8Bo"

sql_query = """
SELECT 
    p.AMOUNT AS SALARY,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
    FLOOR(DATEDIFF(CURDATE(), e.DOB) / 365) AS AGE,
    d.DEPARTMENT_NAME
FROM PAYMENTS p
JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE DAY(p.PAYMENT_TIME) != 1
ORDER BY p.AMOUNT DESC
LIMIT 1;
"""

h = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

pl = {
    "finalQuery": sql_query.strip()
}

response = requests.post(webhook_url, headers=h, json=pl)

if response.status_code == 200:
    print("Query submitted")
else:
    print(f"fail: {response.status_code}")
    print(f"Response: {response.text}")

#eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdBTDIyMTAxNyIsIm5hbWUiOiJBbWl0IFBhdGhhcmthciIsImVtYWlsIjoiYW1pdHBhdGhhcmthcjIyMDg2MEBhY3JvcG9saXMuaW4iLCJzdWIiOiJ3ZWJob29rLXVzZXIiLCJpYXQiOjE3NDY5NjI3MzksImV4cCI6MTc0Njk2MzYzOX0.lXPCSJ1O16o274TWxBIf0MMQQJE0xAfg9C2n0nLB8Bo