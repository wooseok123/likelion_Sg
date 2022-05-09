# 복권 추첨기

import random


def make_lotto():
    randomNum = random.sample(range(1,46),6)
    randomNum.sort()
    
    # 1-45 사이의 번호 6개를 랜덤으로 뽑아 lotto 배열에 넣어보세요
    # HINT: random 모듈 사용
    
    return randomNum


def print_lottos(lottos):
    for i in range(len(lottos)):
        lottos[i].sort()
        print(f"{i+1}번째 복권: {lottos[i]}")
    # 뽑은 복권들을 형식에 맞게 출력해보세요
    # HINT: 정렬 함수 사용



while True:
    lottos = []

    # 구매할 복권의 개수를 입력받아보세요
    howManyLotto = input("구매할 복권의 개수를 입력해주세요 : ")

    # 입력값이 숫자가 아닌 경우는 어떻게 처리할 수 있을까요?
    # HINT: 숫자 판별 함수 사용

    if howManyLotto.isdigit() :
        for i in range(int(howManyLotto)):
            lottos.append(make_lotto())

    else:
        print("숫자를 입력해주세요")
        continue

    # 구매할 복권의 개수만큼 복권을 만들어 lottos 배열에 넣어보세요
    
    print_lottos(lottos)
    break
