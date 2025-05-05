# Code Analyzer Tool

A simple web-based tool built with Streamlit to analyze Python code for various issues. It integrates multiple code quality checks including metrics analysis, security checks, style enforcement, and AI-assisted code review.

## Features
- **Code Metrics**: Provides basic code metrics, maintainability index, and Halstead metrics.
- **Security Checks**: Scans the code for potential security issues, Utilizing Bandit for this check.
- **Code Style**: Identifies PEP 8 style violations, Utilizing Flake8 for this check.
- **AI Code Review**: Uses an AI-powered review to provide code suggestions based on issues found, utilizing Qwen2.5-coder as the LLM.

## Requirements
- Python 3.7+
- Streamlit
- Radon
- Bandit
- Flake8
- Langchain_ollama

You can install the necessary dependencies using pip:

```bash
pip install streamlit radon bandit flake8 langchain_ollama


