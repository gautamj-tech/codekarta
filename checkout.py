class Item:
    def __init__(self, name, unit_price, special_price=None, special_quantity=None):
        self.name = name
        self.unit_price = unit_price
        self.special_price = special_price
        self.special_quantity = special_quantity

    def get_price(self, quantity):
        if self.special_price and quantity >= self.special_quantity:
            n_specials = quantity // self.special_quantity
            n_regular = quantity % self.special_quantity
            return n_specials * self.special_price + n_regular * self.unit_price
        else:
            return quantity * self.unit_price


class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.items = []

    def scan(self, item_name):
        item = next(
            (item for item in self.pricing_rules if item.name == item_name), None
        )
        if not item:
            raise ValueError(f"Item {item_name} not found in pricing rules")
        self.items.append(item)

    def total(self):
        total_price = 0
        for item in self.items:
            total_price += item.get_price(self.items.count(item))
        return total_price


def main():
    with open("price.json", "r") as f:
        pricing_rules = [Item(**item) for item in json.load(f)]

    checkout = Checkout(pricing_rules)
    checkout.scan("A")
    checkout.scan("A")
    checkout.scan("A")
    checkout.scan("B")
    checkout.scan("B")
    checkout.scan("D")
    total_price = checkout.total()
    print(f"Total price: ₹{total_price:.2f}")


if __name__ == "__main__":
    main()