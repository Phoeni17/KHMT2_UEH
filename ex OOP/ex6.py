class Converter():
    def __init__(self, length, unit):
        self.length = float(length)
        self.unit = unit.lower()
        self.sang_meters = {'inches':0.0254,'feet':0.3048, 'yards':0.9144, 'miles':1609.34,'kilometers':1000,'meters':1,'centimeters':0.01,'millimeters':0.001}
        self.sang = self.length * self.sang_meters[self.unit]

    def inches(self):
        chuyen = self.sang / 0.0254
        print(f"Doi sang don vi inches: {chuyen} inches")

    def feet(self):
        chuyen = self.sang / 0.3048
        print(f"Doi sang don vi feet: {chuyen} feet")

    def yards(self):
        chuyen = self.sang / 0.9144
        print(f"Doi sang don vi yards: {chuyen} yards")

    def miles(self):
        chuyen = (self.sang / 1609.34)
        print(f"Doi sang don vi miles: {chuyen} miles")

    def kilometers(self):
        chuyen = self.sang / 1000
        print(f"Doi sang don vi kilometers: {chuyen} km")

    def meters(self):
        print(f"Doi sang don vi meters: {self.sang} m")

    def centimeters(self):
        chuyen = self.sang / 0.01
        print(f"Doi sang don vi centimeters: {chuyen} cm")

    def millimeters(self):
        chuyen = self.sang / 0.001
        print(f"Doi sang don vi millimeters: {chuyen} mm")


c1 = Converter(9, 'inches')

c1.inches()
c1.feet()
c1.yards()
c1.miles()
c1.kilometers()
c1.meters()
c1.centimeters()
c1.millimeters()



