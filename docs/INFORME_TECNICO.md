# INFORME TÉCNICO — Guardians of the Ancient Kingdom

**Asignatura:** Programación Orientada a Objetos con Python  
**Proyecto:** Parcial integrador  
**Autor:** Darwin Jabid Pertuz Pacheco  
**Institución:** Universidad Americana  
**Versión documentada:** v1.0.0 (noviembre de 2026)  
**Repositorio:** https://github.com/pertuzpachecodarwin-ops/GuardiansOfTheAncientKingdom

## 1. Análisis del problema

Se planteó desarrollar una aplicación de escritorio que permitiera demostrar, de forma visual e interactiva, los principios de programación orientada a objetos (POO). El problema de diseño consistía en representar distintos personajes con atributos comunes y ataques diferentes, controlar el estado de un combate por turnos y comunicar sus resultados al usuario sin mezclar todas las responsabilidades en un solo archivo.

**Usuarios previstos:** estudiantes y personas interesadas en un videojuego RPG sencillo. **Alcance:** combate local de un jugador contra un Orco controlado por el programa. **Limitaciones:** no tiene juego en red, guardado de partidas ni base de datos; está pensado principalmente para Windows en su versión ejecutable.

## 2. Objetivos

**General:** construir un videojuego de combate por turnos en Python con interfaz gráfica, aplicando de manera funcional los conceptos fundamentales de POO.

**Específicos:**

1. Modelar personajes mediante una clase abstracta y clases derivadas.
2. Separar las reglas del combate de su presentación gráfica.
3. Permitir seleccionar personaje, atacar, usar pociones y reiniciar la partida.
4. Visualizar personajes, escenario, barras de vida y registro de acciones.
5. Comprobar reglas principales mediante pruebas automatizadas.
6. Documentar y publicar el código y un ejecutable de Windows en GitHub.

## 3. Diseño inicial y clases identificadas

Se escogió una temática de fantasía medieval. La propuesta inicial era un combate sencillo entre personajes; posteriormente se incorporó una interfaz gráfica y recursos visuales.

| Clase | Archivo | Responsabilidad |
|---|---|---|
| `Personaje` | `personajes.py` | Definir atributos y comportamientos compartidos, incluido el contrato de ataque. |
| `Guerrero` | `personajes.py` | Ejecutar el ataque del guerrero. |
| `Mago` | `personajes.py` | Ejecutar el ataque del mago con bonificación. |
| `Arquero` | `personajes.py` | Ejecutar el ataque del arquero con bonificación. |
| `Enemigo` | `personajes.py` | Representar al adversario controlado por el juego. |
| `Combate` | `combate.py` | Coordinar ataques, pociones y finalización de la partida. |
| `InterfazJuego` | `interfaz.py` | Construir la ventana, procesar eventos y actualizar elementos visuales. |

Los personajes implementados son **Arthas** (Guerrero, 100 de vida, ataque 30), **Gandalf** (Mago, 80 de vida, ataque base 40 y daño 45), **Legolas** (Arquero, 80 de vida, ataque base 40 y daño 42) y **Orco** (Enemigo, 100 de vida, ataque 15).

## 4. Arquitectura y organización

El proyecto separa el modelo de personajes, la lógica de combate, la interfaz y los recursos:

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
├── personajes.py
├── combate.py
├── interfaz.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

`main.py` inicia `InterfazJuego`. La interfaz crea un `Combate` con el personaje seleccionado y el enemigo. Cuando se pulsa un botón, la interfaz llama a los métodos de `Combate`; este utiliza los métodos de los personajes y devuelve mensajes. Finalmente, la interfaz actualiza la vida, las imágenes y el registro. Así, la lógica no depende de los controles gráficos.

**Relaciones:** `Guerrero`, `Mago`, `Arquero` y `Enemigo` **heredan** de `Personaje`. `Combate` mantiene referencias a los dos participantes (relación de **asociación/agregación**, pues los personajes se crean antes de entregarse al combate). `InterfazJuego` crea y utiliza un objeto `Combate` para administrar la partida activa.

## 5. Aplicación de los principios de POO

