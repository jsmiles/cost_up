# cost_up
A rest api that calculates the cost of a transaction. The app expects as input, json from a post request formatted like below. This would represent a hypothetical transaction. 

```
{
    "order": {
        "id": 12345,
        "customer": {},
        "currency": "EUR",
        "items": [
            {
                "product_id": 1,
                "quantity": 1
            },
            {
                "product_id": 2,
                "quantity": 5
            },
            {
                "product_id": 3,
                "quantity": 1
            }
        ]
    }
}
```

Tha app then does a couple of things:
1. It looks up the cost of each product
2. It looks up the vat rate for each item
3. It looks up the currency exchange rate
4. It calculates the total cost of the basket of goods in the specified currency
5. It calculates the total vat portion of the cost in the specified currency
6. For each product it calculates the 

Note: the assumption currently built in, is that all received prices are in GBP and that the most recent exchange rate should be used. 

The output should look something like the below with a transaction id, total cost figure, total vat figure and for each product id the component cost and vat. 

```
{
  "12345": {
    "1": {
      "cost": 689,
      "vat": 138
    },
    "2": {
      "cost": 1438,
      "vat": 0
    },
    "3": {
      "cost": 288,
      "vat": 0
    }
  },
  "total_cost": 2414,
  "total_vat": 138
}

```


# Usage
To use the app locally its quite straight forward
1. Ensure you have the requirements
2. In the directory with app.py run  ```python app.py```

Once the server is running locally you could use a utility such as [Postman](https://www.getpostman.com/) to test the API 

# Description
* __app.py__ the flask app, handles the post request and gives the response
* __processing.py__ the logic and functions that comprise the primary calculation logic 
* __ref.json__ the reference data, used to apply the correct price and vat rate. A simpler alternative would be to use database tables. 
* __requirements.txt__ the packages in the virtualenv used to develop this app. Not all are used, but it works with that configuration. 
