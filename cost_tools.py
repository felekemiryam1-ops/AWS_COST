def calculate_total_cost(hourly_price, hours, servers):
    return hourly_price * hours * servers


def calculate_daily_estimate(total_cost):
    return total_cost / 30
