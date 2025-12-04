# 🚀 QA Automation Demo Framework

[![CI Status](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml)
[![Test Report](https://img.shields.io/badge/View-HTML_Report-blue)](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml?query=branch%3Amain+is%3Asuccess)

> **Note:** Select language / 言語を選択 / 选择语言:
> [English](#en) | [日本語](#jp) | [中文](#cn)

---

<span id="en"></span>
## 📖 Project Overview

This is a comprehensive **Test Automation Framework** built with **Python**, **Playwright**, and **Pytest**. 
It demonstrates a modern CI/CD integration where tests are automatically triggered on every push, ensuring continuous quality assurance.

**🎯 Key Features:**
* **Hybrid Testing:** Integrates both **UI** (Playwright) and **API** (Requests) automation.
* **CI/CD Pipeline:** Fully integrated with **GitHub Actions**.
* **Visual Reporting:** Automatically generates and deploys HTML test reports to **GitHub Pages**.

🔗 **[Click here to view the latest Live Test Report](https://github.com/dreamy936/QA-Automation-Demo/actions/workflows/ci.yml?query=branch%3Amain+is%3Asuccess)**

## 🛠 Tech Stack

| Component | Tool | Description |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Core programming language |
| **UI Framework** | Playwright | Fast, reliable browser automation |
| **API Framework** | Requests | Simple, elegant HTTP library |
| **Test Runner** | Pytest | Scalable testing framework |
| **CI/CD** | GitHub Actions | Workflow automation |

## ⚙️ Quick Start

### Installation & Execution

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/dreamy936/QA-Automation-Demo.git](https://github.com/dreamy936/QA-Automation-Demo.git)
    cd QA-Automation-Demo
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

3.  **Run Tests**
    ```bash
    pytest
    ```

---

<span id="jp"></span>
<details>
<summary><strong>🇯🇵 日本語 README (Click to expand)</strong></summary>

## 📖 プロジェクト概要

Pytest + Playwright をベースとした自動テストフレームワークのデモです。
GitHub Actions と連携し、コードがプッシュされるたびに UI および API テストを自動実行します。結果は GitHub Pages で公開されます。

## 🛠 技術スタック

* **言語:** Python 3.x
* **UI 自動化:** Playwright
* **API 自動化:** Pytest + Requests
* **レポート:** Pytest-HTML
* **CI/CD:** GitHub Actions

</details>

<span id="cn"></span>
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
