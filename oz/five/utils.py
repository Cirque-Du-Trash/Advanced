import random
import string
from faker import Faker

faker = Faker()

# 고정 길이 문자열 생성
def generate_fixed_length_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# 유니크 문자열 생성
def generate_unique_string(existing_values, length=10):
    while True:
        unique_str = generate_fixed_length_string(length)
        if unique_str not in existing_values:
            return unique_str

# 유니크 인티저 생성
def generate_unique_integer(existing_values, max_value=30000):
    unique_int = faker.random_int(min=0, max=max_value)
    while unique_int in existing_values:
        unique_int = faker.random_int(min=0, max=max_value)
    return unique_int