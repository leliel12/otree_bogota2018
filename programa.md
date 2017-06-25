# Diseño de Experimentos de Ciencias Sociales con Python y oTree

Autor: Juan B Cabral jbc.develop@gmail.com

Este tutorial, persigue el objetivo de servir de introducción al lenguaje
de programación [Python](http://python.org); y a la plataforma para el
desarrollo de experimentos de ciencias sociales [oTree](http://www.otree.org/).

A lo largo de las 7 clases divididas en dos partes se expondrá conceptos
referentes a:

- Programar en Python.
- Gestionar entornos de desarrollo en Python.
- Comprender el modelo teórico detrás de oTree.
- Crear experimentos con oTree.
- Probar, depurar y desplegar experimentos con oTree.


## Parte 1: oTree y Python.

### Clase 1 - Fundamentos de Python.

- **Introducción:** ¿Que es Python?. Instalación. Interprete.
Características de Python. ¿Por qué usar Python en Ciencia?
- **Tipos Base:** `int`, `float`, `complex`, `str`, `list`, `tuple`,
`dict`, `set` y `None`. Valores de verdad.
- **Orientación a objetos:** Que es un objeto. Python como lenguaje orientado
  a objetos. Clases e Instancias. Ejemplo simple de herencia.


### Clase 2 - Librerías en Python - Conceptos de oTree - Tutorial #0.

- **Librerías:** `datetime`
  (manejo de fecha local y utc), `os` (interacción con el sistema operativo),
  `sh` (interacción con comandos externos) y `pip`
  (para instalar extensiones). Entornos virtuales con `virtualenv`.
- **Conceptos oTree** Sessions, Subsessions, Groups and Object hierarchy.
- **Tutorial 0:** Instalación de oTree y creación de una encuesta simple.


### Clase 3 - Git - Tutorial #1 - Objetos en oTree

- Breve introducción a control de versiones con Git.
- **Tutorial #1:** Public goods game.
- **Objetos en oTree:** Apps, Models, Views, Templates And Forms.


### Clase 4 -  Conceptos de oTree #2 - Tutorial #2 - Bots.

- **Tutorial #2:** Trust Game.
- **Conceptos:** Grupos y juegos multiplayer. Puntos y dinero. Tratamientos.
  Rounds y salas.
- Testing.


## Parte 2: oTree Avanzado.

### Clase 5 - Configuraciones, Internacionalización y Depuración - Tutorial #3.

- Archivo de configuraciones `settings.py`.
- Internacionalización con archivos `.po`.
- Como hacer depuración (`pdb` e `ipdb`)
- **Tutorial #3:** Matching Pennies.


### Clase 6 - Experimentos Reales Complejos.

- **Real Effort:** Particularidad: generación de texto dentro de imágenes.
- **Toilet Game:** Particularidad: incluye un chat rudimentario.


### Clase 7 - Despliegues y Mechanical Turk.

- **Despliegues:** Despliegues en Heroku y despliegues locales. Bases de datos
en producción.
- **MTurk:** Exponiendo el juego en mechanical turk.


## Bibliografía

### Básica.

- **Python Tutorial:** https://docs.python.org/3/tutorial/
- **oTree Documentation:** http://otree.readthedocs.io

### Referencia.

- **Python Documentation:** https://docs.python.org/3/
- **Sh:** https://amoffat.github.io/sh/
- **Heroku Dev Center:** https://devcenter.heroku.com
- **Git Tutorial:** https://git-scm.com/docs/gittutorial
- **Mechanical Turk:** https://aws.amazon.com/documentation/mturk/
- **GNU gettext:** https://www.gnu.org/software/gettext/
- **Poedit:** https://poedit.net/
- **Public Goods Game:** https://en.wikipedia.org/wiki/Public_goods_game
- **Dictator Game (Trust):** https://en.wikipedia.org/wiki/Dictator_game
- **Coordination Game (Real-Effort):** https://en.wikipedia.org/wiki/Coordination_game
- **Matching Pennies Game:** https://en.wikipedia.org/wiki/Matching_pennies
- **Toilet Game:** https://www.scq.ubc.ca/a-game-theoretic-approach-to-the-toilet-seat-problem/


## Referencias.

> Python Software Foundation. The Python Programing Language. Retrieved June
  25, 2017, from https://www.python.org/

> Chen, D. L., Schonger, M., & Wickens, C. (2016). oTree—An open-source
  platform for laboratory, online, and field experiments. Journal of Behavioral
  and Experimental Finance, 9, 88-97.

> Middleton, N., & Schneeman, R. (2013). Heroku: Up and Running: Effortless
  Application Deployment and Scaling. " O'Reilly Media, Inc.".

> Loeliger, J., & McCullough, M. (2012). Version Control with Git: Powerful
  tools and techniques for collaborative software development. "
  O'Reilly Media, Inc.".

> Buhrmester, M., Kwang, T., & Gosling, S. D. (2011). Amazon's Mechanical
  Turk: A new source of inexpensive, yet high-quality, data?. Perspectives on
  psychological science, 6(1), 3-5.

> Drepper, U., Meyering, J., Pinard, F., & Haible, B. (2015). GNU gettext
  tools: Native Language Support Library and Tools. Samurai Media Limited.

> Ledyard, J. (1997). Public goods: A survey of experimental research
  (No. 509). David K. Levine.

> Kahneman, D., Knetsch, J. L., & Thaler, R. H. (1986). Fairness and the
  assumptions of economics. Journal of business, S285-S300.

> Dutcher, G., Salmon, T., & Saral, K. J. (2015). Is' Real'Effort More Real?.

> Harter, R. (2005). A game theoretic approach to the toilet seat
  problem. Science Creative Quarterly.

> Camerer, C. (2010). Behavioral game theory. New Age International.
