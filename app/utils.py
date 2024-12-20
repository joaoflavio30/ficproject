import requests
from django.conf import settings

def get_access_token():
    url = settings.OAUTH2_TOKEN_URL
    payload = {
        "grant_type": "client_credentials",
        "client_id": settings.OAUTH2_CLIENT_ID,
        "client_secret": settings.OAUTH2_CLIENT_SECRET,
    }
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception(f"Failed to fetch token: {response.status_code} {response.text}")

def fetch_api_data():
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f"{settings.OAUTH2_API_BASE_URL}/v2/resource"  # Substitua pelo endpoint real
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed: {response.status_code} {response.text}")

