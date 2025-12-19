from cli import parse_args
from app import load_json, load_default_config, load_env
from app.services import fetch_conversion_rate_currency, fetch_conversion_rate_btn_two_currencies
import os
# from dotenv import load_dotenv

def main():
 args = parse_args()
 load_env(args.env)
 api_currency_key = os.getenv("API_KEY_CURRENCY")

 json_config = load_default_config()
 currency_base_url = json_config["api"]["currency_url"]

 # currency = args.currency
 # print(fetch_conversion_rate_currency(currency_base_url, api_currency_key, currency))

 first_currency = args.first_currency
 second_currency = args.second_currency
 print(fetch_conversion_rate_btn_two_currencies(currency_base_url, api_currency_key, first_currency, second_currency))

if __name__ == "__main__":
       main()
