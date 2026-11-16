
class Combate:

    def __init__(self, jugador, enemigo):
        self.jugador = jugador
        self.enemigo = enemigo
        self.pociones = 3

    def atacar_enemigo(self):
        if not self.jugador.esta_vivo():
            return "Tu personaje ha sido derrotado."

        if not self.enemigo.esta_vivo():
            return "El enemigo ya fue derrotado."

        danio = self.jugador.atacar(self.enemigo)

        return f"{self.jugador.nombre} causó {danio} puntos de daño."

    def enemigo_ataca(self):
        if not self.enemigo.esta_vivo():
            return "El enemigo ha sido derrotado."

        if not self.jugador.esta_vivo():
            return "Tu personaje ha sido derrotado."

        danio = self.enemigo.atacar(self.jugador)

        return f"{self.enemigo.nombre} causó {danio} puntos de daño."

    def usar_pocion(self):
        if not self.jugador.esta_vivo():
            return "No puedes curar a un personaje derrotado."

        if self.pociones <= 0:
            return "No tienes más pociones."

        if self.jugador.vida == self.jugador.vida_maxima:
            return "Tu vida ya está completa."

        self.jugador.curar(25)
        self.pociones -= 1

        return f"Usaste una poción. Pociones restantes: {self.pociones}"

    def combate_terminado(self):
        return (
            not self.jugador.esta_vivo()
            or not self.enemigo.esta_vivo()
        )
