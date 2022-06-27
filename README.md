## 📕 프로젝트 개요(Introduce Project)

### WhereWeather

* `GitHub` `Action`을 이용하여 `Issue` 및 `Gist`에 날씨 정보를 등록합니다.
* 나만의 GitHub Pin을 표시합니다.

## 🏷️ 기능(Function)

1. [날씨 이슈 등록](#날씨-이슈-등록)
1. [날씨 Gist 업데이트](#날씨-Gist-등록)

### 세부 기능(Function Detail)

#### 날씨 이슈 등록

   1. 특정 주기로 날씨 정보를 조회하여 이슈로 등록합니다.

#### 날씨 Gist 등록
   1. 특정 주기로 날씨 정보를 조회하여 Gist를 업데이트합니다.
   ![Pinned](/img/Pinned-JejuPureunBadand.PNG)

## 💡 사용법(Tip)

1. Personal access token을(<https://github.com/settings/tokens>) 생성합니다.
2. 레포지토리에서 `Settings > Secrets > Actions > New` 순서로 Secrets을 생성합니다.
  ![New Secret](/img/New%20Secret.PNG)

* [Secrets 참고](#환경변수env)

3. Action > New workflow에서 `set up a workflow yourself` 또는 템플릿을 선택합니다.

4. [`Weather-Issues`](/.github/workflows/Weather-Issues.yml) 참고하여 생성합니다.
    * 주기는 크론식으로 지정합니다.

## 💻 개발 환경(Develop Environment)

### 세부 환경(Environment Detail)

* ✔ OS : ![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=Windows&logoColor=white)
  * 🕒 Version : `10 Pro 21H2`
* ✔ Language : ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)
  * 🕒 Version : `3.10.4`
* ✔ Dependency : [`requirements`](/requirements.txt)

## 📖 비고(Remark)
* Action Workflow
  * [`Weather-Issues`](/.github/workflows/Weather-Issues.yml)
  * [`start-python-package`](/.github/workflows/start-python-package.yml)

### 환경변수(Env.)

  * `MY_GITHUB_TOKEN` : `Personal access tokens`
  * `GIST_ID` : `Gist ID`
  * `GIST_NAME` : 이슈 및 Gist 명칭
  * `REG_CODE` : 법정동 코드
    |주요 도시|코드|
    |--|--|
    |강릉|4215036027|
    |광주|2917060200|
    |대구|2714051000|
    |대전|3020054000|
    |목포|4611055400|
    |백령도|2872033000|
    |부산|2611053000|
    |서울|1159068000|
    |속초|4221056000|
    |수원|4111356000|
    |안동|4717062000|
    |여수|4613057000|
    |울릉도-독도|4794025000|
    |울산|3111061000|
    |인천|2811058500|
    |전주|4511357000|
    |제주|5011059000|
    |창원|4812552000|
    |청주|4311374100|
    |춘천|4211070500|
    |파주|4148025300|
    |포항|4711155000|
    |홍성|4480025600|
    |흑산도|4691036000|
  * 세부 지역은 <https://www.code.go.kr/stdcode/regCodeL.do> 에서 확인할 수 있습니다.