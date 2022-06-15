import os
from datetime import datetime
from pytz import timezone
from github import Github
from Script import SelectWeather


def get_github_repo(access_token, repository_name):
    g = Github(access_token)
    repo = g.get_user().get_repo(repository_name)
    return repo


def upload_github_issue(repo, title, body):
    repo.create_issue(title=title, body=body)


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "WhereWeather"
    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일 %HH시 %M분")

    issue_title = "[" + today_date + "] 🏝 독도 날씨"
    upload_contents = SelectWeather()
    repo = get_github_repo(
        access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")
