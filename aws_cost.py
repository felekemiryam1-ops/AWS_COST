import sys

from cost_tools import calculate_total_cost, calculate_daily_estimate


prices = {
    "t2.micro": 0.0116,
    "t3.micro": 0.0104,
    "t3.small": 0.0208
}


def main():

    # Check that the user provided 3 arguments
    if len(sys.argv) != 4:
        print("Usage: python aws_cost.py <instance> <hours> <servers>")
        sys.exit()

    instance = sys.argv[1]

    try:
        hours = int(sys.argv[2])
        servers = int(sys.argv[3])
    except ValueError:
        print("Hours and servers must be numbers.")
        sys.exit()

    try:
        hourly_price = prices[instance]
    except KeyError:
        print("Unknown instance type.")
        sys.exit()

    total_cost = calculate_total_cost(
        hourly_price,
        hours,
        servers
    )

    daily_estimate = calculate_daily_estimate(total_cost)

    print("\nAWS COST ESTIMATE")
    print("-----------------")
    print(f"Instance: {instance}")
    print(f"Hourly price: ${hourly_price:.4f}")
    print(f"Hours: {hours}")
    print(f"Servers: {servers}")
    print(f"Monthly estimate: ${total_cost:.2f}")
    print(f"Average daily estimate: ${daily_estimate:.2f}")


main()