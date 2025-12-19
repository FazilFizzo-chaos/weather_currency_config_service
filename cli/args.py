import argparse

def parse_args():
 config_parser = argparse.ArgumentParser(description="Weather & Currency Service")

 config_parser.add_argument("--env", choices=["dev", "prod"], type=str, required=True, help="environment for the project")
 # config_parser.add_argument("--currency", help="Currency for conversion")
 # config_parser.add_argument("--first_currency", required=False, default="USD", help=" 1stCurrency for conversion")
 # config_parser.add_argument("--second_currency", required=False, default="TZS", help=" 2nd Currency for conversion")
 # config_parser.add_argument("--amount", required=False, help="conversion amount")

 config_parser.add_argument("--city_name", default="Dodoma", required=False, help="Name of the city")
 config_parser.add_argument("--state_code", default="TZ-03", required=False, help="State code")
 config_parser.add_argument("--country_code", default="TZ", required=False, help="Country code in ISO 3166 standard or format")

 args = config_parser.parse_args()
 return args