import os
import yaml
import telebot
from telebot import types
from utils import *
from dotenv import load_dotenv

load_dotenv()  

CONFIG_PATH = 'config.yaml'
TOKEN = os.getenv('API_KEY')

bot = telebot.TeleBot(TOKEN)

with open(CONFIG_PATH, "r") as stream:
    config = yaml.safe_load(stream)

party = dict()

def main(party, cfg=config):

    meat, cucumber, tomato, potato, bread, sauce = (0, 0, 0, 0, 0, 0)

    for key, value in party_dict_convert(party).items():

        meat     += get_meat(cfg[value]['MEAT'], duration=party['duration'])
        cucumber += get_cucumber(cfg[value]['CUCUMBER'], duration=party['duration'])
        tomato   += get_tomato(cfg[value]['TOMATO'], duration=party['duration'])
        potato   += get_potato(cfg[value]['POTATO'], duration=party['duration'])
        bread    += get_bread(cfg[value]['BREAD'], duration=party['duration'])
        sauce    += get_sauce(cfg[value]['SAUCE'], duration=party['duration'])

    print(
        f"""
        meat: {meat}
        cucumber: {cucumber}
        tomato: {tomato}
        potato: {potato}
        bread: {bread}
        sauce: {sauce}
        """
        )

    meat     = convert_meat(meat)
    cucumber = convert_cucumber(cucumber)
    tomato   = convert_tomato(tomato)
    potato   = convert_potato(potato)
    bread    = convert_bread(bread)
    sauce    = convert_sauce(sauce)
    coal     = convert_coal(get_coal(cfg['COAL'], meat))

    output = f"""
    Твоя порция:
    🥩 Количество мяса: {meat:.1f} (кг)
    🥒 Количество огурцов: {cucumber:.1f} (кг)
    🍅 Количество помидоров: {tomato:.1f} (кг)
    🥔 Количество картофеля: {potato:.1f} (кг)
    🍞 Количество хлеба: {bread:.0f} (шт)
    🥫 Количество соуса: {sauce:.0f} (шт)
    🪵 Количество угля: {coal:.1f} (кг)
    """

    return output

# Handle help command
@bot.message_handler(commands=['help'])
def help(message):
    text = """
    \n
    ❗ здесь будет уточняющая информацию по продуткам и вся доп инфа.
    """

    bot.send_message(message.chat.id, text)

# Handle duration
@bot.message_handler(commands=['start'])
def start(message):
    party.clear()
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, 
        row_width=1, 
        )
    long_btn = types.KeyboardButton('Больше 5 часов')
    short_btn = types.KeyboardButton('Меньше 3 часов')
    text = """
    \n
    Выберите длительность 🕓
    """
    # 💡 Короткая посиделка
    # 💡 Длительная посиделка

    markup.add(short_btn, long_btn)

    bot.send_message(message.chat.id, text, reply_markup=markup)

# Handle number of men
@bot.message_handler(
    func=lambda message: message.text in ['Меньше 3 часов', 'Больше 5 часов'], 
    content_types=['text']
    )
def enter_men(message):
    party['duration'] = 'long' if message.text == 'Больше 5 часов' else 'short'
    text = """
    \n
    Введите количество мужчин 👨
    """
    bot.send_message(message.chat.id, text, reply_markup=types.ReplyKeyboardRemove())

# Handle number of women
@bot.message_handler(
    func=lambda message: (
        message.text.isdigit() 
        and party.get('men') is None 
        and party.get('duration') is not None
        ), 
    content_types=['text']
    )
def enter_women(message):
    party['men'] = int(message.text)
    text = """
    \n
    Введите количество женщин 👩
    """
    bot.send_message(message.chat.id, text)

# Calculation
@bot.message_handler(
    func=lambda message: (
        message.text.isdigit() 
        and party.get('women') is None 
        and party.get('men') is not None 
        and party.get('duration') is not None
        ), 
    content_types=['text']
    )
def get_calculation(message):
    party['women'] = int(message.text)

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, 
        row_width=1, 
        )
    again_btn = types.KeyboardButton('Сделать новый расчет 🔁')
    markup.add(again_btn)

    bot.send_message(message.chat.id, main(party=party, cfg=config), reply_markup=markup)

# Again Calculation
@bot.message_handler(
    func=lambda message: message.text == 'Сделать новый расчет 🔁', 
    content_types=['text']
    )
def start_again(message):
    start(message)

if __name__ == "__main__":

    bot.infinity_polling()