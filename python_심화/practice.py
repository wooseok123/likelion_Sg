from bs4 import BeautifulSoup 
import urllib.request
from dotenv import load_dotenv
import os
import json
import folium

load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_key = os.environ.get("CLIENT_KEY")

def make_issac_list() :
    url = 'http://www.isaacs.co.kr/bbs/board.php?bo_table=branches&page='
    pageNum = 2
    issac_list = []

    for j in range(1,pageNum):
        sourcecode = urllib.request.urlopen(url+str(j))
        soup = BeautifulSoup(sourcecode, "html.parser")

        for i in soup.find_all("td","td_subject"):
            temp_text = i.get_text()

            issac_list.append(temp_text)

    return issac_list


def search_map(search_text):
    encText = urllib.parse.quote(str(search_text))

    url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='+encText
    request = urllib.request.Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_key)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)

def make_location(issac_list):
    x = []
    y = []
    for issac_location in issac_list:
        temp_map = search_map(issac_location)
        temp_map = json.loads(temp_map)
        try:
            temp_map = temp_map['addresses'][0]
            x.append(float(temp_map['x']))
            y.append(float(temp_map['y']))
        except IndexError:
            pass
    return x, y

def make_marker(map_osm, x, y):
    for i in range(len(x)):
        folium.Marker([y[i], x[i]]).add_to(map_osm)



if __name__ == "__main__" : 

    issac_list = make_issac_list()
    x_list, y_list = make_location(issac_list)

    map_osm = folium.Map()
    map_osm = folium.Map(location=[37.4729081, 127.039306])
    
    make_marker(map_osm, x_list, y_list) #순서 주의해주세요!

    map_osm.save('issac.html')