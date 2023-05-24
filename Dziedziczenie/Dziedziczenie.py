class Prostokat_Pole:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def licz(self):
        print("Pole wynosi:", self.a * self.b, "cm^2")


Prostokat1 = Prostokat_Pole(12, 13)
Prostokat1.licz()

Prostokat2 = Prostokat_Pole(11, 9)
Prostokat2.licz()