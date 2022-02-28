import json
import os
TRANSACTIONS_DIR = "resource"


def init(transactions: list, payer_with_balance_list: list):
    """
        Initialize the storage with given transactions json file
        and payer's balance

        Params:
            transactions (list): All historical transactions with
                                 payer, points and timestamp
            payer_with_balance_list (list): A list stores total reward
                                            points of each payer
        Returns:
            None
    """
    file = open(os.path.join(TRANSACTIONS_DIR, "transactions.json"), "r")
    transactions = json.load(file)
    transactions = sorted(transactions, key=lambda i: i['timestamp'])
    payer_with_balance_list = []
    for transaction in transactions:
        payer = transaction["payer"]
        points = transaction["points"]
        contains_payer = False
        for payer_balance in payer_with_balance_list:
            if payer in payer_balance.values():
                payer_balance["points"] += points
                contains_payer = True
                break
        if not contains_payer:
            payer_with_balance_list.append({"payer": payer, "points": points})
