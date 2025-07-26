import requests

def get_headers(access_token):
    """Genera los headers necesarios para las solicitudes API."""
    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

def get_companies(base_url, endpoint, access_token):
    URL = f"{base_url}{endpoint}"
    response = requests.get(URL, headers=get_headers(access_token), timeout=10)
    response.raise_for_status()
    return response.json()