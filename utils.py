import json
from math import ceil
import datetime, time


def get_meat(basis, body_type='m', duration='short'):
    dur_coeff = 1 if duration == 'short' else 1.15
    bt_coeff = 1 if body_type == 'm' else 1 if body_type == 's' else 1
    return bt_coeff * dur_coeff * basis / 1000


def get_cucumber(basis, body_type='m', duration='short'):
    dur_coeff = 1 if duration == 'short' else 1.15
    bt_coeff = 1 if body_type == 'm' else 1 if body_type == 's' else 1
    return bt_coeff * dur_coeff * basis / 1000


def get_tomato(basis, body_type='m', duration='short'):
    dur_coeff = 1 if duration == 'short' else 1.15
    bt_coeff = 1 if body_type == 'm' else 1 if body_type == 's' else 1
    return bt_coeff * dur_coeff * basis / 1000


def get_potato(basis, body_type='m', duration='short'):
    dur_coeff = 1 if duration == 'short' else 1.15
    bt_coeff = 1 if body_type == 'm' else 1 if body_type == 's' else 1
    return bt_coeff * dur_coeff * basis / 1000


def get_bread(basis, body_type='m', duration='short'):
    dur_coeff = 1 if duration == 'short' else 1.15
    bt_coeff = 1 if body_type == 'm' else 1 if body_type == 's' else 1
    return bt_coeff * dur_coeff * basis / 100


def get_sauce(basis, body_type='m', duration='short'):
    dur_coeff = 1 if duration == 'short' else 1.15
    bt_coeff = 1 if body_type == 'm' else 1 if body_type == 's' else 1
    return bt_coeff * dur_coeff * basis / 100


def get_coal(basis, meat):
    return (basis / 1000) * meat


def convert_meat(meat):
    return ((round(meat, 3) // 0.5) + 1) / 2


def convert_cucumber(cucumber):
    return ((round(cucumber, 3) // 0.1) + 1) / 10

    
def convert_tomato(tomato):
    return ((round(tomato, 3) // 0.1) + 1) / 10

    
def convert_potato(potato):
    return ((round(potato, 3) // 0.2) + 1) / 5

    
def convert_bread(bread):
    return ceil(round(bread, 3))

    
def convert_sauce(sauce):
    return ceil(round(sauce, 2))

    
def convert_coal(meat):
    return ceil(round(meat, 2))


def party_dict_convert(party_dict: dict):
    man_dict = dict.fromkeys(
        range(party_dict['men']), 
        'MAN'
        )
    woman_dict = dict.fromkeys(
        range(party_dict['men'], party_dict['men'] + party_dict['women']), 
        'WOMAN'
        )
    man_dict.update(woman_dict)
    
    return man_dict

def write_json(json_message, input_dict, output_dict, filename='log.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        mess_id = json_message['message_id']

        file_data['message_id'][mess_id] = {}
        file_data['message_id'][mess_id]['user'] = {}
        file_data['message_id'][mess_id]['user']['user_id'] = json_message['from'].get('id', "")
        file_data['message_id'][mess_id]['user']['first_name'] = json_message['from'].get('first_name', "")
        file_data['message_id'][mess_id]['user']['last_name'] = json_message['from'].get('last_name', "")
        file_data['message_id'][mess_id]['user']['username'] = json_message['from'].get('username', "")
        file_data['message_id'][mess_id]['user']['language_code'] = json_message['from'].get('language_code', "")
        file_data['message_id'][mess_id]['user']['is_bot'] = json_message['from'].get('is_bot', "")
        file_data['message_id'][mess_id]['user']['date'] = str(
            (datetime.datetime.utcfromtimestamp(json_message['date']) + datetime.timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')
            ) 

        file_data['message_id'][mess_id]['input'] = input_dict
        file_data['message_id'][mess_id]['output'] = output_dict         
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

if __name__ == "__main__":
    t = {'qwerty': 1, 'zxcv': 2}

    print(t.get('qwerty'))
    print(t.get('asdf'))



    