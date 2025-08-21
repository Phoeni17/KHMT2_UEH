class Time():
    def __init__(self, sec):
        self.sec = sec

    def convert_to_minutes(self):
        phut = self.sec // 60
        giay = self.sec % 60
        print(f"Thoi gian dinh dang theo phut la: {phut}:{giay}")

    def convert_to_hours(self):
        gio = self.sec // 3600
        giol = self.sec % 3600
        phut = giol // 60
        giay = giol % 60
        print(f"Thoi gian dinh dang theo gio la: {gio}:{phut}:{giay}")

tg1 = Time(3650)
tg2 = Time(32200)

tg1.convert_to_minutes()
tg2.convert_to_hours()
