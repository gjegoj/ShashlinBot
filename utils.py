from math import ceil


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
    