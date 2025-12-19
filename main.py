from cli import parse_args
from app import load_json, load_default_config, load_env
from app.services import fetch_conversion_rate_currency
import os
# from dotenv import load_dotenv

def main():
 args = parse_args()
 load_env(args.env)
 api_currency_key = os.getenv("API_KEY_CURRENCY")

 json_config = load_default_config()
 currency_base_url = json_config["api"]["currency_url"]

 currency = args.currency
 print(fetch_conversion_rate_currency(currency_base_url, api_currency_key, currency))

if __name__ == "__main__":
       main()
