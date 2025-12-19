import requests, json

def fetch_geo_location(config_geo_url: str, api_key, city_name, state_code, country_code):
    limit = 5
    try:
     response = requests.get(f"{config_geo_url}?q={city_name},{state_code},{country_code}&limit={limit}&appid={api_key}")
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
