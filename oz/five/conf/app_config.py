import os
import json

# 기본 디렉토리 경로 설정
base_dir = os.path.dirname(os.path.abspath(__file__))
resource_dir = os.path.join(base_dir, "..", "..", "resources")
config_file = os.path.join(resource_dir, "config.json")

with open(config_file, "r") as f:
    config = json.load(f)

# 설정을 가져오는 함수
def get_config():
    return config