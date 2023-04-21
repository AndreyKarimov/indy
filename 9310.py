import json
from pprint import pprint

def best_saler(file_name):
    saler_value = {}
    with open(file_name, encoding='UTF-8') as file:
        data = json.load(file)
    for manager in data:
        name = ' '.join([manager['manager']['first_name'], manager['manager']['last_name']])
        sum_ = 0
        for car in manager['cars']:
            for item, value in car.items():
                sum_ += value if item == 'price' else 0
        saler_value.setdefault(name, sum_)
    the_best_saler = sorted(saler_value, key=lambda x: -saler_value[x])[0]
    print(the_best_saler, saler_value[the_best_saler])


best_saler('manager_sales.json')