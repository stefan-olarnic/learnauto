# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Selenium WebDriver test automation framework using Pytest and the Page Object Model (POM) pattern. Tests run against https://the-internet.herokuapp.com.

**GitHub repo:** https://github.com/stefan-olarnic/learnauto

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
core/base_page.py   - Base page class with WebDriverWait and retry logic
core/user.py        - User data class (username, password)
pages/              - Page Object classes
tests/              - Pytest test files
conftest.py         - Pytest fixtures (context, logged_context)
```

## Fixtures (conftest.py)

| Fixture | Descriere |
|---------|-----------|
| `context` | Creează Chrome driver, încarcă config din ENVIRONMENTS["qa"], yield Context object, quit driver la final |
| `logged_context` | Extinde `context` - face login automat și returnează context deja autentificat |

### Utilizare:
```python
# Test care necesită login manual
def test_something(context):
    page = LoginPage(context)
    page.open()
    page.login()

# Test care primește user deja logat
def test_dashboard(logged_context):
    # logged_context.driver este deja pe pagina securizată
```

## Key Patterns

- **Context Pattern**: `Context` object bundles driver, base_url, env, și valid_user. Toate page objects primesc acest context.
- **Page Object Model**: Fiecare pagină are propria clasă cu locatori ca atribute de clasă și metode pentru interacțiuni.
- **Locators**: Definite ca tuple `(By.ID, "element_id")` și unpacked cu `*locator`.
- **Explicit Waits**: `BasePage` folosește `WebDriverWait` cu timeout 10 secunde și retry pentru `StaleElementReferenceException`.

## BasePage Methods

| Metodă | Ce face |
|--------|---------|
| `find(locator)` | Găsește element cu wait și retry (3x) pentru StaleElementReferenceException |
| `click(locator)` | Așteaptă element clickable, apoi click |
| `type(locator, text)` | Clear + send_keys |
| `get_text(locator)` | Returnează textul elementului |

## Environment Config (config/config.py)

```python
ENVIRONMENTS = {
    "qa": {
        "base_url": "https://the-internet.herokuapp.com",
        "valid_user": {"username": "tomsmith", "password": "SuperSecretPassword!"}
    },
    "stage": {
        "base_url": "https://the-internet.herokuapp.com"
    }
}
```

Pentru a schimba environment-ul, modifică variabila `env` în fixture-ul `context` din conftest.py.

## Limbă

Proprietarul proiectului vorbește română. Poți comunica în română.
