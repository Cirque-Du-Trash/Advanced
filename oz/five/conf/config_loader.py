import os
import json

def get_config_file():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    resource_dir = os.path.join(base_dir, "..", "..", "resources")
    return os.path.join(resource_dir, "config.json")

def load_config():
    config_file = get_config_file()
    with open(config_file, "r") as f:
        return json.load(f)