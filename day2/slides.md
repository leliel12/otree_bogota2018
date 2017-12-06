
---
title:  Python Batteries - oTree Concepts - Tutorial #0
author: Juan Cabral - jbc.develop@gmail.com
date: Jan, 2018
header-includes:
    - \usepackage{caption}

---

# Python Batteries

-   The Python source distribution has long maintained the philosophy of
    **"batteries included"** -- having a rich and versatile standard library
    which is immediately available, without making the user download separate
    packages. This gives the Python language a head start in many projects.
-   **However, the standard library modules aren't always the best choices for a job.**
-   How many functionalities have the python batteries? Try:

```python
import antigravity
```

\centerline{\includegraphics[height=50px]{imgs/batteries.jpeg}}

---

# Python Batteries - ``datetime`` module

The datetime module supplies classes for manipulating dates and times in both
simple and complex ways. While date and time arithmetic is supported, the
focus of the implementation is on efficient attribute extraction for output
formatting and manipulation.

- Full Documentation: https://docs.python.org/3/library/datetime.html


\centerline{\includegraphics[height=50px]{imgs/tm.png}}


----

# `datetime` module: Basic

```python
import datetime
now = datetime.datetime(2003, 8, 4, 12, 30, 45)

print(now)
# => 2003-08-04 12:30:45

print repr(now)
# => datetime.datetime(2003, 8, 4, 12, 30, 45)

print type(now)
# => <type 'datetime.datetime'>

print(now.year, now.month, now.day)
# => 2003 8 4

print(now.hour, now.minute, now.second)
# => 12 30 45
```

---

# `datetime` module: Convert from another type

```python
import datetime
import time

print(datetime.datetime(2003, 8, 4, 21, 41, 43))
# => 2003-08-04 21:41:43

datetime.datetime.today()

datetime.datetime.now()

datetime.datetime.fromtimestamp(time.time())

datetime.datetime.utcnow()

datetime.datetime.utcfromtimestamp(time.time())

```


---

# `datetime` module: to String

```python

>>> now = datetime.datetime.now()
>>> now
datetime.datetime(2017, 12, 5, 23, 37, 53, 112972)

>>> now.ctime()
'Tue Dec  5 23:37:53 2017'

>>> now.isoformat()
'2017-12-05T23:37:53.112972'

>>> now.strftime("%Y%m%dT%H%M%S")
'20171205T233753'

```

---

# `datetime` module: Algebra

```python

>>> past = datetime.datetime.now()
>>> past
datetime.datetime(2017, 12, 5, 23, 37, 53, 112972)


>>> datetime.datetime.now() - past
datetime.timedelta(0, 26, 329369)

>>> datetime.datetime.now() - past
datetime.timedelta(0, 27, 864966)

>>> datetime.datetime.now() - past
datetime.timedelta(0, 29, 289356)

```

---

# `datetime` module: Algebra 2

```python

>>> past = datetime.datetime.now()
>>> past
datetime.datetime(2017, 12, 5, 23, 42, 54, 209964)


>>> delta = datetime.datetime.now() - past
datetime.timedelta(0, 24, 168670)

>>> now = datetime.datetime.now()
>>> now
datetime.datetime(2017, 12, 5, 23, 43, 55, 510720)

>>> now + delta
datetime.datetime(2017, 12, 5, 23, 44, 19, 679390)

```

---

## `datetime` module

Resume:

-   The `datetime.datetime` type represents a date and a time during that
    day.
-   The `datetime.date` type represents just a date, between year 1 and
    9999
-   The `datetime.time` type represents a time, independent of the date.
-   The `datetime.timedelta` type represents the difference between two
    time or date objects.
-   The `datetime.tzinfo` type is used to implement timezone support for
    time and datetime objects (this will not be cover in this tutorial).
-   In servers always use **utcnow()**


---

# Python Batteries - ``random`` module

-   This module implements pseudo-random number generators for various distributions.

    For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.

    There are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions.

- Full Documentation: https://docs.python.org/3/library/random.html


\centerline{\includegraphics[height=50px]{imgs/random.png}}

---

# `random` module: basic

```python
>>> import random

# Random float:  0.0 <= x < 1.0
>>> random.random()
0.37444887175646646

# Random float:  2.5 <= x < 10.0
>>> random.uniform(2.5, 10.0)
3.1800146073117523

# Interval between arrivals averaging 5 seconds
>>> random.expovariate(1 / 5)
5.148957571865031

# Integer from 0 to 9 inclusive
>>> random.randrange(10)
7
```

---

# `random` module: basic 2

```python
# Even integer from 0 to 100 inclusive
>>> random.randrange(0, 101, 2)
26

# Single random element
>>> random.choice(['win', 'lose', 'draw'])
'draw'

# Shuffle a list
>>> deck = 'ace two three four'.split()
>>> random.shuffle(deck)
>>> deck
['four', 'two', 'ace', 'three']

# Four samples without replacement
>>> random.sample([10, 20, 30, 40, 50], k=4)
[40, 10, 50, 30]
```

---

# `random` module: Simulations

```python

>>> import collections
>>> import random

# Six roulette wheel spins
# (weighted sampling with replacement)
>>> random.choices(['red', 'black', 'green'],
                   [18, 18, 2], k=6)
['red', 'green', 'black', 'black', 'red', 'black']

# Deal 20 cards without replacement from a deck of
# 52 playing cards and determine the proportion of
# cards with a ten-value (a ten, jack, queen, or king).
>>> deck = collections.Counter(tens=16, low_cards=36)
>>> seen = random.sample(list(deck.elements()), k=20)
>>> seen.count('tens') / 20
0.15
```

---

# `random` module: Simulations 2

```python

>>> import random
>>> import statistics

# Estimate the probability of getting 5 or more heads
# from 7 spins of a biased coin that settles on
# heads 60% of the time.
>>> def trial():
       return random.sample.choices(
            'HT', cum_weights=(0.60, 1.00),
        k=7).count('H') >= 5
>>> statistics.mean(trial() for _ in range(10000))
0.4169
```

---

# `random` module: resume

-   `random` and `statistics` are useful in many cases but is not feature
    complete.
-   In complex cases you must install numpy and scipy

\centerline{\includegraphics[height=150px]{imgs/eco.png}}



----------------------------------------------------------------------

# References

-   https://docs.python.org/3/library/statistics.html
-   https://docs.python.org/3/library/collections.html
-   https://docs.python.org/3/library/itertools.html
-   https://docs.python.org/3/library/os.html
-   https://docs.python.org/3/library/random.html
-   https://docs.python.org/3/library/time.html
-   https://docs.python.org/3/library/datetime.html
-   https://www.python.org/dev/peps/pep-0206/
-   http://otree.readthedocs.io/en/latest/
