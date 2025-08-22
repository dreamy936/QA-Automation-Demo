#测试文件最小可跑示例
#Test the min operatable case

import requests

def test_get_user_octocat(github_api_base):
    r = requests.get(f"{github_api_base}/users/octocat", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert data["login"] == "octocat"

def test_get_repo_playwright(github_api_base):
    r = requests.get(f"{github_api_base}/repos/microsoft/playwright", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert data["name"].lower() == "playwright"
