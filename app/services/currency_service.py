import requests

def fetch_conversion_rate_currency(config_url: str, api_key, currency: str):
    try:
     response = requests.get(f"{config_url}/{api_key}/latest/{currency}")
     print("Status code:", response.status_code)
     response.raise_for_status()
     if "application/json" in response.headers.get("Content-Type", ""):
       data = response.json()
       return data
     else:
         print("Response is not JSON")
    except requests.exceptions.JSONDecodeError:
            print("Response is not valid JSON")
    except requests.exceptions.RequestException as e:
        print("Request failed: ", e)