| Concepto | Ubicación | Aplicación |
|---|---|---|
| Clases y objetos | `personajes.py`, `combate.py`, `interfaz.py` | Cada personaje y partida se representa mediante instancias con estado y comportamiento. |
| Abstracción | `Personaje` | Hereda de `ABC` y declara `atacar()` con `@abstractmethod`, evitando instanciar directamente una clase incompleta. |
| Herencia | `Guerrero`, `Mago`, `Arquero`, `Enemigo` | Reutilizan vida, nombre, ataque y métodos comunes de `Personaje`. |
| Polimorfismo | `atacar(objetivo)` | El mismo método produce comportamientos distintos según la clase del atacante. |
| Encapsulamiento | `_vida`, `_vida_maxima`, `_ataque` | Las propiedades permiten consultar valores; `recibir_danio()` y `curar()` controlan sus límites. |
| Relaciones | `Combate` y personajes | Un combate administra un jugador y un enemigo sin implementar de nuevo las reglas de cada personaje. |

**Ejemplo de polimorfismo:** el Guerrero usa su ataque base (30); el Mago añade 5 puntos a su ataque base (40 + 5 = 45); el Arquero añade 2 (40 + 2 = 42). El sistema de combate invoca `atacar()` sin necesitar implementar cada tipo de ataque dentro de la interfaz.

**Protección del estado:** al recibir daño, la vida no puede descender de cero; al curar, no puede superar la vida máxima. El método `esta_vivo()` permite conocer si un personaje puede continuar.

## 6. Construcción de la interfaz gráfica

Se utilizó **CustomTkinter** para la ventana, los paneles, botones y selección de personajes. Para el escenario se incorporó **Tkinter Canvas** y **Pillow**, que permiten dibujar el bosque y superponer las imágenes PNG de los personajes sin los bloques opacos que aparecían en las primeras versiones.

**Elementos implementados:**

- Panel izquierdo de selección entre Guerrero, Mago y Arquero, con imagen y estadísticas.
- Arena central con fondo de bosque encantado, personaje del jugador, Orco y barras de vida.
- Botones **Iniciar combate**, **Atacar**, **Usar poción** y **Reiniciar**.
- Contador de pociones y registro de mensajes de combate.
- Mensajes de victoria o derrota y bloqueo de acciones al finalizar el combate.

**Eventos y comunicación:** `Iniciar combate` crea los objetos; `Atacar` llama a `atacar_enemigo()` y, si procede, a `enemigo_ataca()`; `Usar poción` llama a `usar_pocion()`; `Reiniciar` comienza una nueva partida. Los controles se actualizan a partir del estado real de los objetos.

**Capturas de pantalla para incluir en la entrega:**

1. **Pantalla principal:** selección del personaje y arena del bosque.
2. **Combate en curso:** barras de vida modificadas y mensajes de ataque.
3. **Resultado final:** victoria o derrota visible en el registro.

> **Pendiente de insertar capturas:** guardar imágenes propias en `docs/imagenes/` y añadir aquí los enlaces Markdown correspondientes. No se incluyen capturas inventadas.

## 7. Proceso de desarrollo

1. **Idea y alcance:** se eligió un RPG de combate por turnos para demostrar POO.
2. **Modelo de objetos:** se desarrollaron `Personaje`, las clases derivadas y `Combate`.
3. **Interfaz inicial:** se implementaron selección, barras de vida, botones y registro con CustomTkinter.
4. **Pruebas:** se instalaron Pytest y se ejecutaron siete pruebas automatizadas.
5. **Mejoras visuales:** se añadieron recursos PNG, bosque encantado y diseño de fantasía medieval.
6. **Corrección de presentación:** se sustituyó la arena basada en paneles por un `Canvas` para evitar rectángulos opacos detrás de los personajes.
7. **Distribución:** se generó un `.exe` mediante PyInstaller y se comprobó que abre y funciona.
8. **Publicación:** se subió el código a GitHub y se creó una versión `v1.0.0` en Releases; también se actualizó el README.

## 8. Pruebas realizadas

En la ejecución compartida de `python -m pytest -v` se recopilaron **7 pruebas** y todas finalizaron con **PASSED**:

| Prueba | Comportamiento verificado | Resultado |
|---|---|---|
| `test_guerrero_ataca` | Ataque del Guerrero | PASSED |
| `test_mago_tiene_bono_de_ataque` | Bonificación de daño del Mago | PASSED |
| `test_arquero_tiene_bono_de_ataque` | Bonificación de daño del Arquero | PASSED |
| `test_la_vida_no_puede_ser_negativa` | Límite inferior de vida | PASSED |
| `test_curacion_no_supera_vida_maxima` | Límite superior de curación | PASSED |
| `test_no_se_puede_instanciar_personaje_abstracto` | Restricción de la clase abstracta | PASSED |
| `test_no_se_puede_usar_pocion_si_no_quedan` | Caso inválido: ausencia de pociones | PASSED |

También se probó manualmente el juego con selección de personajes, ataque, curación, reinicio y ejecución desde el `.exe`. El usuario confirmó que el ejecutable abrió correctamente.

