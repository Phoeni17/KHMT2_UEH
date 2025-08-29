class Password_manager():
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        print(f"Mat khau hien tai la: {self.old_passwords[-1]}")

    def set_password(self, new):
        self.new = new
        if self.new not in self.old_passwords:
            self.old_passwords.append(new)
            print("Ban da thay mat khau")
        else:
            print("Mat khau moi trung voi mat khau cu!")

    def is_correct(self, password):
        self.password = password
        if self.password == self.old_passwords[-1]:
            print("True => Dung mat khau")
        else:
            print("False => Sai mat khau")

pw1 = Password_manager()

pw1.set_password("max_verstappen")
pw1.get_password()

pw1.set_password("lewis_hamilton")
pw1.get_password()

pw1.set_password("max_verstappen")
pw1.get_password()

pw1.is_correct("max_verstappen")
pw1.is_correct("lewis_hamilton")


