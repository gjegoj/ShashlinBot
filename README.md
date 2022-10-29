# ShashlinBot

## Getting started

1. Create new environment and activate it:
```bash
$ python -m venv <env_name>
$ source <env_name>/bin/activate
```
2. Download and install all required packages:
```bash
$ pip install -r requirements.txt
```
3. Add your Telegram API_KEY:
```bash
$ touch .env
$ echo "API_KEY = <your Telegram API_KEY>" > .env
```
4. Run Bot:
```bash
$ python main.py
```

## Versions

1. **04/June/2022**. ShashlinBot_v1. Pushed to Github.
2. **15/July/2022**. ShashlinBot_v1.1. Changed config. Added duration coefficient. Created body type coefficient and /help command.
3. **15/Aug/2022**. ShashlinBot_v1.2. Changed party dictionary - added chat_id as key. Fixed 0 men and 0 women.
4. **29/Oct/2022**. ShashlinBot_v1.3. Added logging.
