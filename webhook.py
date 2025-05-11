import requests

pl = {
    "name": "Amit Patharkar",         
    "regNo": "0827AL221017",          
    "email": "amitpatharkar220860@acropolis.in"  
}

u = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

response = requests.post(u, json=pl)

if response.status_code == 200:
    data = response.json()
    print("Webhook:", data.get("webhook"))
    print("AcsTk:", data.get("accessToken"))
