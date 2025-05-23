# 인원 수와 음식 가격 리스트 정의
num_of_ppl = 3
food_prices = [10, 20, 15, 17, 50]

# 더치페이 계산 함수 정의
def going_dutch(food_prices: list, num_of_ppl: int):
    total = 0  # 총합 초기화
    for price in food_prices:
        total += price  # 각 음식 가격을 더해 총합 계산
    print(f"Your total is {total}")  # 총합 출력
    return float(total) / num_of_ppl  # 1인당 부담 금액 반환

# 함수 호출 → 1인당 금액 계산
bill = going_dutch(food_prices=food_prices, num_of_ppl=num_of_ppl)

# 1인당 지불해야 할 금액 출력
print(bill)
