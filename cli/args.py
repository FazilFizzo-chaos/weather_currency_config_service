import argparse

def parse_args():
 config_parser = argparse.ArgumentParser(description="Weather & Currency Service")

 config_parser.add_argument("--env", choices=["dev", "prod"], type=str, required=False, help="environment for the project")
 config_parser.add_argument("--currency", help="Currency for conversion")
 config_parser.add_argument("--first_currency", required=False, help=" 1stCurrency for conversion")
 config_parser.add_argument("--second_currency", required=False, help=" 2nd Currency for conversion")

 args = config_parser.parse_args()
 return args