import sys
import json

from cost_tools import calculate_total_cost, calculate_daily_estimate


prices = {
    "t2.micro": 0.0116,
    "t3.micro": 0.0104,
    "t3.small": 0.0208
}


def main():

    #Command-line arguments
   
    if len(sys.argv) == 4:

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


    
    #JSON configuration
    
    elif len(sys.argv) == 1:

        try:
            with open("config.json") as file:
                config = json.load(file)
        except FileNotFoundError:
            print("config.json not found.")
            sys.exit()

        total_infrastructure_cost = 0

        print("\nAWS INFRASTRUCTURE COST ESTIMATE")
        print("--------------------------------")

        for server in config["servers"]:

            instance = server["instance"]
            hours = server["hours"]
            count = server["count"]

            try:
                hourly_price = prices[instance]
            except KeyError:
                print(f"Unknown instance type: {instance}")
                continue

            cost = calculate_total_cost(
                hourly_price,
                hours,
                count
            )

            total_infrastructure_cost += cost

            print(f"\nInstance: {instance}")
            print(f"Hourly price: ${hourly_price:.4f}")
            print(f"Hours: {hours}")
            print(f"Servers: {count}")
            print(f"Cost: ${cost:.2f}")

        daily_estimate = calculate_daily_estimate(
            total_infrastructure_cost
        )

        print("\n-------------------------------")
        print(f"Total monthly cost: ${total_infrastructure_cost:.2f}")
        print(f"Average daily cost: ${daily_estimate:.2f}")


    

    else:

        print(
            "Usage: python aws_cost.py "
            "<instance> <hours> <servers>"
        )

        sys.exit()


main()