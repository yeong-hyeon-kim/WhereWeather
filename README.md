## ๐ ํ๋ก์ ํธ ๊ฐ์(Introduce Project)

### WhereWeather

* `GitHub` `Action`์ ์ด์ฉํ์ฌ `Issue` ๋ฐ `Gist`์ ๋ ์จ ์ ๋ณด๋ฅผ ๋ฑ๋กํฉ๋๋ค.
* ๋๋ง์ GitHub Pin์ ํ์ํฉ๋๋ค.

## ๐ท๏ธ ๊ธฐ๋ฅ(Function)

1. [๋ ์จ ์ด์ ๋ฑ๋ก](#๋ ์จ-์ด์-๋ฑ๋ก)
1. [๋ ์จ Gist ์๋ฐ์ดํธ](#๋ ์จ-Gist-๋ฑ๋ก)

### ์ธ๋ถ ๊ธฐ๋ฅ(Function Detail)

#### ๋ ์จ ์ด์ ๋ฑ๋ก

1. ํน์  ์ฃผ๊ธฐ๋ก ๋ ์จ ์ ๋ณด๋ฅผ ์กฐํํ์ฌ ์ด์๋ก ๋ฑ๋กํฉ๋๋ค.

#### ๋ ์จ Gist ๋ฑ๋ก

1. ํน์  ์ฃผ๊ธฐ๋ก ๋ ์จ ์ ๋ณด๋ฅผ ์กฐํํ์ฌ Gist๋ฅผ ์๋ฐ์ดํธํฉ๋๋ค.
![Pinned](/img/Pinned-JejuPureunBadand.PNG)

## ๐ก ์ฌ์ฉ๋ฒ(Tip)

1.Personal access token์(<https://github.com/settings/tokens>) ์์ฑํฉ๋๋ค.

2.๋ ํฌ์งํ ๋ฆฌ์์ `Settings > Secrets > Actions > New` ์์๋ก Secrets์ ์์ฑํฉ๋๋ค.
![New Secret](/img/New%20Secret.PNG)

* [Secrets ์ฐธ๊ณ ](#ํ๊ฒฝ๋ณ์Environment-Variable)

3.Action > New workflow์์ `set up a workflow yourself` ๋๋ ํํ๋ฆฟ์ ์ ํํฉ๋๋ค.

4.[`Weather-Issues`](/.github/workflows/Weather-Issues.yml) ์ฐธ๊ณ ํ์ฌ ์์ฑํฉ๋๋ค.
    * ์ฃผ๊ธฐ๋ ํฌ๋ก ์์ผ๋ก ์ง์ ํฉ๋๋ค.

## ๐ป ๊ฐ๋ฐ ํ๊ฒฝ(Develop Environment)

### ์ธ๋ถ ํ๊ฒฝ(Environment Detail)

* โ OS : ![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=Windows&logoColor=white)
  * ๐ Version : `10 Pro 21H2`
* โ Language : ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)
  * ๐ Version : `3.10.4`
* โ Dependency : [`requirements`](/requirements.txt)

## ๐ ๋น๊ณ (Remark)
* Action Workflow
  * [`Weather-Issues`](/.github/workflows/Weather-Issues.yml)
  * [`start-python-package`](/.github/workflows/start-python-package.yml)

### ํ๊ฒฝ๋ณ์(Environment Variable)

* `MY_GITHUB_TOKEN` : `Personal access tokens`
* `GIST_ID` : `Gist ID`
* `GIST_NAME` : ์ด์ ๋ฐ Gist ๋ช์นญ
* `REG_CODE` : ์ง์ญ(๋์) ์ฝ๋

    |๋์|์ง์ญ(๋์) ์ฝ๋|
    |--|--|
    |๊ฐ๋ฆ|4215036027|
    |๊ด์ฃผ|2917060200|
    |๋๊ตฌ|2714051000|
    |๋์ |3020054000|
    |๋ชฉํฌ|4611055400|
    |๋ฐฑ๋ น๋|2872033000|
    |๋ถ์ฐ|2611053000|
    |์์ธ|1159068000|
    |์์ด|4221056000|
    |์์|4111356000|
    |์๋|4717062000|
    |์ฌ์|4613057000|
    |์ธ๋ฆ๋-๋๋|4794025000|
    |์ธ์ฐ|3111061000|
    |์ธ์ฒ|2811058500|
    |์ ์ฃผ|4511357000|
    |์ ์ฃผ|5011059000|
    |์ฐฝ์|4812552000|
    |์ฒญ์ฃผ|4311374100|
    |์ถ์ฒ|4211070500|
    |ํ์ฃผ|4148025300|
    |ํฌํญ|4711155000|
    |ํ์ฑ|4480025600|
    |ํ์ฐ๋|4691036000|
  * ์ธ๋ถ ์ง์ญ์ [ํ์ ํ์ค์ฝ๋๊ด๋ฆฌ์์คํ](https://www.code.go.kr/stdcode/regCodeL.do) ์์ ํ์ธํ  ์ ์์ต๋๋ค.
