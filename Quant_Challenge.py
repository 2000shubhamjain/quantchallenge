# -*- coding: utf-8 -*-

#Task 1

import sqlite3
from typing import List, Dict
from flask import Flask, jsonify, Response
from datetime import datetime
import json

def compute_total_buy_volume(*args, **kwargs) -> float:
    """Write a function that computes the total buy volume."""
    # Connecting to the SQLite database
    conn = sqlite3.connect('trades.sqlite')
    cursor = conn.cursor()

    # Extracting strategy_id from kwargs
    strategy_id = kwargs.get('strategy_id', None)

    # Checking if strategy_id is provided
    if strategy_id is not None:
        cursor.execute("SELECT SUM(quantity) FROM epex_12_20_12_13 WHERE side='buy' AND strategy=?", (strategy_id,))
        result = cursor.fetchone()[0]
        total_buy_volume = result if result is not None else 0
    else:
        total_buy_volume = 0  # Default value if strategy_id is not provided

    # Closing the connection
    conn.close()

    return total_buy_volume

def compute_total_sell_volume(*args, **kwargs) -> float:
    """Write a function that computes the total sell volume."""
    # Connecting to the SQLite database
    conn = sqlite3.connect('trades.sqlite')
    cursor = conn.cursor()

    # Extracting strategy_id from kwargs
    strategy_id = kwargs.get('strategy_id', None)

    # Checking if strategy_id is provided
    if strategy_id is not None:
        cursor.execute("SELECT SUM(quantity) FROM epex_12_20_12_13 WHERE side='sell' AND strategy=?", (strategy_id,))
        result = cursor.fetchone()[0]
        total_sell_volume = result if result is not None else 0
    else:
        total_sell_volume = 0  # Default value if strategy_id is not provided

    # Closing the connection
    conn.close()

    return total_sell_volume

# Task 1 Example usage:
strategy_id = 'strategy_1'
total_buy_volume = compute_total_buy_volume(strategy_id=strategy_id)
total_sell_volume = compute_total_sell_volume(strategy_id=strategy_id)

print(f'Total Buy Volume for Strategy {strategy_id}: {total_buy_volume} MW')
print(f'Total Sell Volume for Strategy {strategy_id}: {total_sell_volume} MW')

strategy_id2 = 'strategy_2'
total_buy_volume2 = compute_total_buy_volume(strategy_id=strategy_id2)
total_sell_volume2 = compute_total_sell_volume(strategy_id=strategy_id2)

print(f'Total Buy Volume for Strategy {strategy_id2}: {total_buy_volume2} MW')
print(f'Total Sell Volume for Strategy {strategy_id2}: {total_sell_volume2} MW')


#Task 2


def compute_pnl(strategy_id: str, *args, **kwargs) -> float:
    """
    Write a function that computes the PnL (profit and loss) of each strategy in euros.
    
    It's defined as the sum of the incomes realized with each trade.

    If we sell energy, our income is quantity * price since we got money for our electricity. 
    
    If we buy energy, our income is -quantity * price.
    """
    # Connecting to the SQLite database
    conn = sqlite3.connect('trades.sqlite 2')
    cursor = conn.cursor()

    # Executing SQL query to get trades for the specified strategy_id
    cursor.execute("SELECT quantity, price, side FROM epex_12_20_12_13 WHERE strategy=?", (strategy_id,))
    trades = cursor.fetchall()

    # Closing the connection
    conn.close()

    # Calculating PnL
    pnl = 0
    for quantity, price, side in trades:
        if side == 'sell':
            pnl += quantity * price  # Income from selling energy
        elif side == 'buy':
            pnl -= quantity * price  # Expense from buying energy

    return pnl

# Task 2 Example usage:
strategy_id = 'strategy_1'
pnl = compute_pnl(strategy_id=strategy_id)

print(f'PnL for Strategy {strategy_id}: {pnl} euros')

strategy_id2 = 'strategy_2'
pnl2 = compute_pnl(strategy_id=strategy_id2)

print(f'PnL for Strategy {strategy_id2}: {pnl2} euros')


#Task 3

app = Flask(__name__)

@app.route('/v1/pnl/<string:strategy_id>', methods=['GET'])
def get_pnl(strategy_id: str) -> dict:
    """Expose the function defined in the second task as an entrypoint of a web application."""
    # Calling the compute_pnl function
    pnl_value = compute_pnl(strategy_id)
    
    # Preparing the response
    response = {
        "strategy": strategy_id,
        "value": pnl_value,
        "unit": "euro",
        "capture_time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    json_response = json.dumps(response, indent=2)

    # Returning the JSON response with the appropriate content type header
    return Response(json_response, content_type='application/json; charset=utf-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
#Use this link to find the API: http://0.0.0.0:5000/v1/pnl/strategy_2 
#%%

