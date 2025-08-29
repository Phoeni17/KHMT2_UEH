import numpy as np

class cambien():
    def __init__(self, ten, vitri, ngayghi):
        self.ten = ten
        self.vitri = vitri
        self.ngayghi = ngayghi
        self.data = {}

    def them_dulieu(self, t, data):
        self.data["time"] = t
        self.data["data"] = data
        print(f"Da co {len(data)} du lieu duoc lieu")

    def xoa(self):
        self.data = {}
        print("Da xoa du lieu")

cambien1 = cambien("CB nhiet do", "B1-404", "15/08/2025")

class cambien_xin(cambien):
    def __init__(self, ten, vitri, ngayghi, nhanhieu):
        super().__init__(ten, vitri, ngayghi)
        self.nhanhhieu = nhanhieu

cambien2 = cambien_xin("DHT 11", "UEH", "15/08/2025", "Mitsu")
print(cambien2.ten)
print(cambien2.nhanhhieu)
