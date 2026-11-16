import tkinter as tk
from pathlib import Path

import customtkinter as ctk
from PIL import Image, ImageTk

from personajes import Guerrero, Mago, Arquero, Enemigo
from combate import Combate


class InterfazJuego:
    ANCHO_ARENA = 780
    ALTO_ARENA = 320

    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.ventana = ctk.CTk()
        self.ventana.title("Guardians of the Ancient Kingdom")
        self.ventana.geometry("1120x790")
        self.ventana.minsize(1050, 740)
        self.ventana.configure(fg_color="#10101D")

        self.carpeta_assets = Path(__file__).resolve().parent / "assets"
        self.combate = None
        self.imagen_jugador_tk = None
        self.imagen_enemigo_tk = None
        self.fondo_tk = None
        self.crear_interfaz()
        self.ventana.mainloop()

    def cargar_imagen(self, archivo, ancho, alto):
        ruta = self.carpeta_assets / archivo
        try:
            with Image.open(ruta) as original:
                imagen = original.convert("RGBA")
                imagen.thumbnail((ancho, alto), Image.Resampling.LANCZOS)
            return ctk.CTkImage(light_image=imagen, dark_image=imagen,
                                size=imagen.size)
        except (OSError, ValueError):
            return None

    def crear_interfaz(self):
        encabezado = ctk.CTkFrame(self.ventana, fg_color="#211631",
                                  corner_radius=0, height=88)
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)
        ctk.CTkLabel(encabezado,
                     text="⚔ GUARDIANS OF THE ANCIENT KINGDOM ⚔",
                     font=("Georgia", 25, "bold"),
                     text_color="#F5CA69").pack(pady=(13, 2))
        ctk.CTkLabel(encabezado,
                     text="EL DESTINO DEL REINO ESTÁ EN TUS MANOS",
                     font=("Arial", 11), text_color="#B7A5CD").pack()

        principal = ctk.CTkFrame(self.ventana, fg_color="transparent")
        principal.pack(fill="both", expand=True, padx=15, pady=12)
        principal.grid_columnconfigure(0, weight=0)
        principal.grid_columnconfigure(1, weight=1)
        principal.grid_rowconfigure(0, weight=1)

        izquierda = ctk.CTkFrame(principal, fg_color="#211A30",
                                 corner_radius=14, width=245)
        izquierda.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        izquierda.grid_propagate(False)

        ctk.CTkLabel(izquierda, text="⚔ ELIGE TU GUARDIÁN",
                     font=("Arial", 17, "bold"),
                     text_color="#F5CA69").pack(pady=(26, 18))
        self.personaje_seleccionado = ctk.CTkOptionMenu(
            izquierda, values=["Guerrero", "Mago", "Arquero"],
            command=self.cambiar_personaje, width=195, height=40,
            fg_color="#533C7A", button_color="#74549E")
        self.personaje_seleccionado.pack(pady=8)

        self.imagen_seleccion = ctk.CTkLabel(
            izquierda, text="", width=190, height=210)
        self.imagen_seleccion.pack(pady=12)
        self.descripcion = ctk.CTkLabel(
            izquierda, text="", font=("Arial", 13),
            text_color="#D8CDE8", justify="center")
        self.descripcion.pack(pady=10)
        self.boton_iniciar = ctk.CTkButton(
            izquierda, text="▶ INICIAR COMBATE", command=self.iniciar_combate,
            fg_color="#B78938", hover_color="#D6A44D",
            text_color="#15101B", font=("Arial", 14, "bold"),
            height=45, width=195)
        self.boton_iniciar.pack(pady=20)

        derecha = ctk.CTkFrame(principal, fg_color="#171827", corner_radius=14)
        derecha.grid(row=0, column=1, sticky="nsew")
        ctk.CTkLabel(derecha, text="⚔ ARENA DE COMBATE ⚔",
                     font=("Georgia", 21, "bold"),
                     text_color="#F5CA69").pack(pady=(13, 8))

        # Canvas permite superponer PNG transparentes sobre el bosque.
        self.arena = tk.Canvas(
            derecha, width=self.ANCHO_ARENA, height=self.ALTO_ARENA,
            bg="#252137", highlightthickness=0, bd=0)
        self.arena.pack(padx=12, pady=5)
        self.preparar_fondo()

        self.personaje_canvas = self.arena.create_image(175, 148, anchor="center")
        self.enemigo_canvas = self.arena.create_image(605, 148, anchor="center")
        self.arena.create_text(390, 142, text="VS", fill="#F5CA69",
                               font=("Georgia", 37, "bold"))
        self.nombre_jugador_canvas = self.arena.create_text(
            175, 253, text="Héroe", fill="white", font=("Arial", 15, "bold"))
        self.nombre_enemigo_canvas = self.arena.create_text(
            605, 253, text="Orco", fill="white", font=("Arial", 15, "bold"))

        # Fondo oscuro de las barras para mostrar la vida restante.
        self.arena.create_rectangle(80, 273, 270, 288, fill="#34323D", outline="")
        self.arena.create_rectangle(510, 273, 700, 288, fill="#34323D", outline="")
        self.vida_jugador_canvas = self.arena.create_rectangle(
            80, 273, 270, 288, fill="#28C66F", outline="")
        self.vida_enemigo_canvas = self.arena.create_rectangle(
            510, 273, 700, 288, fill="#E44B4B", outline="")
        self.texto_vida_jugador_canvas = self.arena.create_text(
            175, 305, text="Vida: --", fill="white", font=("Arial", 11, "bold"))
        self.texto_vida_enemigo_canvas = self.arena.create_text(
            605, 305, text="Vida: --", fill="white", font=("Arial", 11, "bold"))

        acciones = ctk.CTkFrame(derecha, fg_color="transparent")
        acciones.pack(pady=(12, 5))
        self.boton_atacar = ctk.CTkButton(
            acciones, text="⚔ ATACAR", command=self.atacar, state="disabled",
            fg_color="#A52C39", hover_color="#C9414F", width=155,
            height=43, font=("Arial", 14, "bold"))
        self.boton_atacar.grid(row=0, column=0, padx=6)
        self.boton_pocion = ctk.CTkButton(
            acciones, text="✚ USAR POCIÓN", command=self.usar_pocion,
            state="disabled", fg_color="#208052", hover_color="#2FA66D",
            width=155, height=43, font=("Arial", 14, "bold"))
        self.boton_pocion.grid(row=0, column=1, padx=6)
        self.boton_reiniciar = ctk.CTkButton(
            acciones, text="↻ REINICIAR", command=self.iniciar_combate,
            fg_color="#51406F", hover_color="#735A98", width=145,
            height=43, font=("Arial", 14, "bold"))
        self.boton_reiniciar.grid(row=0, column=2, padx=6)

        self.texto_pociones = ctk.CTkLabel(
            derecha, text="Pociones disponibles: --",
            font=("Arial", 13), text_color="#A9F0BD")
        self.texto_pociones.pack(pady=4)
        ctk.CTkLabel(derecha, text="📜 REGISTRO DE BATALLA",
                     font=("Arial", 16, "bold"),
                     text_color="#F5CA69").pack(pady=(9, 5))
        self.registro = ctk.CTkTextbox(
            derecha, height=145, fg_color="#10101D",
            text_color="#E7DDF2", font=("Consolas", 13),
            corner_radius=10, wrap="word")
        self.registro.pack(fill="both", expand=True, padx=18, pady=(0, 14))
        self.registro.configure(state="disabled")
        self.cambiar_personaje("Guerrero")

    def preparar_fondo(self):
        ruta = self.carpeta_assets / "fondo.png"
        try:
            with Image.open(ruta) as original:
                fondo = original.convert("RGB").resize(
                    (self.ANCHO_ARENA, self.ALTO_ARENA), Image.Resampling.LANCZOS)
            self.fondo_tk = ImageTk.PhotoImage(fondo)
            self.arena.create_image(0, 0, anchor="nw", image=self.fondo_tk)
        except (OSError, ValueError):
            self.arena.create_text(
                390, 40, text="Bosque encantado", fill="#F5CA69",
                font=("Georgia", 18, "bold"))

    def colocar_imagen_seleccion(self, archivo, simbolo):
        imagen = self.cargar_imagen(archivo, 190, 210)
        if imagen is None:
            self.imagen_seleccion.configure(image=None, text=simbolo,
                                            font=("Arial", 60))
        else:
            self.imagen_seleccion.configure(image=imagen, text="")
        self.imagen_seleccion.image = imagen

    def cambiar_personaje(self, tipo):
        datos = {
            "Guerrero": ("guerrero.png", "🛡", "ARTHAS\n100 de vida\n30 de ataque"),
            "Mago": ("mago.png", "🔮", "GANDALF\n80 de vida\n45 de daño"),
            "Arquero": ("arquero.png", "🏹", "LEGOLAS\n80 de vida\n42 de daño"),
        }
        archivo, simbolo, descripcion = datos[tipo]
        self.colocar_imagen_seleccion(archivo, simbolo)
        self.descripcion.configure(text=descripcion)

    def actualizar_imagen_canvas(self, archivo, identificador, simbolo):
        ruta = self.carpeta_assets / archivo
        try:
            with Image.open(ruta) as original:
                imagen = original.convert("RGBA")
                imagen.thumbnail((215, 205), Image.Resampling.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(imagen)
            self.arena.itemconfigure(identificador, image=imagen_tk)
            if identificador == self.personaje_canvas:
                self.imagen_jugador_tk = imagen_tk
            else:
                self.imagen_enemigo_tk = imagen_tk
        except (OSError, ValueError):
            self.arena.itemconfigure(identificador, image="")
            self.arena.create_text(
                175 if identificador == self.personaje_canvas else 605,
                145, text=simbolo, fill="white", font=("Arial", 60),
                tags="simbolo_temporal")

    def escribir_registro(self, mensaje):
        self.registro.configure(state="normal")
        self.registro.insert("end", mensaje + "\n")
        self.registro.see("end")
        self.registro.configure(state="disabled")

    def iniciar_combate(self):
        tipo = self.personaje_seleccionado.get()
        if tipo == "Guerrero":
            jugador = Guerrero("Arthas", 100, 30)
            archivo, simbolo = "guerrero.png", "🛡"
        elif tipo == "Mago":
            jugador = Mago("Gandalf", 80, 40)
            archivo, simbolo = "mago.png", "🔮"
        else:
            jugador = Arquero("Legolas", 80, 40)
            archivo, simbolo = "arquero.png", "🏹"

        enemigo = Enemigo("Orco", 100, 15)
        self.combate = Combate(jugador, enemigo)
        self.arena.delete("simbolo_temporal")
        self.actualizar_imagen_canvas(archivo, self.personaje_canvas, simbolo)
        self.actualizar_imagen_canvas("orco.png", self.enemigo_canvas, "👹")

        self.registro.configure(state="normal")
        self.registro.delete("1.0", "end")
        self.registro.configure(state="disabled")
        self.boton_atacar.configure(state="normal")
        self.boton_pocion.configure(state="normal")
        self.actualizar_interfaz()
        self.escribir_registro(f"⚔ ¡{jugador.nombre} se enfrenta al Orco!")

    def efecto_golpe(self, identificador):
        # Destello breve sobre el personaje que recibió el ataque.
        x = 175 if identificador == self.personaje_canvas else 605
        efecto = self.arena.create_oval(
            x - 85, 60, x + 85, 235,
            outline="#FF6767", width=5)
        self.ventana.after(180, lambda: self.arena.delete(efecto))

    def atacar(self):
        if self.combate is None or self.combate.combate_terminado():
            return
        mensaje = self.combate.atacar_enemigo()
        self.escribir_registro("⚔ " + mensaje)
        self.efecto_golpe(self.enemigo_canvas)
        self.actualizar_interfaz()
        if self.combate.combate_terminado():
            self.finalizar_combate()
            return
        mensaje = self.combate.enemigo_ataca()
        self.escribir_registro("🛡 " + mensaje)
        self.efecto_golpe(self.personaje_canvas)
        self.actualizar_interfaz()
        if self.combate.combate_terminado():
            self.finalizar_combate()

    def usar_pocion(self):
        if self.combate is None or self.combate.combate_terminado():
            return
        mensaje = self.combate.usar_pocion()
        self.escribir_registro("✚ " + mensaje)
        if "Usaste una poción" in mensaje and not self.combate.combate_terminado():
            respuesta = self.combate.enemigo_ataca()
            self.escribir_registro("⚔ " + respuesta)
            self.efecto_golpe(self.personaje_canvas)
        self.actualizar_interfaz()
        if self.combate.combate_terminado():
            self.finalizar_combate()

    def actualizar_interfaz(self):
        if self.combate is None:
            return
        jugador = self.combate.jugador
        enemigo = self.combate.enemigo
        self.arena.itemconfigure(self.nombre_jugador_canvas, text=jugador.nombre)
        self.arena.itemconfigure(self.nombre_enemigo_canvas, text=enemigo.nombre)
        porcentaje_jugador = max(0, min(1, jugador.vida / jugador.vida_maxima))
        porcentaje_enemigo = max(0, min(1, enemigo.vida / enemigo.vida_maxima))
        self.arena.coords(self.vida_jugador_canvas,
                          80, 273, 80 + 190 * porcentaje_jugador, 288)
        self.arena.coords(self.vida_enemigo_canvas,
                          510, 273, 510 + 190 * porcentaje_enemigo, 288)
        self.arena.itemconfigure(self.texto_vida_jugador_canvas,
                                text=f"Vida: {jugador.vida}/{jugador.vida_maxima}")
        self.arena.itemconfigure(self.texto_vida_enemigo_canvas,
                                text=f"Vida: {enemigo.vida}/{enemigo.vida_maxima}")
        self.texto_pociones.configure(
            text=f"✚ Pociones disponibles: {self.combate.pociones}")

    def finalizar_combate(self):
        self.actualizar_interfaz()
        if self.combate.jugador.esta_vivo():
            self.escribir_registro("🏆 ¡VICTORIA! Has derrotado al enemigo.")
        else:
            self.escribir_registro("Fin del combate. Tu personaje fue derrotado.")
        self.boton_atacar.configure(state="disabled")
        self.boton_pocion.configure(state="disabled")


if __name__ == "__main__":
    InterfazJuego()

