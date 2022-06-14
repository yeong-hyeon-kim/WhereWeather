import requests
from bs4 import BeautifulSoup as bs


def SelectWeather():
    page = 'https://www.weather.go.kr/w/wnuri-fct2021/main/current-weather.do?code=4794033000&unit=m%2Fs&aws=N#refresh'
    response = requests.get(page)
    soup = bs(response.content, 'html.parser')

    # 업데이트 일시
    Update = soup.select('.cmp-cmn-para > a.updated-at > span')
    print("📆 : " + Update[0].text)

    # 온도
    Temp = soup.select('.cmp-cur-weather > ul.wrap-1 > li > span.tmp')
    print("🌡  : " + Temp[0].contents[0] + "℃")

    # 습도
    Humid = soup.select('.cmp-cur-weather > ul.wrap-2 > li > span')
    print("💧 : " + Humid[0].text + Humid[1].text)

    # 일출/일몰
    SunriseAndSunset = soup.select('.cmp-cur-weather > ul.wrap-3 > li > span')
    print("🌅 : " + SunriseAndSunset[0].text + " " + SunriseAndSunset[1].text + " " +
          SunriseAndSunset[2].text + " " + SunriseAndSunset[3].text)

    # 기상특보
    impact = soup.select('.cmp-impact-fct > p')
    print(impact[0].text)

    Weather = ""
    Weather += str(Update) + "\n"
    Weather += str(Temp) + "\n"
    Weather += str(Humid) + "\n"
    Weather += str(SunriseAndSunset) + "\n"

    return Weather


SelectWeather()
