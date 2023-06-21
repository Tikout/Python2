from abc import ABC, abstractmethod
import math
class Ksztalt(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def pole(self):
        pass
    
    @abstractmethod
    def obwod(self):
        pass

class Prostokat(Ksztalt):
    def __init__(self, dlugosc, szerokosc):
        super().__init__()
        self._dlugosc = dlugosc
        self._szerokosc = szerokosc
    
    def pole(self):
        return self._dlugosc * self._szerokosc
    
    def obwod(self):
        return 2 * (self._dlugosc + self._szerokosc)

class Kolo(Ksztalt):
    def __init__(self, promien):
        super().__init__()
        self._promien = promien
    
    def pole(self):
        return math.pi * self._promien**2
    
    def obwod(self):
        return 2 * math.pi * self._promien

# Tworzenie obiektów i wywoływanie metod
prostokat = Prostokat(8, 3)
kolo = Kolo(3)

print("Prostokąt:")
print("Pole:", prostokat.pole())
print("Obwód:", prostokat.obwod())

print("Koło:")
print("Pole:", kolo.pole())
print("Obwód:", kolo.obwod())