import argparse

def parse_args():
 config_parser = argparse.ArgumentParser(description="Weather & Currency Service")

 config_parser.add_argument("--env", choices=["dev", "prod"], type=str, required=False, help="environment for the project")
 config_parser.add_argument("--currency", default="USD", help="Currenvy for conversion")

 args = config_parser.parse_args()
 return args