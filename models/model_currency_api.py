import requests

class NBPClient:

    def __init__(self, base_url='https://api.nbp.pl/api/exchangerates/rates/a/'):
        self.base_url = base_url

    def get_currency_rate(self, currency_code):
        url = f"{self.base_url}{currency_code}/?format=json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return str(data['rates'][0]['mid'])  # Extracting the rate from the JSON response
        except requests.RequestException as e:
            print(f"Error fetching data from NBP API: {e}")

