from dotenv import load_dotenv
import os
#환경변수를 위한 모듈
import requests
# 카카오에게 요청을 보내기 위한 모듈
import json
#python 객체를 JSON 데이터로 만들기 위해 쓰이는 파이썬의 내장 json 모듈

load_dotenv() #환경변수 호출
rest_api_key = os.getenv("REST_API_KEY") 
# 환경변수에서 REST_API_KEY로 저장된 값 가져와서 rest_api_key로 저장
authorization_code = os.getenv("AUTHORIZATION_CODE")
# 환경변수에서 AUTHORIZATION_CODEY로 저장된 값 가져와서 authorization_code 로 저장
url = 'https://kauth.kakao.com/oauth/token'
# 토큰 발급을 해달라고 요청할 url
redirect_uri = 'http://127.0.0.1'
# 발급된 토큰을 반환해줄 url
data = { # 카카오에게 내가 이 api를 활용하겠다~라고 요청 보낼 때 카카오가 요구하는 정보들입니다.
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorization_code,
    }
# 토큰을 발급할 때 카카오가 요구하는 정보들입니다.
response = requests.post(url, data=data)
# 우리가 설정한 토큰 발급을 요청할 url에 , 카카오가 토큰 발급을 위해 필요하다고 한 정보들을 넣어 
# 토큰을 발급해달라는 요청을 보내면 돌아올 응답을 response에 담습니다.
tokens = response.json()
# 토큰 발급 응답을 json 형태로 변환해줍니다.
print(tokens)
# 우리의 터미널에 한번 토큰을 출력해줍니다. (확인용)
with open("kakao_token.json","w") as json_file:
# "kakao_code_json" 이라는 이름의 파일을 쓰기("w") 모드로 열어놓고,
    json.dump(tokens, json_file)
# json으로 내보내고자 하는 파이썬 객체인 tokens를
# 직렬화된 데이터가 쓰여질 파일 json_file 에 쓰기를 해주었습니다