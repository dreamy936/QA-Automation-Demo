# 需要 fixtures: page（pytest-playwright 提供）/ 我们在 conftest 用 pw_context 包装

def test_home_title(pw_context):
    pw_context.goto("https://github.com/", wait_until="domcontentloaded")
    assert "GitHub" in pw_context.title()

def test_search_playwright(pw_context):
    pw_context.goto("https://github.com/", wait_until="domcontentloaded")
    pw_context.get_by_placeholder("Search or jump to...").click()
    pw_context.get_by_placeholder("Search or jump to...").fill("playwright")
    pw_context.keyboard.press("Enter")
    pw_context.wait_for_timeout(1000)
    # 断言结果页里含有关键字
    assert "playwright" in pw_context.url.lower()
