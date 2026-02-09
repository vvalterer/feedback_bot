# 🤖 Feedback Form Bot

[![CI](https://github.com/vvalterer/feedback_bot/actions/workflows/ci.yml/badge.svg)](https://github.com/vvalterer/feedback_bot/actions/workflows/ci.yml)

Telegram-бот для сбора заявок и обратной связи.

**Бренд:** Вячеслав Ветошкин · [1vetoshkin.ru](https://1vetoshkin.ru) · [Telegram](https://t.me/TkAs007bot)

---

## 🚀 Быстрый запуск

### Локально
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Заполните BOT_TOKEN и ADMIN_IDS
python app/main.py
```

### Docker
```bash
docker-compose up -d --build
```

---

## 📦 Структура проекта

```
feedback_bot/
├── app/
│   ├── main.py           # Entry point
│   ├── config.py         # Pydantic Settings
│   ├── handlers/         # Обработчики команд
│   │   ├── feature.py    # Сохранение заявок
│   │   └── help_text.py  # /start, /help
│   └── database/         # Слой данных (aiosqlite)
│       ├── models.py     # Инициализация БД
│       └── requests.py   # CRUD операции
├── tests/                # pytest + pytest-asyncio
├── .github/workflows/    # GitHub Actions CI
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── pytest.ini
```

---

## 🧩 Настройки (.env)

```ini
BOT_TOKEN=your_bot_token_here
ADMIN_IDS=123456789,987654321
DB_PATH=data/database.sqlite3
LOG_LEVEL=INFO
```

---

## 🧪 Тестирование

```bash
pytest tests/ -v
```

---

## 📋 Технологии

| Компонент | Технология |
|-----------|------------|
| Framework | aiogram 3.4.1 |
| Database | aiosqlite 0.20.0 |
| Config | pydantic-settings 2.1.0 |
| Testing | pytest 8.0.0 |
| CI/CD | GitHub Actions |

---

## ✅ Функции

- `/start` — приветствие
- `/help` — справка
- Любое сообщение → сохранение заявки в БД + уведомление админов

---

© 2025 Вячеслав Ветошкин
