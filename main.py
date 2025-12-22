from cli import parse_args
from app import load_json, load_default_config, load_env, deep_merge_conflict
from app.services import fetch_conversion_rate_currency, fetch_conversion_rate_btn_two_currencies, fetch_geo_location, fetch_current_weather_data
import os
import json

def main():
 args = parse_args()

 load_env(args.env)
 api_currency_key = os.getenv("API_KEY_CURRENCY")
 api_weather_key = os.getenv("API_KEY_WEATHER")

 currency = args.currency
 first_currency = args.first_currency
 second_currency = args.second_currency
 amount = args.amount
 city_name = args.city_name
 state_code = args.state_code
 country_code = args.country_code


 override_env_config = load_json(args.env)
 default_config = load_default_config()

 if args.env is None:
  default_config = load_default_config()
  currency_base_url = default_config["api"]["currency_url"]
  print(fetch_conversion_rate_currency(currency_base_url, api_currency_key, currency))
  if amount:
   print(fetch_conversion_rate_btn_two_currencies(currency_base_url, api_currency_key, first_currency, second_currency,
                                                  amount))
  else:
   print(fetch_conversion_rate_btn_two_currencies(currency_base_url, api_currency_key, first_currency, second_currency))

  geo_location_url = default_config["api"]["geocode_url"]
  geo_data = fetch_geo_location(geo_location_url, api_weather_key, city_name, state_code, country_code)[0]
  geo_lat = geo_data["lat"]
  geo_lon = geo_data["lon"]

  weather_url = default_config["api"]["weather_url"]
  weather_data = fetch_current_weather_data(weather_url, api_weather_key, geo_lat, geo_lon)
 elif args.env:
  merge_config = deep_merge_conflict(default_config, override_env_config)
  currency_merge_config_url = merge_config["api"]["currency_url"]
  print(fetch_conversion_rate_currency(currency_merge_config_url, api_currency_key, currency))
  if amount:
   print(fetch_conversion_rate_btn_two_currencies(currency_merge_config_url, api_currency_key, first_currency, second_currency,
                                                  amount))
  else:
   print(fetch_conversion_rate_btn_two_currencies(currency_merge_config_url, api_currency_key, first_currency, second_currency))

  geo_location_url = merge_config["api"]["geocode_url"]
  geo_data = fetch_geo_location(geo_location_url, api_weather_key, city_name, state_code, country_code)[0]
  geo_lat = geo_data["lat"]
  geo_lon = geo_data["lon"]

  weather_url = merge_config["api"]["weather_url"]
  weather_data = fetch_current_weather_data(weather_url, api_weather_key, geo_lat, geo_lon)


if __name__ == "__main__":
       main()
