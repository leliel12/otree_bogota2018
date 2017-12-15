
---
title:  oTree Concepts \#2 - Tutorial \#2 - Bots.
author: Juan Cabral - jbc.develop@gmail.com
date: Jan, 2018
pandoc-latex-fontsize:
  - classes: [smallcontent]
    size: tiny
header-includes:
    - \usepackage{caption}

---

# Tutorial \#2: Trust Game.

\centerline{\includegraphics[height=150px]{imgs/code.png}}

- Open your console (Powershell, terminal, or any flaored pyton console)
- Open an editor (PyCharm, SublimeText, Kate, Atom...)
- Follow Me!

---

# Tutorial \#2: Trust Game.

-   Now let’s create a 2-player Trust game, and learn some more features of oTree.

    -   To start, Player 1 receives 10 points;
    -   Player 2 receives nothing.
    -   Player 1 can send some or all of his points to Player 2.
    -   Before P2 receives these points they will be tripled.
    -   Once P2 receives the tripled points he can decide to send some or all of
        his points to P1.

---

# Tutorial \#2: Trust Game.

## Define models.py

-   First we define our app’s constants. The endowment is 10 points and the
    donation gets tripled.
-   There are 2 critical data points to record: the “sent” amount from P1, and
    the “sent back” amount from P2.
-   Also, let’s define the payoff function in the Group class.

---

# Tutorial \#2: Trust Game.

## Define the templates and views

We need 3 pages:

1.  P1’s “Send” page
2.  P2’s “Send back” page
3.  “Results” page that both users see.
4.  It would also be good if game instructions appeared on each page so
    that players are clear how the game works.
5.  This game has 2 wait pages:
    a.  P2 needs to wait while P1 decides how much to send
    b.  P1 needs to wait while P2 decides how much to send back
    c.  After the second wait page, we should calculate the payoffs. So, we use
        **`after_all_players_arrive`**.
6.  Then we define the page sequence.

---

# Tutorial \#2: Trust Game.

## Settings and run

-   Add an entry to **`SESSION_CONFIGS`** in **`settings.py`**
-   Reset the database and run.


----------------------------------------------------------------------

# References

-   http://otree.readthedocs.io/en/latest/
-   http://blog.easylearning.guru/implementing-mtv-model-in-python-django/
-   https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
-   https://en.wikipedia.org/wiki/Django_(web_framework)
-   https://www.quora.com/What-is-a-Full-Stack-Web-framework
