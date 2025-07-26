import requests
from dotenv import load_dotenv
import os


def validate_env_vars():
    required_vars = ["CLIENT_ID", "CLIENT_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        print(f"Error: Faltan variables de entorno: {', '.join(missing_vars)}")
        return False
    return True


def create_access_token():
    load_dotenv()

    if not validate_env_vars():
        return None

    url = "https://login.microsoftonline.com/c90883ad-2e4e-4e99-8bbb-32445268ef88/oauth2/v2.0/token"
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    body_data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://api.businesscentral.dynamics.com/.default",
    }

    response = requests.post(
        url,
        body_data,
        timeout=10,
    )
    data = response.json()
    to_return_access_token = data.get("access_token")
    return to_return_access_token


access_token = create_access_token()
print(access_token)
