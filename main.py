from cli import parse_args
from app import load_json, load_default_config, load_env
from app.services import fetch_conversion_rate_currency, fetch_conversion_rate_btn_two_currencies, fetch_geo_location
import os

def main():
 args = parse_args()
 load_env(args.env)
 json_config = load_default_config()

 # api_currency_key = os.getenv("API_KEY_CURRENCY")
 api_weather_key = os.getenv("API_KEY_WEATHER")

 # currency_base_url = json_config["api"]["currency_url"]
 # currency = args.currency
 # print(fetch_conversion_rate_currency(currency_base_url, api_currency_key, currency))

 # first_currency = args.first_currency
 # second_currency = args.second_currency
 # amount = args.amount
 # if amount:
 #  print(fetch_conversion_rate_btn_two_currencies(currency_base_url, api_currency_key, first_currency, second_currency, amount))
 # else:
 #  print(fetch_conversion_rate_btn_two_currencies(currency_base_url, api_currency_key, first_currency, second_currency))

 geo_location_url = json_config["api"]["geocode_url"]
 city_name = args.city_name
 state_code = args.state_code
 country_code = args.country_code

 geo_data = fetch_geo_location(geo_location_url, api_weather_key, city_name, state_code, country_code)[0]
 geo_lat = geo_data["lat"]
 geo_lon = geo_data["lon"]



if __name__ == "__main__":
       main()
