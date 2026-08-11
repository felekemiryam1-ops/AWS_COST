import json

from cost_tools import calculate_total_cost, calculate_daily_estimate


prices = {
    "t2.micro": 0.0116,
    "t3.micro": 0.0104,
    "t3.small": 0.0208
}


def main():

    with open("config.json") as file:
        config = json.load(file)

    instance = config["instance"]
    hours = config["hours"]
    servers = config["servers"]

    hourly_price = prices[instance]

    total_cost = calculate_total_cost(
        hourly_price,
        hours,
        servers
    )

    daily_estimate = calculate_daily_estimate(total_cost)

    print(f"Instance: {instance}")
    print(f"Hours: {hours}")
    print(f"Servers: {servers}")
    print(f"Monthly estimate: ${total_cost:.2f}")
    print(f"Average daily estimate: ${daily_estimate:.2f}")


main()