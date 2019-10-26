import json
import requests


with open('./ref.json') as my_json:
    read_content = json.load(my_json)

def data_parser(data):
    items_list = data['order']['items']
    my_dict = {}
    total_cost = 0
    total_vat = 0
    curr_rate = currency_rate(data['order']['currency'])
    curr_rate = round(float(curr_rate),2)

    for eachItem in items_list:
        qty = eachItem['quantity']
        for key, value in eachItem.items():
            if key == 'product_id':
                pid, cost, band = price_checker(value)
                cost = cost * qty
                adj_cost = cost * curr_rate
                total_cost += adj_cost
                vat = vat_checker(band)
                vat = cost * vat
                adj_vat = vat * curr_rate
                total_vat += adj_vat
                my_dict[pid] = {"cost": round(adj_cost), "vat": round(adj_vat)}

    return_list = {f"{data['order']['id']}" : my_dict, "total_cost" : round(total_cost), "total_vat" : round(total_vat)}
    return return_list


def price_checker(key):
    price_list = read_content['prices']
    return_list = [x for x in price_list if x['product_id'] == key]
    for eachItem in return_list:
        for key, value in eachItem.items():
            if key == 'product_id':
                pid = value
            elif key == 'price':
                cost = value
            elif key == 'vat_band':
                band = value

    return pid, cost, band


def vat_checker(band):
    vat_list = read_content[f'vat_bands']
    for key, value in vat_list.items():
        if key == band:
            return value

def currency_rate(var):
    res = requests.get(f"https://api.exchangeratesapi.io/latest?base=GBP")
    res = res.json()
    res = res['rates']
    for key, val in res.items():
        if key == f'{var}':
            return str(val)
