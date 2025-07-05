
import csv
from models import model_currency_api
# This script reads a CSV file containing product information and stores it in a list of tuples.
# Each tuple contains the product ID, name, category, and price.
# The CSV file is expected to have a header row with the columns: id, name, category, price.



rate = model_currency_api.NBPClient().get_currency_rate('EUR')
# Initialize an empty list to store product tuples

def add_mortgage_in_percentage(price, percentage):

    return price + (price * (percentage / 100))

def product_title(product):
    return f"{product[1]} ({product[2]})"

def get_first_product_price():

    return  round(float(product_list[0][4])) if product_list else None

product_list = []

mortage = 5 # The mortgage percentage
decimals = 1

with open("secret/list_of_products.csv", encoding='utf-8') as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
   
    for row in reader:
        if len(row) < 7:
            continue
        product = (
            int(row[0]),
            row[1],
            row[2],
            row[3],
            round(add_mortgage_in_percentage(float(row[4]) * float(rate), mortage), decimals) if row[4] is not None and row[4] != '' else 0,
            float(row[5]) if row[5] is not None and row[5] != '' else 0,
            row[6].strip()
        )
        product_list.append(product)


def get_product_list():


    return product_list
