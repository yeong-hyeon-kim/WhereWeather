import requests
from bs4 import BeautifulSoup as bs


def SelectWeather(LocalCode):
    page = 'https://www.weather.go.kr/w/wnuri-fct2021/main/current-weather.do?code=' + \
        str(LocalCode) + '&unit=m%2Fs&aws=N#refresh'
    response = requests.get(page)
    soup = bs(response.content, 'html.parser')

    # 업데이트 일시
    Update = soup.select('.cmp-cmn-para > a.updated-at > span')
    UpdateContent = "📆 : " + Update[0].text
    print(UpdateContent)

    # 온도
    Temp = soup.select('.cmp-cur-weather > ul.wrap-1 > li > span.tmp')
    TempContent = "🌡 :  " + Temp[0].contents[0] + "℃"
    print(TempContent)

    # 습도
    Humid = soup.select('.cmp-cur-weather > ul.wrap-2 > li > span')
    HumidContent = "💧 : " + Humid[0].text + Humid[1].text
    print(HumidContent)

    # 일출/일몰
    SunriseAndSunset = soup.select('.cmp-cur-weather > ul.wrap-3 > li > span')
    SunriseAndSunsetContent = "🌄 : " + \
        SunriseAndSunset[0].text + " " + SunriseAndSunset[1].text + \
        " 🌅 " + SunriseAndSunset[2].text + " " + SunriseAndSunset[3].text
    print(SunriseAndSunsetContent)

    # 기상특보
    Impact = soup.select('.cmp-impact-fct > p')
    ImpactContent = "📢 : " + Impact[0].text
    print(ImpactContent)

    Weather = ""
    Weather += str(UpdateContent) + "\n"
    Weather += str(TempContent) + "\n"
    Weather += str(HumidContent) + "\n"
    Weather += str(SunriseAndSunsetContent) + "\n"
    Weather += str(ImpactContent) + "\n"

    return Weather
