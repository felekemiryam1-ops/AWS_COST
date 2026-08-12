from aws_pricing import get_price_from_api

price = get_price_from_api("t3.micro")

print(f"Price: ${price}/hour")
