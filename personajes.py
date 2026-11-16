
from abc import ABC, abstractmethod


# Clase abstracta principal
class Personaje(ABC):

    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self._vida = vida
        self._vida_maxima = vida
        self._ataque = ataque

    @property
    def vida(self):
        return self._vida

    @property
    def ataque(self):
        return self._ataque

    def recibir_danio(self, cantidad):
        self._vida -= cantidad

        if self._vida < 0:
            self._vida = 0

    def curar(self, cantidad):
        self._vida += cantidad

        if self._vida > self._vida_maxima:
            self._vida = self._vida_maxima

    def esta_vivo(self):
        return self._vida > 0

    @abstractmethod
    def atacar(self, objetivo):
        pass
    
    @property
    def vida_maxima(self):
     return self._vida_maxima


# Clase Guerrero
class Guerrero(Personaje):

    def atacar(self, objetivo):
        danio = self.ataque
        objetivo.recibir_danio(danio)
        return danio


# Clase Mago
class Mago(Personaje):

    def atacar(self, objetivo):
        danio = self.ataque + 5
        objetivo.recibir_danio(danio)
        return danio


# Clase Arquero
class Arquero(Personaje):

    def atacar(self, objetivo):
        danio = self.ataque + 2
        objetivo.recibir_danio(danio)
        return danio


# Clase Enemigo
class Enemigo(Personaje):

    def atacar(self, objetivo):
        danio = self.ataque
        objetivo.recibir_danio(danio)
        return danio
