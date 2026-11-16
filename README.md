# ⚔️ Guardians of the Ancient Kingdom

**Videojuego RPG de combate por turnos desarrollado en Python utilizando Programación Orientada a Objetos (POO).**

## 📖 Descripción

Guardians of the Ancient Kingdom es un videojuego de fantasía medieval en el que el jugador selecciona un personaje y se enfrenta a un Orco mediante combates por turnos.

El proyecto fue desarrollado como parte del Parcial Integrador de Programación Orientada a Objetos.

## 🎮 Características principales

- Selección de tres personajes: Guerrero, Mago y Arquero.
- Combate por turnos contra un enemigo controlado por el programa.
- Sistema de ataque y reducción de vida.
- Pociones para recuperar salud.
- Barras de vida actualizadas durante el combate.
- Registro de acciones y resultados.
- Detección de victoria y derrota.
- Opción para reiniciar el combate.
- Interfaz gráfica de fantasía medieval.
- Imágenes de personajes con fondo transparente.
- Escenario de bosque encantado.
- Versión ejecutable para Windows.

## 🛡️ Personajes

| Personaje | Clase | Vida | Daño |
|---|---|---|---|
| Arthas | Guerrero | 100 | 30 |
| Gandalf | Mago | 80 | 45 |
| Legolas | Arquero | 80 | 42 |
| Orco | Enemigo | 100 | 15 |

## 🧠 Programación Orientada a Objetos

El videojuego aplica los siguientes conceptos:

- **Abstracción:** clase abstracta `Personaje`.
- **Herencia:** clases `Guerrero`, `Mago`, `Arquero` y `Enemigo`.
- **Polimorfismo:** cada personaje implementa su propio método `atacar()`.
- **Encapsulamiento:** atributos protegidos y propiedades para gestionar las estadísticas.
- **Relación entre objetos:** la clase `Combate` administra los personajes participantes.

## 🛠️ Tecnologías utilizadas

- Python 3
- CustomTkinter
- Tkinter Canvas
- Pillow
- Pytest
- PyInstaller
- Git y GitHub

## 📂 Estructura del proyecto

```text
GuardiansOfTheAncientKingdom/
├── assets/
│   ├── fondo.png
│   ├── guerrero.png
│   ├── mago.png
│   ├── arquero.png
│   └── orco.png
├── docs/
│   └── INFORME_TECNICO.md
├── pruebas/
│   └── test_personajes.py
├── main.py
├── personajes.py
├── combate.py
├── interfaz.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Instalación y ejecución

Para ejecutar el proyecto desde el código fuente:

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto.
3. Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

4. Ejecutar el videojuego:

```bash
python main.py
```

## 💻 Descargar el videojuego para Windows

El juego también está disponible como archivo ejecutable.

**[Descargar desde GitHub Releases](https://github.com/pertuzpachecodarwin-ops/GuardiansOfTheAncientKingdom/releases)**

Descarga el archivo ejecutable de la versión más reciente y ábrelo en Windows. No es necesario instalar Python.

## 🧪 Pruebas automatizadas

El proyecto incluye pruebas con Pytest para comprobar el funcionamiento de las clases y las reglas del combate.

Para ejecutarlas:

```bash
python -m pytest -v
```

Se implementaron siete pruebas relacionadas con ataques, bonificaciones, límites de vida, abstracción y uso de pociones.

## 📋 Documentación técnica

La carpeta `docs` contiene el informe técnico del proyecto, donde se describen su diseño, implementación y aplicación de los principios de POO.

## 🔖 Historial de versiones

### v1.0.0 — Primera versión ejecutable

- Implementación del sistema de combate.
- Desarrollo de la interfaz gráfica.
- Incorporación de imágenes de personajes.
- Integración del escenario de bosque encantado.
- Implementación de pruebas automatizadas.
- Generación del ejecutable para Windows.
- Publicación del proyecto en GitHub.

## 👨‍💻 Autor

Darwin Jabid Pertuz Pacheco

Universidad Americana

Proyecto académico de Programación Orientada a Objetos.