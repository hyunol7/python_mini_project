import random

# 소문자 알파벳 리스트
lower_alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]

# 대문자 알파벳 리스트
upper_alphabets = [alphabet.upper() for alphabet in lower_alphabets]

# 모든 알파벳 (소문자 + 대문자)
all_alphabets = lower_alphabets + upper_alphabets

# 숫자 리스트 (1~9)
numbers = [str(i) for i in range(1, 10)]

# 특수 문자 리스트
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '|', '/', '?', '.', ',', '>', '<', ':', ';', '[', ']', '{', '}', '~']

# 각 요소의 개수 설정
num_of_alphabets = 9
num_of_numbers = 3
num_of_symbols = 2

# 최종 비밀번호를 담을 리스트
strong_password = []

# 랜덤 알파벳 추가
for i in range(num_of_alphabets):
    strong_password.append(random.choice(all_alphabets))

# 랜덤 숫자 추가
for i in range(num_of_numbers):
    strong_password.append(random.choice(numbers))

# 랜덤 특수 문자 추가
for i in range(num_of_symbols):
    strong_password.append(random.choice(symbols))

# 리스트 섞기
random.shuffle(strong_password)

# 리스트를 문자열로 변환하여 출력
print("".join(strong_password))
