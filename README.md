[![CI](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml)


---

🔗 [Appendix Q&A](#-附录面试问答集-interview-qa)


# 🚀 Github-Automation-Project

[中文](#cn-chinese) | [日本語](#jp-japanese) | [English](#en-english)

🔗 View the Latest Online HTML Test Report (GitHub Pages)
👉 [Click here](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml?query=branch%3Amain+is%3Asuccess)



### 🚀 CI/CD Pipeline | CI/CD パイプライン | CI/CD 流程

✅ Runs on every push → Triggers GitHub Actions workflow

✅ Installs dependencies → Python, Playwright, Browsers

✅ Runs API tests (pytest tests/api)

✅ Runs UI tests (pytest tests/ui)

✅ Generates HTML report with pytest-html

✅ Uploads artifacts (downloadable from Actions)

✅ Deploys reports to GitHub Pages (public URL)



### 📂 Project Structure | プロジェクト構成 | 项目结构

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


📌 附录：面试问答集 (面接Q&A / Interview Q&A)
Q1: 这个项目是做什么的？

中文 👉 一个基于 GitHub Actions 的自动化测试 Demo，集成了 API 测试和 UI 测试，每次 push 自动运行并生成 HTML 报告。

日本語 👉 GitHub Actions ベースの自動テストデモで、APIテストとUIテストを統合し、pushごとに自動実行してHTMLレポートを生成します。

English 👉 An automation testing demo based on GitHub Actions, integrating API & UI tests, runs automatically on each push and generates HTML reports.


Q2: 为什么要同时做 API 和 UI 测试？

中文 👉 API 测试验证逻辑快，UI 测试保证交互正常，互补性强。

日本語 👉 APIテストはロジック確認が速く、UIテストは操作フローの正常性を保証し、補完的です。

English 👉 API tests validate logic quickly, UI tests ensure interactions work properly — they complement each other.


Q3: 测试结果如何可视化？

中文 👉 用 pytest-html 生成 HTML 报告，并通过 GitHub Actions 上传到 Artifacts / Pages 在线查看。

日本語 👉 pytest-html でHTMLレポートを生成し、GitHub Actionsで Artifacts / Pages にアップロードしてオンラインで確認します。

English 👉 Reports are generated with pytest-html and published via GitHub Actions to Artifacts / Pages for online viewing.


Q4: 在项目中最大的收获是什么？

中文 👉 学会把自动化测试融入 CI/CD，让测试成为持续集成的一部分。

日本語 👉 自動テストをCI/CDに組み込み、継続的インテグレーションの一部にできたことです。

English 👉 Learned to integrate automated testing into CI/CD, making testing part of continuous integration.




Q5: 如果测试失败了如何排查？

中文 👉 查看 CI 日志，结合截图/trace，在本地复现同样命令。

日本語 👉 CIログを確認し、スクリーンショットやtraceを利用して、ローカルで再現します。

English 👉 Check CI logs, use screenshots/trace, and reproduce locally with the same command.


Q6: 为什么选 Pytest+Requests / Playwright？

中文 👉 这是实际项目常用组合：Requests 写 API，Pytest 框架灵活，Playwright UI 自动化现代高效。

日本語 👉 実プロジェクトでよく使われる組み合わせ：RequestsはAPI、Pytestは柔軟なフレームワーク、Playwrightはモダンで効率的なUI自動化。

English 👉 A common real-world stack: Requests for API, Pytest for flexibility, Playwright for modern efficient UI automation.


Q7: CI/CD 是什么？

中文 👉 CI/CD = 持续集成 / 持续交付，本项目属于持续集成（CI）。

日本語 👉 CI/CD = 継続的インテグレーション / 継続的デリバリー、このプロジェクトはCI部分に当たります。

English 👉 CI/CD = Continuous Integration / Continuous Delivery, this project focuses on CI.


Q8: 项目工作原理 / 意义是什么？

中文 👉 Push → 触发 CI → 跑测试 → 生成报告 → 发布 GitHub Pages；保证代码变更不破坏功能。

日本語 👉 Push → CIトリガー → テスト実行 → レポート生成 → GitHub Pages公開；コード変更が機能を壊さないようにします。

English 👉 Push → Trigger CI → Run tests → Generate report → Publish via GitHub Pages; ensures changes don’t break features.


Q9: “每次 push 都会运行测试”是所有仓库吗？

中文 👉 不是，只对这个仓库（QA-Automation-Demo）生效，除非其他仓库也配置了 CI。

日本語 👉 いいえ、このリポジトリ（QA-Automation-Demo）のみに適用され、他のリポジトリはCIを設定しない限り動きません。

English 👉 No, only this repository (QA-Automation-Demo) runs tests, unless other repos also have CI configured.

--

👩‍💻 Author: Amber  
Role: QA Enthusiast, Automation Learner  
Contact: GitHub Profile  
