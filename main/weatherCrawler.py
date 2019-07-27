import requests
from bs4 import BeautifulSoup

def getWeather():
    response = requests.get("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8").text

    soup = BeautifulSoup(response,'html.parser')
    wet = soup.select('.now dl .item_condition span')[0].text

    return wet