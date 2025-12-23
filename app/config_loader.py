from dotenv import load_dotenv
import os
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent  # base dir of this file
PROJECT_ROOT = BASE_DIR.parent  # root dir of the whole project
CONFIG_DIR = PROJECT_ROOT / "config"  # config files dir


def load_env(env=None):
   env_file = f".env.{env}"
   load_dotenv(env_file)


def load_json(env):
    config_file_env_path = CONFIG_DIR / f"{str(env)}.json"
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


def deep_merge_conflict(base: dict, override: dict) -> dict:
    result = base.copy()
    for key, value in override.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = deep_merge_conflict(result[key], value)
        else:
            result[key] = value
    return result