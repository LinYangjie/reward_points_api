
def spend_points(total_cost: int, transactions: list,
                 payer_with_balance_list: list):
    """ A helper function get payer's in their account

        Params:
            total_cost(int): Total reward points spent
            transactions(list): A list with historical transactions
            payer_with_balance_list(list): A list with each payer's balance

        Returns:
            An integer which presents the reward points with given payer

    """
    # Check if total_balance is enough
    total_balance = sum(points["points"] for points in payer_with_balance_list)
    if total_balance < total_cost:
        return [], transactions

    # Check if total cost is not valid
    if total_cost <= 0:
        return [], transactions

    # Transactions will keep after spending reward points
    new_transactions_history = []
    payer_expenditure_list = []
    idx = 0

    # Start consuming reward points
    for transaction in transactions:

        # Each transaction
        payer = transaction["payer"]
        reward_points = transaction["points"]

        # Get current balance from payer
        balance = get_balance(payer_with_balance_list, payer)

        # If payer does not have enough reward points to spend
        if balance <= 0:
            new_transactions_history.append(transaction)
            continue

        # -------- Consume reward points ----------------

        # If reward_points are less or equal than total cost
        if reward_points <= total_cost:

            # Update balance
            spend_points_from_payer(payer_with_balance_list,
                                    payer,
                                    reward_points)

            # Update expenditure
            record_expenditure_by_payer(payer_expenditure_list,
                                        payer,
                                        reward_points)
            total_cost -= reward_points
        else:

            # Update balance
            spend_points_from_payer(payer_with_balance_list,
                                    payer,
                                    total_cost)
            # Update expenditure
            record_expenditure_by_payer(payer_expenditure_list,
                                        payer,
                                        total_cost)
            total_cost = 0

        # Check if all spend points are all counsumed
        if total_cost == 0:
            break

        idx += 1

    # Update to latest transactions history
    latest_transactions = new_transactions_history + transactions[idx:]

    return payer_expenditure_list, latest_transactions

# ------------helper function ------------------- #


# given payer balance list and payer, return how much payer spend
def get_balance(payer_with_balance_list: list, payer: str):
    """ A helper function get payer's in their account

        Params:
            payer_with_balance_list(list): a list with payer and their reward
                                           points
            payer(str): payer who owns reward points

        Returns:
            An integer which presents the reward points with given payer

    """
    for payer_with_balance in payer_with_balance_list:
        if payer == payer_with_balance["payer"]:
            return payer_with_balance.get("points")
    return -1


def spend_points_from_payer(payer_with_balance_list: list,
                            payer: str,
                            spend_points: int):
    """ A helper function update payer's balance after consume reward points

        Params:
            payer_with_balance_list(list): a list with payer and their reward
                                           points
            payer(str): payer who owns reward points
            spend_points(int):
        Returns:
            An integer which presents the reward points with given payer

    """
    for payer_with_balance in payer_with_balance_list:
        if payer == payer_with_balance["payer"]:
            payer_with_balance["points"] -= spend_points
            break


def record_expenditure_by_payer(payer_expenditure_list: dict, payer: str,
                                spend_points: int):
    """ A helper function record payer consuming reward points

        Params:
            payer_with_balance_list(list): a list with payer and their reward
                                           points
            payer(str): payer who owns reward points

        Returns:
            An integer which presents the reward points with given payer

    """
    found_payer = False
    for payer_expenditure in payer_expenditure_list:
        if payer == payer_expenditure["payer"]:
            payer_expenditure["points"] -= spend_points
            found_payer = True
            break
    if not found_payer:
        payer_expenditure_list.append({"payer": payer,
                                       "points": -spend_points})
