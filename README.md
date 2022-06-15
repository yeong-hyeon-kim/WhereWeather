## 📕 프로젝트 개요(Introduce Project)

### WhereWeather

* `GitHub` `Action`을 이용하여 `Issue`에 날씨 정보를 등록합니다.

## 🏷️ 기능(Function)

1. [날씨 정보 알림](#날씨-정보-알림)

### 세부 기능(Function Detail)

#### 기상 정보 알림

   1. 특정 주기로 날씨 정보를 조회하여 이슈로 등록합니다.

## 💡 사용법(Tip)

1. Personal access token을(<https://github.com/settings/tokens>) 생성합니다.
2. 레포지토리에서 `Settings/Secrets/Actions/New` 순서로 Secrets을 생성합니다.
  ![New Secret](/img/New%20Secret.PNG)

* `Name` : `Alias`
* `Value` : `Personal access token`

3. Action/New workflow에서 `set up a workflow yourself` 또는 템플릿을 선택합니다.

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
