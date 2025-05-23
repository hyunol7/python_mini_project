# 맞춰야 할 단어를 리스트로 변환 (문자 하나씩 분리)
question = list("batman")

# 플레이어가 맞춘 글자를 보여줄 리스트 (처음엔 전부 '-'로 표시)
lst = []
for i in range(0, len(question)):
    lst.append('-')

# 단어 길이만큼 '-'로 가려진 상태 출력
print("Here is the word")
print(lst)

# 최대 시도 횟수
num_of_try = 10

# 게임 루프 시작
while True:
    # 사용자로부터 문자 하나 입력받기
    chat = input("Guess the char?")

    # 입력받은 문자가 실제 단어에 있는지 확인
    i = 0  # 인덱스 추적용
    for elem in question:
        if elem == chat:
            lst[i] = chat  # 맞춘 위치에 문자 표시
        i += 1

    # 현재 상태 출력
    print(lst)

    # 모든 문자를 다 맞췄는지 확인
    if "-" not in lst:
        print("You win")
        break  # 게임 종료 (승리)

    # 시도 횟수 초과했는지 확인
    if num_of_try < 1:
        print("You lose")
        break  # 게임 종료 (패배)

    # 틀렸든 맞췄든 기회는 줄어든다
    num_of_try -= 1
