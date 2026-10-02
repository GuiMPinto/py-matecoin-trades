import json
from decimal import Decimal


def calculate_profit() -> None:
    with open("trades.json", "r") as file:
        trades = json.load(file)

    total_bought = Decimal("0")
    total_sold = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")

        total_bought += bought
        total_sold += sold

        earned_money += (sold * price) - (bought * price)

    matecoin_account = total_bought - total_sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=4)


if __name__ == "__main__":
    calculate_profit()
