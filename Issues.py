import os
import github
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


def update_gist(access_token, gist_id, title, content):
    g = Github(access_token)
    gist = g.get_gist(gist_id)
    # Gits Contents
    data = {"Gist": github.InputFileContent(content, title)}
    gist.edit(files=data)


if __name__ == "__main__":
    # Debug Acces Token
    # access_token = ""
    access_token = os.environ['MY_GITHUB_TOKEN']
    # Debug Gist id
    # gist_id = ""
    gist_id = os.environ['GIST_ID']
    # Debug Gist Name
    # gist_name = "제주 🍊, 푸른 바당 🌊"
    gist_name = os.environ['GIST_NAME']
    # Debug Reg Code
    # reg_code = "5011059000"
    reg_code = os.environ['REG_CODE']

    repository_name = "WhereWeather"
    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일 %H시 %M분")

    issue_title = "[" + today_date + "] " + gist_name
    upload_contents = SelectWeather(reg_code)
    repo = get_github_repo(access_token, repository_name)

    update_gist(access_token, gist_id, gist_name, upload_contents)
    print("Update Github Gist Success!")

    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")
