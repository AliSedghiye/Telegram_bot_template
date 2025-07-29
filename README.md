# Telegram_bot_template
A Telegram bot template built with Python, ideal for rapid bot development.

## MongoDB 

1. Install pymongo if not already:
    ```
    pip install pymongo
    ```

## how to run 

1. set your telegram bot token as environment variable `PYTEL_TOKEN` :
    ```
    export PYTEL_TOKEN=<your_telegram_bot_token>
    ```

2. Add `src` to `PYTHONPATH`:
    ```
    export PYTHONPATH=${pwd}
    ```

3. run:
    ```
    python src/pytel.py
    ```