import sys
import json

from cost_tools import calculate_total_cost, calculate_daily_estimate
from aws_pricing import get_price_from_api


def save_report(report):
    with open("cost_report.txt", "w") as file:
        file.write(report)


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
            hourly_price = get_price_from_api(instance)
        except Exception:
            print("Could not get pricing information.")
            sys.exit()

        total_cost = calculate_total_cost(
            hourly_price,
            hours,
            servers
        )

        daily_estimate = calculate_daily_estimate(total_cost)

        report = f"""
AWS COST ESTIMATE

Instance: {instance}
Hourly price: ${hourly_price:.4f}
Hours: {hours}
Servers: {servers}

Monthly estimate: ${total_cost:.2f}
Average daily estimate: ${daily_estimate:.2f}
"""

        print(report)
        save_report(report)



    #JSON configuration
 
    elif len(sys.argv) == 1:

        try:
            with open("config.json") as file:
                config = json.load(file)
        except FileNotFoundError:
            print("config.json not found.")
            sys.exit()

        total_infrastructure_cost = 0

        report = """
AWS INFRASTRUCTURE COST ESTIMATE

"""

        for server in config["servers"]:

            instance = server["instance"]
            hours = server["hours"]
            count = server["count"]

            try:
                hourly_price = get_price_from_api(instance)
            except Exception:
                print(f"Could not get pricing for {instance}.")
                continue

            cost = calculate_total_cost(
                hourly_price,
                hours,
                count
            )

            total_infrastructure_cost += cost

            report += f"""
Instance: {instance}
Hourly price: ${hourly_price:.4f}
Hours: {hours}
Servers: {count}
Cost: ${cost:.2f}
"""

        daily_estimate = calculate_daily_estimate(
            total_infrastructure_cost
        )

        report += f"""

Total monthly cost: ${total_infrastructure_cost:.2f}
Average daily cost: ${daily_estimate:.2f}
"""

        print(report)
        save_report(report)



    # Invalid command
  
    else:

        print(
            "Usage: python aws_cost.py "
            "<instance> <hours> <servers>"
        )

        sys.exit()


main()