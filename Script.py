import requests
from bs4 import BeautifulSoup as bs


def RefreshWeather(LocalCode):
    page = 'https://www.weather.go.kr/w/wnuri-fct2021/main/current-weather.do?code=' + \
        str(LocalCode) + '&unit=m%2Fs&aws=N#refresh'
    response = requests.get(page)
    soup = bs(response.content, 'html.parser')

    return soup


def SelectWeather(LocalCode):
    soup = RefreshWeather(LocalCode)

    # 업데이트 일시
    Update = soup.select('.cmp-cmn-para > a.updated-at > span')

    # 알수 없는 페이지 에러 발생 시 재조회
    if len(Update) == 0:
        soup = RefreshWeather(LocalCode)

    UpdateContent = "📆 : " + Update[0].text
    print(UpdateContent)

    # 온도
    Temp = soup.select('.cmp-cur-weather > ul.wrap-1 > li > span.tmp')
    TempContent = "🌡️  : " + Temp[0].contents[0] + "℃"
    print(TempContent)

    # 습도, 바람, 1시간강수량
    CurrentWeather = soup.select('.cmp-cur-weather > ul.wrap-2 > li > span')
    HumidContent = "💧  : " + CurrentWeather[0].text + CurrentWeather[1].text
    WindContent = "🍃 : " + CurrentWeather[2].text + CurrentWeather[3].text
    RainContent = "☔ : " + \
        CurrentWeather[4].text + " " + CurrentWeather[5].text
    print(HumidContent)
    print(WindContent)
    print(RainContent)

    # 대기질
    Air = soup.select('.cmp-cur-weather > ul.wrap-2 > li > strong > span')
    AirContent = "🍃 : PM2.5:" + Air[0].text + "-" + Air[1].text + \
        ",PM10:" + Air[2].text + "-" + Air[3].text + \
        ",O₃:" + Air[4].text + "-" + Air[5].text
    AirContent = AirContent.replace("범례보기", "")
    print(AirContent)

    # 일출/일몰
    SunriseAndSunset = soup.select('.cmp-cur-weather > ul.wrap-3 > li > span')
    SunriseAndSunsetContent = "🌅 : " + \
        SunriseAndSunset[0].text + " " + SunriseAndSunset[1].text + \
        " 🌇 " + SunriseAndSunset[2].text + " " + SunriseAndSunset[3].text
    print(SunriseAndSunsetContent)

    # 기상특보
    Impact = soup.select('.cmp-impact-fct > p')
    ImpactContent = "📢 : " + Impact[0].text
    print(ImpactContent)

    Weather = ""
    Weather += str(UpdateContent) + "\n"
    Weather += str(TempContent) + "\n"
    Weather += str(HumidContent) + "\n"
    Weather += str(WindContent) + "\n"
    Weather += str(SunriseAndSunsetContent) + "\n"
    Weather += str(RainContent) + "\n"
    Weather += str(AirContent) + "\n"
    Weather += str(ImpactContent) + "\n"

    return Weather
