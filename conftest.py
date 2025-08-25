#Install Playwright browsers for UI tests.
#为 UI 测试装好 Playwright 浏览器
#Automatically take a screenshot on test failure and save to the 'test-results' directory, making it easy to view as an artifact in GitHub Actions.
#失败自动截图到 test-results，便于在 Actions 里查看工件


import os
import pytest

# API 基础地址
@pytest.fixture(scope="session")
def github_api_base():
    return "https://api.github.com"

# Playwright 页面包装：失败时截图到 test-results/
@pytest.fixture(scope="function")
def pw_context(page, request):
    yield page
    # 测试执行后的阶段报告由 makereport 钩子注入到 item 上
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        os.makedirs("test-results", exist_ok=True)
        page.screenshot(path=f"test-results/{request.node.name}.png")

# ！！！pytest 8 需要显式声明 hookwrapper=True
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 先让其他钩子/pytest 执行
    outcome = yield
    # 再拿到报告对象
    rep = outcome.get_result()
    # 注入到用例对象上，供上面的 fixture 判断
    setattr(item, "rep_" + rep.when, rep)

#失败时自动截图并嵌入 HTML 报告
from pathlib import Path
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # 仅在用例执行阶段失败才处理
    if rep.when != "call" or rep.passed:
        return

    # 需要能拿到 page（或你自定义的 pw_context）
    page = None
    for name in ("page", "pw_context"):
        if name in item.funcargs:
            page = item.funcargs[name]
            break
    if not page:
        return

    out_dir = Path("test-results") / item.name
    out_dir.mkdir(parents=True, exist_ok=True)
    img = out_dir / "screenshot.png"
    try:
        page.screenshot(path=str(img), full_page=True)
    except Exception:
        return

    # 嵌入 pytest-html
    try:
        from pytest_html import extras
        extra = getattr(rep, "extra", [])
        extra.append(extras.image(str(img)))
        rep.extra = extra
    except Exception:
        pass
