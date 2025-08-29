import numpy as np
class cambien():
    def __init__(self, ten, vitri, ngayghi):
        self.ten = ten
        self._vitri = vitri
        self.__ngayghi = "01/01"

    def lay_ngay(self):
        print(self.__ngayghi)


cambien1 = cambien("CB Nhiet do", "B1-404","15/08")
cambien1.__ngayghi = "31/12"
print(cambien1.__ngayghi)
cambien1.lay_ngay()

cambien1.doi
