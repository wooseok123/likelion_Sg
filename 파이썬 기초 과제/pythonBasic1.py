# 문자열 다루기

string_input = "  abcd ,    abcd  "

# 문자열을 콤마를 기준으로 나누어 각각 저장해보세요

stringA, stringB = string_input.split(",")

# 두 개의 문자열이 가진 앞뒤 공백을 제거해볼까요?

stringA = stringA.strip()
stringB = stringB.strip()

# 두 개의 문자열이 같은지 비교하여 결과를 출력해보세요

areStringsSame = ""

if stringA == stringB :
    areStringsSame = "같은"
else :
    areStringsSame = "다른"

print(f"두 문자열은 {areStringsSame} 문자열입니다.")

# 다시 두 개의 문자열을 합쳐 하나의 문자열로 만드세요

newString = stringA + stringB
newString_length = len(newString)

# 합친 문자열의 길이를 출력해보세요

print(f"합친 문자열의 길이는 {newString_length} 입니다.")