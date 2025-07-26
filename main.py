from auth_manager import create_access_token
from customers import get_companies

if __name__ == "__main__":
    base_url = "https://login.microsoftonline.com/c90883ad-2e4e-4e99-8bbb-32445268ef88/"
    endpoint = "customers/sales"
    access_token = create_access_token()
    api_response = get_companies(base_url,endpoint,access_token)
    
    print(api_response)