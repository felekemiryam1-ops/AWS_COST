import requests


def get_price_from_api(instance):
    family, size = instance.split(".")

    url = f"https://ec2pricing.com/us-east-1/{family}/{size}.json"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    return data["price"]