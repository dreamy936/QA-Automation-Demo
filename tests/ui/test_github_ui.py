def test_home_title(pw_context):
    pw_context.goto("https://github.com/", wait_until="domcontentloaded")
    assert "GitHub" in pw_context.title()

def test_search_results_by_url(pw_context):
    # 最稳：直接用查询参数访问搜索结果页
    pw_context.goto("https://github.com/search?q=playwright&type=repositories", wait_until="domcontentloaded")
    assert "search" in pw_context.url.lower()
    # 断言页面上有结果列表的容器
    assert pw_context.locator("main").inner_text().lower().count("playwright") >= 1

def test_search_from_home_relaxed(pw_context):
    # 更鲁棒的“从首页搜索”版本（若 GitHub 改了占位符也不至于红）
    pw_context.goto("https://github.com/", wait_until="domcontentloaded")
    # 搜索输入框有时是按钮触发，再出现输入框；尝试按 "/" 热键唤出搜索
    pw_context.keyboard.press("/")
    # 用更宽松的 role/name 查询；不同区域 name 可能略不同
    box = pw_context.get_by_role("combobox")
    box.fill("playwright")
    pw_context.keyboard.press("Enter")
    pw_context.wait_for_url("**/search**")
    assert "search" in pw_context.url.lower()
