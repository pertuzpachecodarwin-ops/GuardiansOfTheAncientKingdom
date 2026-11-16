
import customtkinter as ctk

from personajes import Guerrero, Mago, Arquero, Enemigo
from combate import Combate


class InterfazJuego:

    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.ventana = ctk.CTk()
        self.ventana.title("Guardians of the Ancient Kingdom")
        self.ventana.geometry("750x650")
        self.ventana.resizable(False, False)

        self.combate = None

        self.crear_interfaz()

        self.ventana.mainloop()

    def crear_interfaz(self):

        titulo = ctk.CTkLabel(
            self.ventana,
            text="GUARDIANS OF THE ANCIENT KINGDOM",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=20)

        # Selección del personaje
        self.seleccion = ctk.CTkFrame(self.ventana)
        self.seleccion.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(
            self.seleccion,
            text="Selecciona tu personaje:",
            font=("Arial", 16)
        ).pack(pady=10)

        self.personaje_seleccionado = ctk.CTkOptionMenu(
            self.seleccion,
            values=["Guerrero", "Mago", "Arquero"]
        )
        self.personaje_seleccionado.pack(pady=10)

        self.boton_iniciar = ctk.CTkButton(
            self.seleccion,
            text="Iniciar combate",
            command=self.iniciar_combate
        )
        self.boton_iniciar.pack(pady=10)

        # Panel de personajes
        self.panel_combate = ctk.CTkFrame(self.ventana)
        self.panel_combate.pack(pady=15, padx=20, fill="x")

        self.nombre_jugador = ctk.CTkLabel(
            self.panel_combate,
            text="Jugador: --",
            font=("Arial", 16, "bold")
        )
        self.nombre_jugador.pack(pady=8)

        self.vida_jugador = ctk.CTkProgressBar(
            self.panel_combate,
            width=400
        )
        self.vida_jugador.pack(pady=5)
        self.vida_jugador.set(1)

        self.texto_vida_jugador = ctk.CTkLabel(
            self.panel_combate,
            text="Vida: --"
        )
        self.texto_vida_jugador.pack()

        self.nombre_enemigo = ctk.CTkLabel(
            self.panel_combate,
            text="Enemigo: --",
            font=("Arial", 16, "bold")
        )
        self.nombre_enemigo.pack(pady=8)

        self.vida_enemigo = ctk.CTkProgressBar(
            self.panel_combate,
            width=400
        )
        self.vida_enemigo.pack(pady=5)
        self.vida_enemigo.set(1)

        self.texto_vida_enemigo = ctk.CTkLabel(
            self.panel_combate,
            text="Vida: --"
        )
        self.texto_vida_enemigo.pack()

        # Botones de acciones
        self.panel_botones = ctk.CTkFrame(self.ventana)
        self.panel_botones.pack(pady=10)

        self.boton_atacar = ctk.CTkButton(
            self.panel_botones,
            text="Atacar",
            command=self.atacar,
            state="disabled"
        )
        self.boton_atacar.grid(row=0, column=0, padx=10, pady=10)

        self.boton_pocion = ctk.CTkButton(
            self.panel_botones,
            text="Usar poción",
            command=self.usar_pocion,
            state="disabled"
        )
        self.boton_pocion.grid(row=0, column=1, padx=10, pady=10)

        self.texto_pociones = ctk.CTkLabel(
            self.panel_botones,
            text="Pociones: 0"
        )
        self.texto_pociones.grid(row=1, column=0, columnspan=2, pady=5)

        # Registro del combate
        ctk.CTkLabel(
            self.ventana,
            text="Registro del combate",
            font=("Arial", 16, "bold")
        ).pack(pady=5)

        self.registro = ctk.CTkTextbox(
            self.ventana,
            width=650,
            height=120
        )
        self.registro.pack(pady=5)
        self.registro.configure(state="disabled")

    def escribir_registro(self, mensaje):

        self.registro.configure(state="normal")
        self.registro.insert("end", mensaje + "\n")
        self.registro.see("end")
        self.registro.configure(state="disabled")

    def iniciar_combate(self):

        tipo = self.personaje_seleccionado.get()

        if tipo == "Guerrero":
            jugador = Guerrero("Arthas", 100, 30)

        elif tipo == "Mago":
            jugador = Mago("Gandalf", 80, 40)

        else:
            jugador = Arquero("Legolas", 80, 40)

        enemigo = Enemigo("Orco", 100, 15)

        self.combate = Combate(jugador, enemigo)

        self.actualizar_interfaz()

        self.boton_atacar.configure(state="normal")
        self.boton_pocion.configure(state="normal")

        self.registro.configure(state="normal")
        self.registro.delete("1.0", "end")
        self.registro.configure(state="disabled")

        self.escribir_registro(
            f"¡Ha comenzado el combate contra {enemigo.nombre}!"
        )

    def atacar(self):

        if self.combate is None:
            return

        mensaje = self.combate.atacar_enemigo()
        self.escribir_registro(mensaje)

        if self.combate.combate_terminado():
            self.finalizar_combate()
            return

        mensaje = self.combate.enemigo_ataca()
        self.escribir_registro(mensaje)

        self.actualizar_interfaz()

        if self.combate.combate_terminado():
            self.finalizar_combate()

    def usar_pocion(self):

        if self.combate is None:
            return

        mensaje = self.combate.usar_pocion()
        self.escribir_registro(mensaje)

        if "Usaste una poción" in mensaje:
            if not self.combate.combate_terminado():
                mensaje = self.combate.enemigo_ataca()
                self.escribir_registro(mensaje)

        self.actualizar_interfaz()

        if self.combate.combate_terminado():
            self.finalizar_combate()

    def actualizar_interfaz(self):

        jugador = self.combate.jugador
        enemigo = self.combate.enemigo

        self.nombre_jugador.configure(
            text=f"Jugador: {jugador.nombre}"
        )

        self.vida_jugador.set(
            jugador.vida / jugador.vida_maxima
        )

        self.texto_vida_jugador.configure(
            text=f"Vida: {jugador.vida}/{jugador.vida_maxima}"
        )

        self.nombre_enemigo.configure(
            text=f"Enemigo: {enemigo.nombre}"
        )

        self.vida_enemigo.set(
            enemigo.vida / enemigo.vida_maxima
        )

        self.texto_vida_enemigo.configure(
            text=f"Vida: {enemigo.vida}/{enemigo.vida_maxima}"
        )

        self.texto_pociones.configure(
            text=f"Pociones: {self.combate.pociones}"
        )

    def finalizar_combate(self):

        self.actualizar_interfaz()

        if self.combate.jugador.esta_vivo():
            self.escribir_registro("¡FELICIDADES! Has ganado el combate.")
        else:
            self.escribir_registro("Has sido derrotado. Fin del combate.")

        self.boton_atacar.configure(state="disabled")
        self.boton_pocion.configure(state="disabled")


if __name__ == "__main__":
    InterfazJuego()
