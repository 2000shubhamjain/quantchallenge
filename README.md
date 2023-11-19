# quantchallenge

# Energy Trading API

This is a simple web application that exposes an API endpoint to retrieve the Profit and Loss (PnL) data for a given energy trading strategy.

## Setup

1. Install the required dependencies:

   ```bash
   pip install Flask

2. Run the Flask application:
   The application will be accessible at http://0.0.0.0:5000/v1/pnl/strategy_2 or http://localhost:5000/v1/pnl/strategy_1

# API Endpoint

## Get PnL for a Strategy
Endpoint:
  ```bash
  GET /v1/pnl/<strategy_id>
```
## Parameters:

strategy_id (string): The identifier for the trading strategy.
## Response:

Returns the PnL data for the specified strategy in JSON format.
Example Response:
```bash
{
  "strategy": "strategy_1",
  "value": -50.0,
  "unit": "euro",
  "capture_time": "2023-11-19T04:53:47Z"
}
```
## Functions
## def compute_total_buy_volume(*args, **kwargs) -> float:
    A function that computes the total buy volume.
    
## def compute_total_sell_volume(*args, **kwargs) -> float:
    A function that computes the total sell volume.
    
## compute_pnl(strategy_id: str) -> float:
Computes the Profit and Loss (PnL) for a given trading strategy.

Parameters:
strategy_id (str): The identifier for the trading strategy.

Returns:
float: The computed PnL for the specified strategy.

## get_pnl(strategy_id: str) -> Response:
Returns the PnL data for a given trading strategy in a JSON-formatted response.

Parameters:
strategy_id (str): The identifier for the trading strategy.

Returns:
Response: Flask Response object containing the PnL data in JSON format.

## Example

To get the PnL for a strategy with ID "my_strategy," make a GET request to:

```bash
http://localhost:5000/v1/pnl/my_strategy
```