**Comando para repetir las pruebas:**

```bash
python -m pytest -v
```

## 9. Problemas técnicos encontrados y soluciones

| Problema encontrado | Causa | Solución aplicada |
|---|---|---|
| `ModuleNotFoundError: No module named 'PIL'` | Pillow no estaba instalado en el entorno de Python. | Se instaló con `python -m pip install pillow` y se añadió como dependencia. |
| `SyntaxError: invalid syntax` en `fg_color` | Faltaba una coma entre argumentos al editar un panel. | Se corrigió `fg_color="#211A30",`. |
| `ValueError: ['imagen'] are not supported arguments` | Se escribió `imagen=` en lugar del parámetro inglés `image=` de CustomTkinter. | Se corrigió el argumento y se separó la referencia de imagen del widget. |
| `_tkinter.TclError: unknown option "-relheigth"` | Error tipográfico en el método `place()`. | Se reemplazó `relheigth` por `relheight`. |
| Rectángulos morados detrás de los personajes | `fg_color="transparent"` en CustomTkinter no produce transparencia real sobre fotografías. | Se utilizó `tk.Canvas` con imágenes PNG superpuestas al fondo. |
| `git` no se reconocía inicialmente | Git no estaba disponible en la terminal. | Se instaló/configuró Git; posteriormente `git --version` respondió correctamente y se inicializó el repositorio. |
| GitHub rechazaba adjuntos `.exe` y `.zip` desde el navegador | La carga de archivos falló en la interfaz web; no se confirmó una causa única. | Se utilizó GitHub CLI para autenticar y publicar la versión. |

Estos problemas muestran el proceso de depuración de dependencias, sintaxis, parámetros de interfaz, composición visual y distribución.

## 10. Tecnologías y justificación

| Herramienta | Uso | Motivo |
|---|---|---|
| Python 3 | Lógica y clases | Lenguaje de la asignatura y soporte de POO. |
| CustomTkinter | Controles gráficos | Facilita una interfaz moderna con botones y paneles. |
| Tkinter Canvas | Arena de combate | Permite superponer imágenes y texto en el escenario. |
| Pillow | Imágenes | Abre y prepara los recursos PNG para mostrarlos. |
| Pytest | Pruebas automatizadas | Comprueba reglas y casos inválidos. |
| PyInstaller | Ejecutable Windows | Permite distribuir el juego sin exigir Python al usuario final. |
| Git y GitHub | Control de versiones | Mantienen historial de commits y repositorio público. |
| GitHub CLI | Publicación de Releases | Permitió completar la publicación cuando falló la carga web. |

## 11. Instalación, ejecución y distribución

Para ejecutar desde el código fuente:

```powershell
python -m pip install -r requirements.txt
python main.py
```

Para ejecutar pruebas:

```powershell
python -m pytest -v
```

Para construir el ejecutable en Windows, desde la raíz del proyecto:

```powershell
python -m pip install pyinstaller
python -m PyInstaller --noconfirm --clean --onefile --windowed --name "GuardiansOfTheAncientKingdom" --add-data "assets;assets" --collect-all customtkinter main.py
```

La aplicación utiliza una ruta de recursos compatible con la ejecución normal y con los archivos empaquetados por PyInstaller (`sys._MEIPASS` cuando corresponda). El ejecutable se genera en `dist/`.

**Distribución:** https://github.com/pertuzpachecodarwin-ops/GuardiansOfTheAncientKingdom/releases

## 12. Conclusiones

El proyecto permitió aplicar los principios de POO en un programa funcional: las clases modelan los personajes, el polimorfismo diferencia sus ataques y la clase `Combate` administra las reglas de la partida. La separación de responsabilidades facilitó mejorar la presentación sin rehacer la lógica.

Las siete pruebas automatizadas aportaron evidencia del funcionamiento de reglas clave, incluido un caso inválido. Las correcciones de interfaz demostraron la importancia de conocer las limitaciones de las bibliotecas gráficas y de probar los cambios de forma incremental.

Finalmente, la publicación del código y del ejecutable permite entregar tanto una versión revisable por el docente como una aplicación que se puede probar directamente en Windows.

## 13. Mejoras futuras (no requeridas para v1.0.0)

- Animaciones de ataque y recepción de daño más elaboradas.
- Pantalla de victoria y derrota independiente.
- Efectos visuales de curación.
- Menú principal e instrucciones dentro del juego.

Estas ideas se consideran mejoras futuras; **no se presentan como funciones ya implementadas**.
