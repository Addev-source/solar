# app.py
from flask import Flask, render_template, request
# Import necessary modules and classes
# Initialize the Flask application
import models.model_products as model_products
from models.model_contact_form import ContactFormSender
from models.model_redirect import data_processor
import logging
logging.basicConfig(level=logging.INFO)
from helper import comtap

help = comtap.local_temp()


app = Flask(__name__)

SMTP_CFG = {
    'smtp_server':   'serwer2518763.home.pl',
    'smtp_port':     587,  # lub 465 jeśli wolisz SSL
    'smtp_user':     'biuro@solarnedachy.eu',
    'smtp_password': 'solar8375001onboard'
}

get_product = model_products.get_product_list



@app.errorhandler(404)
def handle_exception(e):
    return render_template('error_404.html')


@app.route('/', methods=['GET'])

def index():
    """Render the index page with the current Euro price."""
    first_product_price = model_products.get_first_product_price()
    return render_template('index.html', first_product=first_product_price)


@app.route('/about')
def about():
    return render_template(
        'about.html',
        active_page='about')

@app.route('/shop', methods=['GET', 'POST'])
def shop():
    return render_template(
        'shop.html',
        product_table=get_product(),
        active_page='shop')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    success = None
    error   = []

    if request.method == 'POST':
        form_data = request.form.to_dict()
        # Tworzysz instancję z full configiem SMTP
        form = ContactFormSender(form_data, **SMTP_CFG)

        # Dodatkowe przetwarzanie danych, jeśli potrzebne
        data_processor().process(form_data)

        # Pobierz listę ewentualnych błędów
        errors = form.error_name_message()
        if not errors:
            # brak walidacyjnych błędów → próbuj wysłać maila
            try:
                form.send()
            except Exception as e:
                success = False
                error.append(f"Błąd wysyłki: {e}")
            else:
                success = True
        else:
            success = False
            error = errors

    return render_template(
        'contact.html',
        active_page='contact',
        success=success,
        error=error
    )
   

@app.route('/projects')
def projects():
    return render_template(
        'projects.html',
        active_page='projects')

@app.route('/informations')
def informations():
    return render_template('informations.html')

