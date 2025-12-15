import argparse

def parse_args():
 config_parser = argparse.ArgumentParser(description="Reading config files")

 config_parser.add_argument("--env", choices=["dev", "prod"], type=str, required=False, help="environment for the project")

 args = config_parser.parse_args()
 return args