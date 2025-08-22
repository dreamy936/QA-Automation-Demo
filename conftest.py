#Install Playwright browsers for UI tests.
#为 UI 测试装好 Playwright 浏览器
#Automatically take a screenshot on test failure and save to the 'test-results' directory, making it easy to view as an artifact in GitHub Actions.
#失败自动截图到 test-results，便于在 Actions 里查看工件


# conftest.py
import os
import pytest

# ---- API 共用配置（如需 Token，可在此读取环境变量）
@pytest.fixture(scope="session")
def github_api_base():
    return "https://api.github.com"

# ---- UI: Playwright 基础页面
@pytest.fixture(scope="function")
def pw_context(page, request):
    # 出错时截图
    yield page
    if request.node.rep_call.failed:
        os.makedirs("test-results", exist_ok=True)
        page.screenshot(path=f"test-results/{request.node.name}.png")

# 在每个用例阶段结束后，pytest 会设置 rep_* 属性
def pytest_runtest_makereport(item, call):
    if "pw_context" in item.fixturenames:
        outcome = yield
        rep = outcome.get_result()
        setattr(item, "rep_" + rep.when, rep)
