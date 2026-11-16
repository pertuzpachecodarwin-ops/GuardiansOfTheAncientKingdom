# INFORME TÉCNICO
## Guardians of the Ancient Kingdom

### 1. Introducción

El presente proyecto consiste en el desarrollo de un videojuego llamado Guardians of the Ancient Kingdom, elaborado en Python mediante el paradigma de programación orientada a objetos.

El juego permite seleccionar un personaje y participar en un combate por turnos contra un enemigo. Cuenta con una interfaz gráfica que facilita la interacción del usuario.

### 2. Objetivo general

Desarrollar una aplicación interactiva que permita demostrar la aplicación de los principios fundamentales de la programación orientada a objetos mediante un videojuego de combate.

### 3. Tecnologías utilizadas

- Python 3: lenguaje de programación utilizado.
- CustomTkinter: biblioteca utilizada para desarrollar la interfaz gráfica.
- Pytest: herramienta utilizada para realizar las pruebas automatizadas.
- Visual Studio Code: entorno utilizado para desarrollar el proyecto.

### 4. Descripción del funcionamiento

El funcionamiento del videojuego se desarrolla de la siguiente manera:

1. El usuario inicia la aplicación.
2. Selecciona uno de los personajes disponibles: Guerrero, Mago o Arquero.
3. Inicia el combate contra un enemigo.
4. El jugador puede atacar o utilizar una poción de curación.
5. El enemigo responde a los ataques cuando corresponde.
6. El combate termina cuando el jugador o el enemigo pierde toda su vida.
7. La interfaz muestra el resultado del combate.

### 5. Diseño orientado a objetos

El proyecto utiliza los siguientes conceptos de programación orientada a objetos:

**Abstracción:**

Se implementa mediante la clase abstracta Personaje, que establece una estructura común para los diferentes tipos de personajes.

**Herencia:**

Las clases Guerrero, Mago, Arquero y Enemigo heredan los atributos y métodos de la clase Personaje.

**Encapsulamiento:**

Se utilizan atributos protegidos para controlar el acceso a información como la vida y el ataque de los personajes. También se utilizan propiedades para consultar sus valores.

**Polimorfismo:**

Cada tipo de personaje implementa su propio método atacar, permitiendo que los ataques tengan comportamientos diferentes.

**Relación entre objetos:**

La clase Combate se relaciona con los objetos jugador y enemigo para controlar las acciones y el desarrollo de cada enfrentamiento.

### 6. Descripción de los archivos

- **main.py:** inicia la aplicación.
- **interfaz.py:** contiene la ventana gráfica y los controles del videojuego.
- **personajes.py:** contiene la clase abstracta Personaje y sus clases derivadas.
- **combate.py:** administra los ataques, las pociones y el estado del combate.
- **test_personajes.py:** contiene las pruebas automatizadas.
- **README.md:** presenta la información general y las instrucciones de ejecución.

### 7. Pruebas realizadas

Se utilizó Pytest para comprobar el funcionamiento de los componentes principales del videojuego.

Se realizaron siete pruebas:

1. Verificar que el Guerrero cause el daño esperado.
2. Comprobar el bono de ataque del Mago.
3. Comprobar el bono de ataque del Arquero.
4. Verificar que la vida no sea negativa.
5. Comprobar que la curación no supere la vida máxima.
6. Verificar que no se pueda instanciar directamente la clase abstracta Personaje.
7. Comprobar que no se pueda utilizar una poción cuando no quedan disponibles.

**Resultado:** las siete pruebas fueron aprobadas correctamente (7 passed).

### 8. Problemas técnicos y soluciones

**Problema 1: Contenido de la interfaz gráfica cortado.**

Durante la ejecución inicial, algunos elementos de la ventana, especialmente el registro del combate, no se visualizaban completamente.

**Solución:** se aumentó la altura de la ventana de 650 a 720 píxeles para permitir que todos los elementos se mostraran correctamente.

**Problema 2: Instalación y disponibilidad de dependencias.**

Durante la preparación de las pruebas se verificó la instalación de Pytest. La terminal indicó que los paquetes se encontraban instalados en el perfil del usuario porque la instalación global no estaba disponible.

**Solución:** se verificó la disponibilidad de Pytest y se utilizó el comando `python -m pytest -v` para ejecutar las pruebas con el mismo intérprete de Python utilizado en el proyecto.

### 9. Conclusiones

El desarrollo de Guardians of the Ancient Kingdom permitió aplicar los conceptos fundamentales de la programación orientada a objetos en una aplicación funcional.

Se logró implementar una interfaz gráfica, diferentes tipos de personajes, un sistema de combate y pruebas automatizadas.

Además, el proyecto permitió comprender la importancia de organizar el código en diferentes módulos y utilizar herramientas de prueba para verificar su funcionamiento.

### 10. Evidencias

En esta sección se deben agregar capturas de pantalla que demuestren:

- La ventana principal del videojuego.
- La selección de personajes.
- Un combate en ejecución.
- El resultado de las siete pruebas aprobadas.