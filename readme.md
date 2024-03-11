This kata simulates a supermarket checkout system that calculates the total price of scanned items based on their individual prices and any applicable special offers.

Features:

Calculates total price considering unit prices and special offers.
Uses classes (Item, Checkout) for object-oriented programming principles.
Requirements:

Python 3 (version 2.6 or later recommended)
json library (included in Python 2.6 or later, install using pip for older versions)
Setup:

Clone or download the repository.
Navigate to the project directory in your terminal.
Running the Script:

Load pricing rules: The code expects pricing rules to be defined in a JSON file named pricing_rules.json. You can either modify the provided sample file or create a new one following the format:
JSON
[
  {
    "name": "A",
    "unit_price": 50,
    "special_price": 130,
    "special_quantity": 3
  },
]
Each item is defined as an object with properties like name, unit_price, special_price (optional), and special_quantity (optional).
Execute the script:
```
git clone git@github.com:gautamj-tech/codekarta.git
python checkout.py
```
This will run the script, calculate the total price based on pre-defined scan operations (currently in the script) and display the output on the console.

