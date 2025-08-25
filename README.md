[![CI](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml)

# 🚀 Github-Automation-Project

[中文](#cn-chinese) | [日本語](#jp-japanese) | [English](#en-english)

🔗 View the Latest Online HTML Test Report (GitHub Pages)
👉 [Click here](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml?query=branch%3Amain+is%3Asuccess)



🚀 CI/CD Pipeline | CI/CD パイプライン | CI/CD 流程

✅ Runs on every push → Triggers GitHub Actions workflow

✅ Installs dependencies → Python, Playwright, Browsers

✅ Runs API tests (pytest tests/api)

✅ Runs UI tests (pytest tests/ui)

✅ Generates HTML report with pytest-html

✅ Uploads artifacts (downloadable from Actions)

✅ Deploys reports to GitHub Pages (public URL)



📂 Project Structure | プロジェクト構成 | 项目结构

```bash
QA-Automation-Demo/
│── .github/workflows/ci.yml     # CI/CD workflow
│── tests/                       # Test cases
│    ├── api/                    # API tests
│    └── ui/                     # UI tests (Playwright)
│── conftest.py                  # Pytest fixtures
│── pytest.ini                   # Pytest config
│── requirements.txt             # Dependencies
│── README.md                    # Project guide
```





---

## cn-Chinese

### 📖 项目简介

这是一个基于 Pytest + Playwright 的自动化测试 Demo。
通过 GitHub Actions，在每次 push 时运行 UI/API 测试，并将测试报告同时发布为 可下载的 artifact 和 GitHub Pages 在线 HTML 报告。


### 🛠 技术栈
语言: Python 3.x

UI 自动化: Playwright

API 自动化: Pytest + Requests

报告: Allure / Pytest-HTML

CI/CD: GitHub Actions

### ⚙️ 快速开始
```bash
git clone https://github.com/dreamy936/QA-Automation-Demo.git
cd QA-Automation-Demo
python -m venv .venv
.\.venv\Scripts\activate   # Windows (PowerShell)
# source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
playwright install
pytest tests/
```

### 📝  注意事项
本地运行时请务必使用 虚拟环境 (python -m venv .venv)。

运行测试前先执行 pip install -r requirements.txt。

使用 pytest 执行时，报告会自动生成。

如果 CI 失败，请检查：

1.依赖安装 (pip install)

2.浏览器安装 (python -m playwright install --with-deps)

3.ci.yml 中的报告路径

时区已固定为 Asia/Tokyo (JST)，保持与本地时间一致。


---

## jp-japanese

### 📖 プロジェクト概要

このリポジトリは Pytest + Playwright を使った自動テストのデモです。
GitHub Actions と連携し、プッシュのたびに UI / API テストを実行し、テストレポートを アーティファクト と GitHub Pages (オンライン HTML レポート) の両方で公開します。

### 🛠 技術スタック

言語: Python 3.x

UI 自動化: Playwright

API 自動化: Pytest + Requests

レポート: Allure / Pytest-HTML

CI/CD: GitHub Actions

### ⚙️ クイックスタート
```bash
git clone https://github.com/dreamy936/QA-Automation-Demo.git
cd QA-Automation-Demo
python -m venv .venv
.\.venv\Scripts\activate   # Windows (PowerShell)
# source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
playwright install
pytest tests/
```


### 📝  注意事項
ローカル実行時は必ず 仮想環境 (python -m venv .venv) を使用してください。

テスト実行前に pip install -r requirements.txt を実行してください。

pytest を使って実行すると、レポートは自動生成されます。

CI が失敗した場合、以下を確認してください:

1.依存関係 (pip install)

2.ブラウザインストール (python -m playwright install --with-deps)

3.ci.yml 内のレポート出力パス

タイムゾーンは Asia/Tokyo (JST) に固定しています。

---

## en-english

### 📖 Project Overview

This is a demo repository for automated testing with Pytest + Playwright.
The project integrates with GitHub Actions to run UI/API tests on every push, and publishes test reports as both downloadable artifacts and GitHub Pages (online HTML reports).

### 🛠 Tech Stack

Language: Python 3.x

UI Automation: Playwright

API Automation: Pytest + Requests

Reports: Allure / Pytest-HTML

CI/CD: GitHub Actions

### ⚙️ Quick Start
```bash
git clone https://github.com/dreamy936/QA-Automation-Demo.git
cd QA-Automation-Demo
python -m venv .venv
.\.venv\Scripts\activate   # Windows (PowerShell)
# source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
playwright install
pytest tests/
```


###  📝 Notes
Always use a virtual environment when running locally (python -m venv .venv).

Run pip install -r requirements.txt before running tests.

Use pytest in PowerShell or CI; reports will be auto-generated.

If CI fails, check:

1.Dependency installation (pip install)

2.Browser installation (python -m playwright install --with-deps)

3.Report upload paths in ci.yml

Timezone is set to Asia/Tokyo (JST) for consistency with local time.

--

👩‍💻 Author: Amber  
Role: QA Enthusiast, Automation Learner  
Contact: GitHub Profile  

--

