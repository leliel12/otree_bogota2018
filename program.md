# Designing Social Science Experiments with Python and oTree

Autor: Juan B Cabral jbc.develop@gmail.com

Este tutorial, persigue el objetivo de servir de introducc{on al lenguaje
de programación [Python](http://python.org) ya la plataforma para el
desarrollo de experimentos de ciencias sociales [oTree](http://www.otree.org/).
A lo largo de las 7 clases divididas en dos partes se mostrara como:

- Programar en Python.
- Gestionar entornos de desarrolo en Python.
- Comprender el modelo teorico detrás de oTree.
- Crear experimentos con oTree.
- Probar, depurar y desplegar experimentos con oTree.


### Parte 1: oTree y Python

### Clase 1 - Python Fundamentals

- **Introducción:** ¿Que es Python?. Instalación. Interprete.
Características de Python. ¿Por qué usar Python en Ciencia?
- **Tipos Base:** `int`, `float`, `complex`, `str`, `list`, `tuple`,
`dict`, `set` y `None`. Valores de verdad.
- **Orientación a objetos:** Que es un objeto. Python como lenguaje orientado
  a objetos. Clases e Instancias. Ejemplo simple de herencia.


### Clase 2 - Librerías en Python - Conceptos de oTree - Tutorial#0

- **Librerías:** `datetime`
  (manejo de fecha local y utc), `os` (interacción con el sistema operativo),
  `sh` (interacción com comandos externos) y `pip`
  (para instalar extensiones). Entornos virtuales con `virtualenv`.
- **Conceptos oTree** Sessions, Subsession, Groups and Object hierarchy.
- **Tutorial 0:** Instalación de oTree y creación de una encuesta simple.


### Clase 3 - Tutorial #1 - Objetos en oTree

- **Tutorial #1:** Public goods game
- **Objetos en oTree:** Apps, Models, Views, Templates And Forms


### Clase 4 -  Conceptos de oTree #2 - Tutorial #2 - Bots

- **Tutorial #2:** Trust Game
- **Conceptos:** Grupos y juegos multiplayer; putos y dinero, tratamientos,
  rounds y salas.
- Testing


## Parte 2: oTree Avanzado

### Clase 5 - Configuraciones, Internacionalización y Depuracón - Tutorial #3

- Archivo de configuraciones `settings.py`.
- Internacionalizacion con archivos `.po`.
- Como hacer depuración (`pdb` e `ipdb`)
- **Tutorial #3:** Matching Pennies

### Clase 6 - Experimentos Reales Complejos

- **Real effort:** Particularidad: generación de texto dentro de imágenes
- **Toilet Game:** Particularidad: incluye un chat rudimentario.


### Clase 7 - Despliegues y Mechanical Turk

- **Despliegues:** Despliegues en Heroku y despliegues locales. Bases de datos
en producción
- **MTurk:** Exponiendo el juego en mechanical turk.
