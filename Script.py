import requests
from bs4 import BeautifulSoup as bs

page = 'https://www.weather.go.kr/w/wnuri-fct2021/main/current-weather.do?code=4794033000&unit=m%2Fs&aws=N#refresh'
response = requests.get(page)
soup = bs(response.content, 'html.parser')

# 현재 날씨
# 온도
Temp = soup.select('.cmp-cur-weather > ul.wrap-1 > li > span')
print(Temp[0].text + Temp[3].text)

# 습도
Humid = soup.select('.cmp-cur-weather > ul.wrap-2 > li > span')
print(Humid[0].text + Humid[1].text)

# 일출/일몰
SunriseAndSunset = soup.select('.cmp-cur-weather > ul.wrap-3 > li > span')
print(SunriseAndSunset[0].text + " " + SunriseAndSunset[1].text + " " +
      SunriseAndSunset[2].text + " " + SunriseAndSunset[3].text)

# 기상특보
impact = soup.select('.cmp-impact-fct > p')
print(impact[0].text)
