import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_test(page: Page):
    # 每次测试前，访问 GitHub 首页
    page.goto("https://github.com/")

def test_github_homepage_title(page: Page):
    # 验证页面标题
    assert "GitHub: Let’s build from here…" in page.title()

def test_search_for_playwright_repo(page: Page):
    # 查找搜索框
    page.get_by_placeholder("Search GitHub…").click()
    # 输入关键词
    page.get_by_placeholder("Search GitHub…").fill("playwright")
    page.get_by_placeholder("Search GitHub…").press("Enter")
    # 验证搜索结果页面标题
    expect(page).to_have_title("Search · playwright")
    # 验证搜索结果中是否包含特定仓库
    expect(page.get_by_text("microsoft/playwright")).to_be_visible()
