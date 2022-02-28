from flask import Flask, jsonify, request
from utils.spend_points import spend_points
from utils.init import init
import datetime

app = Flask(__name__)

transactions = []
payer_with_balance_list = []

# initialize transactions and list with each payer's reward points
init(transactions, payer_with_balance_list)


# See historical transaction
@app.route("/transactions", strict_slashes=False, methods=["GET"])
def get_all_transaction():
    try:
        return jsonify(transactions)
    except Exception as e:
        return jsonify(str(e)), 400


# See all payers with their balance
@app.route("/balance", strict_slashes=False, methods=["GET"])
def get_all_balance():
    try:
        return jsonify(payer_with_balance_list)
    except Exception as e:
        return jsonify(str(e)), 400


# Add transaction with given payer and points
@app.route("/add-transaction", methods=["POST"])
def do_transaction():
    try:
        payer = request.form.get("payer")
        points = int(request.form.get("points"))
        timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        transactions.append({"payer": payer,
                             "points": points,
                             "timestamp": timestamp})
        return jsonify(transactions)
    except Exception as e:
        return jsonify(str(e)), 400


# Spend points and consume reward points
@app.route("/spend-points", methods=["PUT"])
def spend():
    try:
        data = request.get_json()
        points = data["points"]
        global transactions
        global payer_with_balance_list
        payer_expenditure_list, new_transactions = spend_points(points,
                                                                transactions,
                                                                payer_with_balance_list)
        if len(payer_expenditure_list) == 0:
            return "insufficient balance", 400
        else:
            transactions = new_transactions
            return jsonify(payer_expenditure_list)
    except Exception as e:
        return jsonify(str(e)), 400


if __name__ == "__main__":
    app.run(debug=True)
