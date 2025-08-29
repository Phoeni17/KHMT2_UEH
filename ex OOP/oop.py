class Students():
    n = 0
    def __init__(self, MSSV, Name, Lop, Gender, DOB, GK, CK):
        self.MSSV = MSSV
        self.Name = Name
        self.Lop = Lop
        self.Gender = Gender
        self.DOB = str(DOB)
        self.GK = float(GK)
        self.CK = float(CK)
        Students.n += 1
    def Introduction(self):
        if self.Gender == "Male":
            print("Ban "+ self.Name + " co MSSV la "+ self.MSSV + ", anh ay la sv lop "+ self.Lop + " va sinh ngay "+ self.DOB)
        elif self.Gender == "Female":
            print("Ban " + self.Name + " co MSSV la " + self.MSSV + ", co ay la sv lop " + self.Lop + " va sinh ngay " + self.DOB)
        else:
            print("Hay nhap gioi tinh sang tieng Anh nhe")

    def Tong_Ket(self):
        Score = (self.GK + self.CK) / 2
        if Score >= 5.0:
            print(f"Ban {self.Name} da qua mon voi so diem: {Score}")
        else:
            print(f"Ban {self.Name} da rot mon!")



s1 = Students("31241020155", "Bui Xuan Cong Minh", "ICA", "Male", "10/09/2006", 9.75, 8.5)
print(s1.n)
s2 = Students("31241020001", "Nguyen Van An", "Robot", "Male", "01/01/2006", 2.0, 6.0)
print(s2.n)
s3 = Students("31241027272", "Bui Thi Tuyet Trinh", "ICP", "Female", "27/05/2006", 9.5, 7.5)
print(s3.n)

s2.Tong_Ket()
print(Students.n)
