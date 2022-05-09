# 성적 계산기

import math


students = {20111111: ['호랑이', 92, 85, 65], 20101234: ['사자', 100, 90, 75],
            20124321: ['토끼', 95, 90, 90], 20135555: ['여우', 55, 60, 65]}


def add():
    id = int(input("학번을 입력하세요: "))

    # 이미 등록된 학생의 학번이 입력된 경우는 어떻게 확인할 수 있을까요?

    if id in students.keys():
        print("이미 등록된 학생입니다.")
        return

    # 학생의 이름과 국영수 성적을 입력받아 등록해주세요

    name = input("이름을 입력하세요 : ")
    korean = int(input("국어성적을 입력하세요 : "))
    english = int(input("영어성적을 입력하세요 : "))
    math = int(input("수학성적을 입력하세요 : "))

    students[id] = [name, korean, english, math]

    print("학생의 성적을 입력했습니다.")


def delete():
    id = int(input("삭제하기 원하는 학생의 학번을 입력하세요: "))

    # 없는 학생의 학번이 입력된 경우는 어떻게 확인할 수 있을까요?
    
    if not id in students.keys():
        print("없는 학생입니다.")
        return

    # 학생 정보를 삭제해주세요

    del students[id]

    print("학번: %d 학생의 정보를 삭제했습니다." % id)


def print_all():
    print("-" * 50)

    for key,value in students.items():
        print(f"학번 : {key}, 이름 : {value[0]}          | 국어 : {value[1]} / 영어 : {value[2]} / 수학 : {value[3]} / 평균 : {int(sum(value[1:]))}")
    # 학생들의 성적을 포맷에 맞게 출력해주세요
    # 성적의 평균을 구해 함께 출력해주세요


    print("-" * 50)


while True:
    print()
    print("1. 추가, 2. 삭제, 3. 출력, 4. 종료")
    num = int(input("숫자를 선택하세요: "))
    print()

    # 조건문을 채워 넣어 주세요!
    if num == 1:
        add()
    elif num == 2:
        delete()
    elif num == 3:
        print_all()
    else:
        break

# 실습 3번 추가 HINT
# 1. add 함수에서 이미 등록된 학생인 경우 return으로 함수 종료하기
# 2. delete 함수에서 없는 학생인 경우에도 return으로 함수 종료하기
# 3. 사전에서 key 값으로 value 값을 가져올 때 해당 key 값이 없으면 None으로 반환됩니다
# 4. 출력은 예시와 똑같이 하지 않아도 됩니다 부담가지지 마세요
