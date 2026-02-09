        # FeedbackFormBot — заявки и обратная связь

        **Бренд:** Вячеслав Ветошкин · **Сайт:** https://1vetoshkin.ru · **Telegram:** https://t.me/TkAs007bot  
        **Дата сборки:** 2025-10-21

        ## Коротко
        Принимайте обращения клиентов в один клик и не теряйте заявки.

        ## Ключевые функции
        - Сбор заявок в SQLite
- Быстрый ответ пользователю
- Простой экспорт заявок
- Готов к Docker‑деплою

        ## Где применить
        - Форма обратной связи сайта
- Личные заказы в Telegram
- Прием баг‑репортов

        ## Что внутри
        - `app/` (handlers, services, database)
        - `requirements.txt`, `Dockerfile`, `docker-compose.yml`
        - `.env.example` (минимальные настройки)
        - `README.md` (тех. установка), **README_STORE.md** (для витрины)

        ## Быстрый старт
        ```bash
        python -m venv .venv && source .venv/bin/activate
        pip install -r requirements.txt
        python app/main.py
        # или
        docker-compose up -d --build
        ```

        ## Скриншоты (заглушки)
        Сохраните скриншоты в `docs/screenshots/1.png`, `2.png`, `3.png`, затем вставьте в карточку товара.

        ## Поддержка
        Вопросы и помощь: https://t.me/TkAs007bot

        ---
        © 2025 Вячеслав Ветошкин. Использование разрешено покупателю на один проект (Single Use). Расширенную лицензию запросите в личке.
