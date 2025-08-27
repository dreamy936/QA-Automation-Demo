# ================================
# 作用：API 测试文件，演示最小可跑的示例。  
# これは API テストファイルで、最小限の実行可能なサンプルを示す。  
# This is an API test file demonstrating the minimum runnable example.  
# ================================

# 发送 HTTP 请求 / HTTPリクエスト送信 / Send HTTP requests
import requests


# 测试用例【用户维度】：获取 GitHub 用户 octocat  （这是一个官方的吉祥物，可保证API请求必然返回200）
# GitHub ユーザー octocat を取得して検証  
# Test: fetch GitHub user "octocat" and validate response  
def test_get_user_octocat(github_api_base):
    r = requests.get(f"{github_api_base}/users/octocat", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert data["login"] == "octocat"


# 测试用例【仓库维度】：获取 Playwright 仓库信息  ，模拟“公司内部的项目仓库”是否能被正确访问。
# Playwright リポジトリ情報を取得して検証  
# Test: fetch Playwright repository info and validate response  
def test_get_repo_playwright(github_api_base):
    r = requests.get(f"{github_api_base}/repos/microsoft/playwright", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert data["name"].lower() == "playwright"  #目的：👉 “去 GitHub API 查询 microsoft/playwright 这个仓库，然后检查返回的 name 字段是不是等于 playwright。”
