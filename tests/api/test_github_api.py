import requests
import pytest

BASE_URL = "https://api.github.com"

def test_get_octocat_user_info():
    """测试获取 octocat 用户信息 API"""
    url = f"{BASE_URL}/users/octocat"
    response = requests.get(url)

    # 验证响应状态码为 200
    assert response.status_code == 200

    # 验证返回的 JSON 数据
    data = response.json()
    assert data['login'] == 'octocat'
    assert data['id'] == 583231
    assert data['name'] == 'The Octocat'
    assert data['type'] == 'User'

def test_get_non_existent_user():
    """测试获取不存在的用户，验证 404 状态码"""
    url = f"{BASE_URL}/users/a_non_existent_user_12345"
    response = requests.get(url)

    # 验证响应状态码为 404
    assert response.status_code == 404
