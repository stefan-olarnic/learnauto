# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Selenium WebDriver test automation framework using Pytest + pytest-bdd (BDD/Gherkin) and the Page Object Model (POM) pattern. Tests run against OrangeHRM: https://opensource-demo.orangehrmlive.com

**GitHub repo:** https://github.com/stefan-olarnic/learnauto

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Commands

```bash
# Activează venv înainte de orice comando
venv\Scripts\activate

# Rulează toate testele
pytest -v

# Rulează testele BDD
pytest tests/step_defs/test_login_steps.py -v

# Rulează un singur test
pytest tests/step_defs/test_login_steps.py::test_name -v

# Raport HTML
pytest --html=report.html
```

## Structura Proiectului

```
learn py/
├── conftest.py                  # Fixtures globale (context, logged_context) — rămâne în root
├── requirements.txt             # Dependențele pachetelor — rămâne în root
├── .gitignore                   # Excludere venv/, __pycache__, etc.
├── CLAUDE.md                    # Asta
├── config/
│   └── config.py                # ENVIRONMENTS dict (base_url, valid_user per env)
├── core/
│   ├── base_page.py             # BasePage — WebDriverWait, retry, metode comune
│   ├── context.py               # Context class (driver, base_url, env, valid_user)
│   └── user.py                  # User class (username, password)
├── pages/
│   └── login/
│       ├── __init__.py          # Exportează LoginPage și LOCATORS
│       ├── login_page.py        # Clasa LoginPage (moștenește BasePage)
│       └── login_locators.py    # LOCATORS dictionary cu toți locatorii
├── tests/
│   ├── features/
│   │   └── login.feature        # Scenarii Gherkin (Scenario Outline)
│   ├── step_defs/
│   │   └── test_login_steps.py  # Step definitions (given/when/then)
│   └── exemplu_test.py          # Exemplu test cu logged_context fixture
└── venv/                        # Virtual environment (în .gitignore)
```

## Fixtures (conftest.py)

| Fixture | Descriere |
|---------|-----------|
| `context` | Creează Chrome driver, încarcă config din ENVIRONMENTS["qa"], yield Context, quit driver la final |
| `logged_context` | Extinde `context` — face login automat cu valid_user, returnează context deja autentificat |

```python
# Test care face login manual
def test_something(context):
    page = LoginPage(context)
    page.open()
    page.login()

# Test care primește user deja logat
def test_dashboard(logged_context):
    # logged_context.driver este deja logat
```

## BDD / Gherkin

Testele folosesc **pytest-bdd** cu **Scenario Outline** pentru a rula același test cu date diferite.

### login.feature — scenarii în Gherkin:
- `Given` — pregătire (deschide pagina)
- `When` — acțiune (login cu credențiale)
- `Then` — verificare (mesajul așteptat)
- `Scenario Outline` + `Examples` table = un template rulat pentru fiecare linie din tabel

### test_login_steps.py — step definitions:
- `scenarios('../features/login.feature')` — încarcă scenariile
- `@given / @when / @then` — leagă step-urile Gherkin de cod Python
- `parsers.parse()` — extrage valorile din ghilimele din .feature

## Page Object Model + Locators

### Structura pages/:
Fiecare pagină are un subfolder propriu:
```
pages/
  login/
    __init__.py          # Exportează LoginPage și LOCATORS
    login_page.py        # Clasa cu metode (open, login, get_message)
    login_locators.py    # LOCATORS dictionary
```

### Locators — strategie:
- **Input fields** → `By.NAME` (câmpurile au atribut `name` pentru form submission)
- **Butonul submit** → `By.CSS_SELECTOR` cu `button[type='submit']` (butonele nu au `name`)
- **Mesaje/alerte** → `By.CSS_SELECTOR` cu class-ul specific

### LOCATORS dictionary:
Toți locatorii sunt într-un singur dict în `login_locators.py`. Accesați cu `LOCATORS["key"]`.

### LoginPage moștenește BasePage:
- `super().__init__(context)` — setează self.context, self.driver, self.wait din BasePage
- Folosește metode din BasePage: `self.type()`, `self.click()`, `self.find()` — au WebDriverWait (10s) și retry

## BasePage Methods (core/base_page.py)

| Metodă | Ce face |
|--------|---------|
| `find(locator)` | WebDriverWait + retry 3x pentru StaleElementReferenceException |
| `click(locator)` | Așteaptă element clickable, apoi click |
| `type(locator, text)` | find + clear + send_keys |
| `get_text(locator)` | Returnează textul elementului |

## Environment Config (config/config.py)

- `base_url` — doar domeniul (ex: `https://opensource-demo.orangehrmlive.com`)
- Path-urile specifice paginilor sunt în page objects (ex: `+ "/web/index.php/auth/login"`)
- Schimba environment-ul prin variabila `env` în fixture-ul `context` din conftest.py

## Limbă

Proprietarul proiectului vorbește română. Comunică în română.
