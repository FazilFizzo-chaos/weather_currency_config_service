from dotenv import load_dotenv
import os
import json
from pathlib import Path
load_dotenv(".env.dev")

env = os.getenv("APP_ENV", "dev")

BASE_DIR = Path(__file__).resolve().parent # base dir of this file
PROJECT_ROOT = BASE_DIR.parent # root dir of the whole project
CONFIG_DIR = PROJECT_ROOT / "config" # config files dir
config_file_env_path = CONFIG_DIR / f"{env}.json"

def load_json():
    try:
      with open(config_file_env_path, encoding="utf-8") as config_file:
        return json.load(config_file)
    except FileNotFoundError:
       raise FileNotFoundError(f"Config file not found: config/{env}.json")

config_default_path = CONFIG_DIR / "defaults.json"
def load_default_config():
    try:
      with open(config_default_path, encoding="utf-8") as f:
        return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {config_default_path}")