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

if not os.path.exists('log.json'):
    with open("log.json", "w") as f:
        f.write(json.dumps({'message_id': {}}, indent=4))
        f.close()

party = dict()

def main(party_dict, cfg=config):

    products = {
        'meat': 0,
        'cucumber': 0,
        'tomato': 0,
        'potato': 0,
        'bread': 0,
        'sauce': 0,
        'coal': 0
    }
    # meat, cucumber, tomato, potato, bread, sauce = (0, 0, 0, 0, 0, 0)

    if party_dict['men'] + party_dict['women'] == 0:
        return '🤨🤨🤨 Эмм... 😑😑😑'

    for key, value in party_dict_convert(party_dict).items():

        products['meat']     += get_meat(cfg[value]['MEAT'], duration=party_dict['duration'])
        products['cucumber'] += get_cucumber(cfg[value]['CUCUMBER'], duration=party_dict['duration'])
        products['tomato']   += get_tomato(cfg[value]['TOMATO'], duration=party_dict['duration'])
        products['potato']   += get_potato(cfg[value]['POTATO'], duration=party_dict['duration'])
        products['bread']    += get_bread(cfg[value]['BREAD'], duration=party_dict['duration'])
        products['sauce']    += get_sauce(cfg[value]['SAUCE'], duration=party_dict['duration'])
    
    print(party_dict)

    products['meat']     = convert_meat(products['meat'])
    products['cucumber'] = convert_cucumber(products['cucumber'])
    products['tomato']   = convert_tomato(products['tomato'])
    products['potato']   = convert_potato(products['potato'])
    products['bread']    = convert_bread(products['bread'])
    products['sauce']    = convert_sauce(products['sauce'])
    products['coal']     = convert_coal(get_coal(cfg['COAL'], products['meat']))

    output = f"""
    Твоя порция:
    🥩 Количество мяса: {products['meat']:.1f} (кг)
    🥒 Количество огурцов: {products['cucumber']:.1f} (кг)
    🍅 Количество помидоров: {products['tomato']:.1f} (кг)
    🥔 Количество картофеля: {products['potato']:.1f} (кг)
    🍞 Количество хлеба: {products['bread']:.0f} (шт)
    🥫 Количество соуса: {products['sauce']:.0f} (шт)
    🪵 Количество угля: {products['coal']:.1f} (кг)
    """

    return output, party_dict, products

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
    # print(dict(message.json))
    party.pop(message.chat.id, None)
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
    party[message.chat.id] = {}
    party[message.chat.id]['duration'] = 'long' if message.text == 'Больше 5 часов' else 'short'
    text = """
    \n
    Введите количество мужчин 👨
    """
    bot.send_message(message.chat.id, text, reply_markup=types.ReplyKeyboardRemove())

# Handle number of women
@bot.message_handler(
    func=lambda message: (
        message.text.isdigit() 
        and party[message.chat.id].get('men') is None 
        and party[message.chat.id].get('duration') is not None
        ), 
    content_types=['text']
    )
def enter_women(message):
    party[message.chat.id]['men'] = int(message.text)
    text = """
    \n
    Введите количество женщин 👩
    """
    bot.send_message(message.chat.id, text)

# Calculation
@bot.message_handler(
    func=lambda message: (
        message.text.isdigit() 
        and party[message.chat.id].get('women') is None 
        and party[message.chat.id].get('men') is not None 
        and party[message.chat.id].get('duration') is not None
        ), 
    content_types=['text']
    )
def get_calculation(message):
    party[message.chat.id]['women'] = int(message.text)

    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, 
        row_width=1, 
        )
    again_btn = types.KeyboardButton('Сделать новый расчет 🔁')
    markup.add(again_btn)

    results = main(party_dict=party[message.chat.id], cfg=config)
    bot.send_message(message.chat.id, results[0], reply_markup=markup)
    write_json(dict(message.json), results[1], results[2], filename='log.json')

# Again Calculation
@bot.message_handler(
    func=lambda message: message.text == 'Сделать новый расчет 🔁', 
    content_types=['text']
    )
def start_again(message):
    start(message)

if __name__ == "__main__":

    print("Bot has been started")
    bot.infinity_polling()