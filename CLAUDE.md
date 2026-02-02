# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Selenium WebDriver test automation framework using Pytest and the Page Object Model (POM) pattern. Tests run against https://the-internet.herokuapp.com.

## Commands

```bash
# Run all tests
pytest

# Run a single test
pytest tests/test_login.py::test_valid_login

# Run with HTML report
pytest --html=report.html

# Run with verbose output
pytest -v
```

## Architecture

```
config/config.py    - Environment configurations (QA, Stage) with base URLs and test users
core/context.py     - Context object holding driver, base_url, env, and valid_user
core/base_page.py   - Base page class with common methods (find, click, type, get_text)
core/user.py        - User data class
pages/              - Page Object classes (inherit from BasePage or use Context)
tests/              - Pytest test files
conftest.py         - Pytest fixtures (context fixture creates Chrome driver)
```

## Key Patterns

- **Context Pattern**: The `context` fixture (conftest.py) creates a Context object that bundles driver, environment config, and test user. All page objects receive this context.
- **Page Object Model**: Each page has its own class with locators as class attributes (tuples of By strategy and value) and methods for page interactions.
- **Locators**: Defined as tuples `(By.ID, "element_id")` and unpacked with `*locator` in find_element calls.

## Environment Selection

Currently hardcoded to "qa" in conftest.py. To change environment, modify the `env` variable in the context fixture.
