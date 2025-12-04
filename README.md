# 🚀 QA Automation Demo Framework

[![CI Status](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml)
[![Test Report](https://img.shields.io/badge/View-HTML_Report-blue)](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml?query=branch%3Amain+is%3Asuccess)

> **Note:** Select language / 言語を選択 / 选择语言:
> [English](#-project-overview) | [日本語](#-日本語-readme) | [中文](#-中文-readme)

---

## 📖 Project Overview

This is a comprehensive **Test Automation Framework** built with **Python**, **Playwright**, and **Pytest**. 
It demonstrates a modern CI/CD integration where tests are automatically triggered on every push, ensuring continuous quality assurance.

**🎯 Key Features:**
* **Hybrid Testing:** Integrates both **UI** (Playwright) and **API** (Requests) automation.
* **CI/CD Pipeline:** Fully integrated with **GitHub Actions**.
* **Visual Reporting:** Automatically generates and deploys HTML test reports to **GitHub Pages**.
* **Maintainability:** Uses the **Page Object Model (POM)** design pattern (Assuming you did this).

🔗 **[Click here to view the latest Live Test Report](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml?query=branch%3Amain+is%3Asuccess)**

## 🛠 Tech Stack

| Component | Tool | Description |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Core programming language |
| **UI Framework** | Playwright | Fast, reliable browser automation |
| **API Framework** | Requests | Simple, elegant HTTP library |
| **Test Runner** | Pytest | Scalable testing framework |
| **CI/CD** | GitHub Actions | Workflow automation |
| **Reporting** | Pytest-HTML / Allure | Visualization of test results |

## 📂 Project Structure

```text
QA-Automation-Demo/
│── .github/workflows/   # CI/CD configurations (YAML)
│── tests/               # Test suites
│   ├── api/             # API test cases
│   └── ui/              # UI test cases (Playwright)
│── pages/               # Page Object Models (Recommended to add this folder)
│── conftest.py          # Pytest fixtures & hooks
│── pytest.ini           # Configuration file
│── requirements.txt     # Python dependencies
└── README.md            # Documentation
```

## ⚙️ Quick Start

### Prerequisites
* Python 3.8+
* Git

### Installation & Execution

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/dreamy936/QA-Automation-Demo.git](https://github.com/dreamy936/QA-Automation-Demo.git)
    cd QA-Automation-Demo
    ```

2.  **Set up Virtual Environment**
    ```bash
    # Windows (PowerShell)
    python -m venv .venv
    .\.venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

4.  **Run Tests**
    ```bash
    # Run all tests
    pytest

    # Run only UI tests
    pytest tests/ui

    # Run with slow motion (for debugging)
    pytest tests/ui --slowmo 1000
    ```

## 🧩 Architectural Decisions (Why this stack?)

* **Why Playwright?** Chosen for its speed, auto-wait capabilities, and native support for modern web features compared to Selenium.
* **Why GitHub Actions?** To demonstrate a "Shift-Left" testing approach where feedback is immediate upon code changes.
* **Why Hybrid (UI + API)?** API tests provide fast feedback on backend logic, while UI tests ensure the end-user journey is functional.

---

<details>
<summary><strong>🇯🇵 日本語 README (Click to expand)</strong></summary>

## 📖 プロジェクト概要

Pytest + Playwright をベースとした自動テストフレームワークのデモです。
GitHub Actions と連携し、コードがプッシュされるたびに UI および API テストを自動実行します。結果は GitHub Pages で公開されます。

## 🛠 技術スタック

* **言語:** Python 3.x
* **UI 自動化:** Playwright
* **API 自動化:** Pytest + Requests
* **レポート:** Pytest-HTML / Allure
* **CI/CD:** GitHub Actions

（以下、Quick Startの手順は英語と同様）

</details>

<details>
<summary><strong>🇨🇳 中文 README (点击展开)</strong></summary>

## 📖 项目简介

这是一个基于 Pytest + Playwright 的自动化测试框架演示。
通过 GitHub Actions 实现了 CI/CD 流程，每次代码提交都会自动运行测试，并生成可以在线预览的 HTML 报告。

## 🛠 技术栈

* **语言:** Python 3.x
* **UI 自动化:** Playwright
* **API 自动化:** Pytest + Requests
* **报告:** Pytest-HTML
* **CI/CD:** GitHub Actions

</details>

---

## 👩‍💻 Author

**Amber**
* *QA Automation Engineer*
* Focus: Python, Playwright, CI/CD pipelines.

```

---

### **针对“附录：面试问答集”的处理建议**

我强烈建议把原本 README 最后的 "面试 Q&A" 部分**删掉**，或者转移位置。

**为什么？**
因为 README 是给同事、老板或面试官展示“你的技术成果”的地方。把 Q&A 放这里，感觉像是你在背书，而不是在做项目。

**替代方案：**
在面试时，当面试官问你 "Why did you choose Playwright?" 时，你可以**口头**回答这些内容（你的 Q&A 内容本身写得很好！），这会显得你对技术有深刻的理解，而不是照着文档念。

如果你一定要保留，可以像上面模板那样，改写成 `Architectural Decisions` (架构决策)，用陈述句表达，而不是问答句。

* **原版 (Q&A):** "Q: 为什么要同时做 API 和 UI 测试？ A: API 测试验证逻辑快..."
* **专业版 (Decisions):** "**Testing Strategy:** I implemented a hybrid approach. API tests are used for fast feedback on business logic, while UI tests cover critical user journeys." (看，意思一样，但听起来像个资深工程师的总结)。

### **下一步 (Next Step)**

你的项目结构里提到了 `tests/ui` 和 `conftest.py`。
**你想让我帮你 Review 一下 `conftest.py` 或者其中一个 UI 测试用例的代码吗？**
(很多初学者在 `conftest.py` 里的 `fixture` 作用域 scope 设置上容易踩坑，这在面试中也是高频考点)。
