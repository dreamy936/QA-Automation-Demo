# =============================
# 语言：纯 Python 🐍。
# 作用：提供 全局可用的 fixture（夹具），不用在每个测试文件里重复写。
# 归属：这是 Pytest 框架的一个特殊配置文件，名字必须是 conftest.py。
# =============================

import os
import pytest

# API base URL
# API 基础地址：（提供了 github_api_base fixture，返回 GitHub API 的 base URL。测试时可以直接调用，不用重复写 URL）
# API ベースURL
@pytest.fixture(scope="session")
def github_api_base():
    return "https://api.github.com"


# Playwright UI fixture with auto screenshot
# Playwright 页面夹具，失败时自动截图（用 yield 暴露 page 给测试用例。如果用例失败，会在 test-results/ 目录自动保存截图。）
# Playwright UIフィクスチャ、失敗時に自動スクリーンショット
@pytest.fixture(scope="function")
def pw_context(page, request):
    yield page
    # 测试执行后的阶段报告由 makereport 钩子注入到 item 上
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        os.makedirs("test-results", exist_ok=True)
        page.screenshot(path=f"test-results/{request.node.name}.png")


# Hook: capture test result (pytest 8 requires hookwrapper=True)
# 钩子：捕获测试结果（pytest 8 要求 hookwrapper=True）
# フック：テスト結果をキャプチャ（pytest 8はhookwrapper=Trueが必須）
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


# Hook: take full-page screenshot on failure & embed in pytest-html
# 钩子：失败时全屏截图，并嵌入 pytest-html 报告
# フック：失敗時に全ページスクリーンショットを撮り、pytest-htmlレポートに埋め込み
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # 仅在用例执行阶段失败才处理
    if rep.when != "call" or rep.passed:
        return

    # 需要能拿到 page（或我自定义的 pw_context）
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

    # Embed screenshot in pytest-html report
    # 将截图嵌入 pytest-html 报告
    # pytest-htmlレポートにスクリーンショットを埋め込み
    try:
        from pytest_html import extras
        extra = getattr(rep, "extra", [])
        extra.append(extras.image(str(img)))
        rep.extra = extra
    except Exception:
        pass
