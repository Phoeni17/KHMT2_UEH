class Investment():
    def __init__(self, principal, interest):
        self.principal = float(principal)
        self.interest = float(interest)

    def value_after(self, n):
        self.n = int(n)
        value = self.principal * (1 + self.interest) ** n
        print(f"Vay gia tri sau {self.n} nam la: ${value}")

    def __str__(self):
        return f"Tien goc: ${self.principal}, Lai suat: {self.interest}%"


invest1 = Investment(1000, 5.12)
invest2 = Investment(7270, 4.5)
invest3 = Investment(5000, 4.0)

invest1.value_after(5)
invest2.value_after(10)
invest3.value_after(7)

