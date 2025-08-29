class Product():
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = int(amount)
        self.price = int(price)

    def get_price(self, purchase_amount):
        self.purchase_amount = int(purchase_amount)

        if self.purchase_amount < 10:
            total = self.purchase_amount * self.price
        elif 10 <= self.purchase_amount <= 99:
            total = self.purchase_amount * self.price * 90/100
        else:
            total = self.purchase_amount * self.price * 80 / 100
        print(f"So tien phai tra cho {self.purchase_amount} {self.name} la: {total}")

    def make_purchase(self):
        left = self.amount - self.purchase_amount
        print(f"So {self.name} duoc mua: {self.purchase_amount}")
        print(f"So {self.name} con trong kho: {left}")

p1 = Product("Yamaha R1", 200, 20000)
p2 = Product("Honda CBR1000R", 150, 18000)
p3 = Product("Kawasaki H2", 50, 30000)

p1.get_price(7)
p1.make_purchase()

p2.get_price(125)
p2.make_purchase()

p3.get_price(30)
p3.make_purchase()
