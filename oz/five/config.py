import json

# 설정 파일 로드
def load_config(file_path):
    if not file_path.endswith('.json'):
        raise ValueError("Unsupported file type. Use JSON.")
    with open(file_path, 'r') as file:
        return json.load(file)