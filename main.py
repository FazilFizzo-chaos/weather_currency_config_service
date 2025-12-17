from cli import parse_args
from app import load_json, load_default_config
import os
from dotenv import load_dotenv

args = parse_args()

# if args.env == "dev": # if env variable is 'dev', load dev configs
#  load_dotenv(".env.dev")
#  load_json(args.env)
# elif args.env == "prod":
#  load_dotenv(".env.prod")
#  load_json(args.env)
# else:   # else, if no argument(s) load default config
#  load_default_config()
config = load_default_config()