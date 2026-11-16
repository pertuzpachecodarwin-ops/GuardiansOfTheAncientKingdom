# Guardians of the Ancient Kingdom

## Descripción del proyecto

Guardians of the Ancient Kingdom es un videojuego de combate por turnos desarrollado en Python utilizando programación orientada a objetos y la biblioteca CustomTkinter para su interfaz gráfica.

El jugador puede seleccionar entre tres personajes: Guerrero, Mago y Arquero. Cada personaje cuenta con características y ataques diferentes, y debe enfrentarse a un enemigo controlado por el programa.

## Objetivo

Desarrollar una aplicación que permita aplicar los principales conceptos de la programación orientada a objetos mediante un videojuego interactivo con interfaz gráfica.

## Tecnologías utilizadas

- Python 3.
- CustomTkinter.
- Pytest.

## Características principales

- Selección de personajes.
- Sistema de combate por turnos.
- Ataques con diferentes valores de daño.
- Sistema de vida para jugador y enemigo.
- Uso de pociones de curación.
- Registro de acciones durante el combate.
- Mensajes de victoria y derrota.

## Conceptos de programación orientada a objetos

- **Abstracción:** clase base Personaje.
- **Herencia:** Guerrero, Mago, Arquero y Enemigo heredan de Personaje.
- **Encapsulamiento:** atributos protegidos y propiedades para consultar los valores.
- **Polimorfismo:** cada personaje implementa su propio método atacar.
- **Relaciones entre objetos:** la clase Combate trabaja con los personajes participantes.

## Estructura del proyecto

```text
GuardiansOfTheAncientKingdom/
│
├── main.py
├── interfaz.py
├── personajes.py
├── combate.py
├── requirements.txt
├── README.md
│
├── docs/
│   └── INFORME_TECNICO.md
│
└── pruebas/
    └── test_personajes.py
```

## Instalación

1. Tener Python instalado.
2. Abrir una terminal en la carpeta del proyecto.
3. Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

4. Ejecutar la aplicación:

```bash
python main.py
```

## Ejecución de las pruebas

Para ejecutar las pruebas automatizadas, instalar Pytest:

```bash
python -m pip install pytest
```

Después ejecutar:

```bash
python -m pytest -v
```

El proyecto cuenta con siete pruebas automatizadas para verificar el funcionamiento de los personajes, ataques, curaciones, vida, abstracción y pociones.

## Autor

Proyecto académico desarrollado para la asignatura de Programación Orientada a Objetos.