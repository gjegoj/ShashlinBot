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
$ echo "API_KEY: <your Telegram API_KEY>" > .env
```
4. Run Bot:
```bash
$ python main.py
```

## Versions

1. ShashlinBot_v1. Pushed to Github.
2. ShashlinBot_v1.1. Changed config. Added duration coefficient. Created body type coefficient and /help command.
