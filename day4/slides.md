
---
title:  oTree Concepts \#2 - Tutorial \#2
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

\centerline{\includegraphics[height=150px]{imgs/setup_and_run.png}}

---

# oTree Concepts \#2.
## Groups

-   oTree’s group system lets you divide players into groups and have players
    interact with others in the same group. This is often used in multiplayer games.
-   To set the group size, go to your app’s **`models.py`** and set
    **`Constants.players_per_group`**.

```python
class Constants(BaseConstants):
    ...
    players_per_group = 2
```

---

# oTree Concepts \#2 - Multiplayer Games
## Groups

-   If all players should be in the same group, or if it’s a single-player
    game, set it to **`None`**:

```python
class Constants(BaseConstants):
    # ...
    players_per_group = None
```

-   In this case, **`self.group.get_players()`** and
    **`self.subsession.get_players()`** has the same behavior.
-   Each player has an attribute **`id_in_group`**, which will tell you if it
    is player 1, player 2, etc.


---

# oTree Concepts \#2 - Multiplayer Games
## Getting players

Group objects have the following methods:

-   **`get_players()`**: Returns a list of the players in the group
    (ordered by `id_in_group`).
-   **`get_player_by_id(n)`**: Returns the player in the group with the given
    `id_in_group`.

\centerline{\includegraphics[height=120px]{imgs/player_select.png}}

---

# oTree Concepts \#2 - Multiplayer Games
## Getting players

-   **`get_player_by_role(r)`**: Returns the player with the given role.
    If you use this method, you must define the role method. For example:

```python
class Group(BaseGroup):
    def set_payoff(self):
        buyer = self.get_player_by_role('buyer')

class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'buyer'
        return 'seller'
```


---

# oTree Concepts \#2 - Multiplayer Games
## Getting other players

**`Player`** objects have methods **`get_others_in_group()`** and
**`get_others_in_subsession()`** that return a **`list`** of the other players
in the group and subsession. For example, with 2-player groups you can get
the partner of a player:

```python
class Player(BasePlayer):

    def get_partner(self):
        return self.get_others_in_group()[0]
```


---

# oTree Concepts \#2 - Multiplayer Games
## Group matching - Fixed matching

-   By default, in each round, players are split into groups of
    size **`Constants.players_per_group`**.
-   They are grouped sequentially – for example:

    >   if there are 2 players per group,
        then P1 and P2 would be grouped together, and so would P3 and P4, and
        so on.

-   **`id_in_group`** is also assigned sequentially within each group.
-   This means that by default, the groups are the same in each round, and
    even between apps that have the same **`players_per_group`**.
-   If you want to rearrange groups, you can use the next techniques.

---

# oTree Concepts \#2 - Multiplayer Games
## Group matching - **`group_randomly()`**

-   Subsessions have a method **`group_randomly()`** that shuffles players
    randomly, so they can end up in any group, and any position within the group.
-   For example, this will group players randomly each round:

```python
class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
```

---

# oTree Concepts \#2 - Multiplayer Games
## Group matching - **`group_randomly()`**

-   If you would like to shuffle players between groups but keep players in
    fixed roles, use **`group_randomly(fixed_id_in_group=True)`**:

```python
class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)

```

---

# oTree Concepts \#2 - Multiplayer Games
## Group matching - **`group_like_round()`**

-   To copy the group structure from one round to another round, use the
    **`group_like_round(n)`** method.
-   The argument to this method is the round number whose group structure
    should be copied.
-   In the below example, the groups are shuffled in round 1, and then
    subsequent rounds copy round 1’s grouping structure.

```python
class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            # <some shuffling code here>
        else:
            self.group_like_round(1)
```


---

# oTree Concepts \#2 - Multiplayer Games
## Group matching - **`get_group_matrix()`**

-   Subsessions have a method called **`get_group_matrix()`**
    that return the structure of groups as a matrix, i.e. a list of lists,
    with each sublist being the players in a group, ordered by
    **`id_in_group`**.
-   The following lines are equivalent.

```python
matrix = self.get_group_matrix()
# === is equivalent to ===
matrix = [
    group.get_players()
    for group in self.get_groups()]
```

---

# oTree Concepts \#2 - Multiplayer Games
## Group matching - **`set_group_matrix()`**

-   **`set_group_matrix()`** lets you modify the group structure in any way
    you want.
-   You can modify the list of lists returned by `get_group_matrix()`,
    using regular Python list operations, and then pass this modified matrix
    to **`set_group_matrix()`**.

\centerline{\includegraphics[height=120px]{imgs/matrix.png}}


---

# oTree Concepts \#2 - Multiplayer Games
## Group matching - **`set_group_matrix()`**

-   Here is how this would look in **`creating_session`**:

```python
class Subsession(BaseSubsession):
    def creating_session(self):
        matrix = self.get_group_matrix()
        for row in matrix:
            row.reverse()
        self.set_group_matrix(matrix)
```

---

# oTree Concepts \#2 - Multiplayer Games
## Group matching - **`set_group_matrix()`**

-   You can also pass a matrix of integers. It must contain all integers
    from **1** to the number of players in the subsession.
-   Each integer represents the player who has that id_in_subsession. For example:

```python
>>> new_structure = [[1, 3,  5],
...                  [7, 9, 11],
...                  [2, 4,  6],
...                  [8,10, 12]]
>>> self.set_group_matrix(new_structure)
>>> self.get_group_matrix()
```

-   You can even use **`set_group_matrix`** to make groups of uneven sizes.

---

# oTree Concepts \#2 - Multiplayer Games
## Group matching - **`group.set_players()`**

-   If you just want to rearrange players within a group, you can use the
    method on **`group.set_players()`** that takes as an argument a list of
    the players to assign to that group, in order.
-   For example, if you want players to be reassigned to the same groups but
    to have roles randomly shuffled around within their groups
    (e.g. so player 1 will either become player 2 or remain player 1),
    you would do this:

```python
class Subsession(BaseSubsession):

    def creating_session(self):
        for group in self.get_groups():
            players = group.get_players()
            players.reverse()
            group.set_players(players)
```


---

# oTree Concepts \#2 - Multiplayer Games
## Group matching - Shuffling during the session

-   If your shuffling logic needs to depend
    on something that happens after the session starts, you should do the
    shuffling in a wait page instead of in `creating_session`
-   For example, let’s say you want to randomize groups in round 2 only if a
    certain result happened in round 1. You need to make a WaitPage with
    wait_for_all_groups=True and put the shuffling code in
    after_all_players_arrive:

```python
class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        if some_condition:
            self.subsession.group_randomly()
```


---

# oTree Concepts \#2 - Multiplayer Games
## Group matching - Shuffling during the session

-   You should also use is_displayed() so that this method
    only executes once. For example:

```python
class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        # [...shuffle groups for round 1]
        subsessions = self.subsession.in_rounds(
            2, Constants.num_rounds)
        for subsession in subsessions:
            subsession.group_like_round(1)

    def is_displayed(self):
        return self.round_number == 1
```


---

# oTree Concepts \#2 - Wait pages

-   Wait pages are necessary when one player needs to wait for others to take
    some action before they can proceed.
-   If you have a WaitPage in your sequence of pages, then oTree waits until
    all players in the group have arrived at that point in the sequence,
    and then all players are allowed to proceed.

```python
class NormalWaitPage(WaitPage):
    pass
```

\centerline{\includegraphics[height=100px]{imgs/waiting.png}}

---

# oTree Concepts \#2 - Wait pages

-   If your subsession has multiple groups playing simultaneously, and you
    would like a wait page that waits for all groups (i.e. all players in the
    subsession), you can set the **`attribute wait_for_all_groups = True`** on
    the wait page, e.g.:

```python
class AllGroupsWaitPage(WaitPage):
    wait_for_all_groups = True
```

---

# oTree Concepts \#2 - Wait pages
## Methods - **`after_all_players_arrive()`**

-   Any code you define here will be executed once all players have arrived at
    the wait page.

    For example, this method can determine the winner and set each player’s
    payoff.

```python
class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()
```

## WARNING

-   you can’t reference **`self.player`** inside **`after_all_players_arrive`**,
    because the code is executed once for the entire group, not for each individual
    player.
-   However, you can use **`self.player`** in a wait page’s **`is_displayed`**.

---

# oTree Concepts \#2 - Wait pages
## Methods - **`is_displayed()`**

-   Works the same way as with regular pages. If this returns **`False`** then
    the player skips the wait page.
-   If some or all players in the group skip the wait page, then
    **`after_all_players_arrive()`** may not be run.

\centerline{\includegraphics[height=140px]{imgs/displayed.png}}

---

# oTree Concepts \#2 - Wait pages
## Methods - **`group_by_arrival_time`**

-   If you set **`group_by_arrival_time = True`** on a `WaitPage`, players
    will be grouped in the order they arrive at that wait page:

```python
class MyWaitPage(WaitPage):
    group_by_arrival_time = True

```

For example, if **`players_per_group = 2`**, the first 2 players to arrive at
the wait page will be grouped together, then the next 2 players, and so on.

This is useful in sessions where some participants might drop out in something like
consent pages.

---

# oTree Concepts \#2 - Wait pages
## Methods - **`group_by_arrival_time`**

If a game has multiple rounds, you may want to only group by arrival time in round 1:

```python
class MyWaitPage(WaitPage):
    group_by_arrival_time = True

    def is_displayed(self):
        return self.round_number == 1
```

If you do this, then subsequent rounds will keep the same group structure as
round 1. Otherwise, players will be re-grouped by their arrival time in each
round.

---

# oTree Concepts \#2 - Wait pages
## Methods - **`group_by_arrival_time`**

### Notes:

-   **`id_in_group`** is not necessarily assigned in the order players arrived at the page.
-   **`group_by_arrival_time`** can only be used if the wait page is the first
    page in **`page_sequence`**
-   If you use **`is_displayed`** on a page with **`group_by_arrival_time`**,
    it should only be based on the round number. **Don’t use** `is_displayed`
    to show the page to some players but not others.
-   If you need further control on arranging players into groups, use
    **`get_players_for_group().`**

---

# oTree Concepts \#2 - Wait pages
## Methods - **`get_players_for_group()`**

-   If you’re using **`group_by_arrival_time`** and want more control over which players
    are assigned together, you can use **`get_players_for_group()`**.
-   Let’s say that in addition to grouping by arrival time, you need each group
    group to consist of 1 man and 1 woman (or 2 “A” players and 2 “B” players, etc).
-   If you define a method called **`get_players_for_group`**, it will get called
    whenever a new player reaches the wait page.
-   The method’s argument is the list of players who are waiting to be
    grouped (in no particular order).
-   If you select some of these players and return them as a list, those
    players will be assigned to a group, and move forward.
-   If you don’t return anything, then no grouping occurs.

---

# oTree Concepts \#2 - Wait pages
## Methods - **`get_players_for_group()`**

- Here’s an example where each group has 2 A and B players.

```python
class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True

    def get_players_for_group(self, waiting_players):
        a_players = [p for p in waiting_players if
                     p.participant.vars['type'] == 'A']
        b_players = [p for p in waiting_players if
                     p.participant.vars['type'] == 'B']
        if len(a_players) >= 2 and len(b_players) >= 2:
            return [a_players[0], a_players[1],
                    b_players[0], b_players[1]]

    def is_displayed(self):
        return self.round_number == 1
```

---

# oTree Concepts \#2 - Wait pages
## Methods - Customizing the wait page’s appearance

-   You can customize the text that appears on a wait page by setting the
    **`title_text`** and **`body_text`**:

```python
class MyWaitPage(WaitPage):
    title_text = "Custom title text"
    body_text = "Custom body text"
```

---

# oTree Concepts \#2 - Wait pages
## Methods - Customizing the wait page’s appearance

-   You can also make a custom wait page template. For example,
    save this to **`my_app/templates/my_app/MyWaitPage.html`**:

```javascript
{% extends 'otree/WaitPage.html' %}
{% load staticfiles otree %}
{% block title %}{{ title_text }}{% endblock %}
{% block content %}
    {{ body_text }}
    My custom content here.
{% endblock %}
```

Then tell your wait page to use this template:

```python
class MyWaitPage(WaitPage):
    template_name = 'my_app/MyWaitPage.html'
```

---

# oTree Concepts \#2 - Apps & rounds

## Apps

-   In oTree (and Django), an app is a folder containing Python and HTML code.
-   A session is basically a sequence of apps that are played one after the other.

## Creating an app

Enter:

```bash
$ otree startapp your_app_name
```

-   This will create a new app folder based on a oTree template, with most of the
    structure already set up for you.

---

# oTree Concepts \#2 - Apps & rounds
## Apps - Combining apps

-   In your **`SESSION_CONFIGS`**, you can combine apps by setting
    'app_sequence'.
-   assuming you have created apps named my_app_1 and my_app_2):

```python
SESSION_CONFIGS = [{
    'name': 'my_session_config',
    'display_name': 'My Session Config',
    'num_demo_participants': 2,
    'app_sequence': ['my_app_1', 'my_app_2'],
}]
```

---

# oTree Concepts \#2 - Apps & rounds
## Rounds

-   You can make a game run for multiple rounds by setting
    **`Constants.num_rounds`** in **`models.py`**.
-   For example, if your session config’s app_sequence is
    **`['app1', 'app2'`**], where:
    -   **app1** has **`num_rounds = 3`**
    -   and **app2** has **`num_rounds = 1`**, then your sessions will contain
        4 subsessions.

        1. app1 Round1
        2. app1 Round2
        3. app1 Round3
        4. app2 Round1

---

# oTree Concepts \#2 - Apps & rounds
## Rounds - Round numbers

-   You can get the current round number with **`self.round_number`**
    (this attribute is present on subsession, group, player, and page **objects**).
-   Round numbers start from 1.

\centerline{\includegraphics[height=150px]{imgs/round.png}}

---

# oTree Concepts \#2 - Apps & rounds
## Rounds - Passing data between rounds or apps

-   Each round has separate Subsession, Group, and Player objects.
-   For example, let’s say you set **`self.player.my_field = True`** in **round 1**.
    In round 2, if you try to access **`self.player.my_field`**, you will find its
    value is **`None`**,
-   This is because the Player objects in **round 1** are separate from Player
    objects in **round 2**.

---

# oTree Concepts \#2 - Apps & rounds
## Rounds - **`in_rounds, in_previous_rounds, in_round`** etc.

-   Player, group, and subsession objects have the following methods, which work
    similarly:

    -   **`in_previous_rounds()`** return a list
        of players representing the same participant in previous rounds of the same app
    -   **`in_all_rounds()`** like `in_previous_rounds` but includes the current round’s player
- For example, if you wanted to calculate a participant’s payoff for all
previous rounds of a game, plus the current one:

```python
cumulative_payoff = sum([p.payoff for p in
                        self.player.in_all_rounds()])
```

---

# oTree Concepts \#2 - Apps & rounds
## Rounds - **`in_rounds, in_previous_rounds, in_round`** etc.

-   **`in_rounds(m, n)`** returns a list of players representing the same participant from rounds m to n.
-   **`in_round(n)`**  returns just the player in round m.
-   For example, to get the player’s payoff in the previous round, you would
    do:

```python
self.player.in_round(self.round_number - 1).payoff
```

---

# oTree Concepts \#2 - Apps & rounds
## Rounds - **`in_rounds, in_previous_rounds, in_round`** etc.

-   Similarly, **subsession** objects have methods **`in_previous_rounds()`**,
    **`in_all_rounds(), in_rounds(m,n)`** and **`in_round(m)`** that work the same way.
-   **Group** objects also have methods but note that if you
    **re-shuffle** groups between rounds, then these methods **may not return**
    **anything meaningful.**

---

# oTree Concepts \#2 - Apps & rounds
## Rounds - **`participant.vars`**

-   **`in_all_rounds()`** only is useful when you need to access data from a previous
    round of the same app.
-   If you want to pass data between different apps,
    you should store this data on the participant, which persists across apps
-   **`participant.vars`**: is a dictionary that can store any data.
    For example, you can set an attribute like this:

```python
self.participant.vars['name'] = 'John'
```

---

# oTree Concepts \#2 - Apps & rounds
## Apps - Passing data between apps

-   The current participant can be accessed from a **`Page`** or **`Player`**:

```python
# in views.py
class MyPage(Page):
    def before_next_page(self):
        self.participant.vars['foo'] = 1

# in models.py
class Player(BasePlayer):
    def some_method(self):
        self.participant.vars['foo'] = 1
```

---

# oTree Concepts \#2 - Apps & rounds
## Apps - **`session.vars`**

-   For global variables that are the same for all participants in the
    session, you can use **`self.session.vars`**.
-   This is a dictionary just  like participant.vars. The difference is that if
    you set a variable in self.session.vars, it will apply to all participants
    in the session, not just one.
-   As described here, the session object can be accessed from a Page object or
    any of the models (Player, Group, Subsession, etc.).

\centerline{\includegraphics[height=90px]{imgs/session.png}}

---

# oTree Concepts \#2 - Treatments

-   To assign participants to different treatment groups, you can put the
    code in the subsession’s **`creating_session`** method
-   For example, if you want some participants to be in a **“blue”** treatment
    group and others to be in a **“red”** treatment group, first define a
    color field on the Player model:

```python
class Player(BasePlayer):
    color = models.CharField()
```

-   Then you can assign to this field randomly:


```python
class Subsession(BaseSubsession):

  def creating_session(self):
    for player in self.get_players():
      player.color = random.choice(['blue', 'red'])

```

---

# oTree Concepts \#2 - Treatments

-   If your game has multiple rounds, the above code gets executed for
    each round.
-   So if you want to ensure that participants are assigned to the same
    treatment group each round, you should set the property at the
    participant level, which persists across subsessions, and only set
    it in the first round:

```python
class Subsession(BaseSubsession):
  def creating_session(self):
    if self.round_number == 1:
      for p in self.get_players():
        color = random.choice(['blue', 'red'])
        p.participant.vars['color'] = color
```

- Then elsewhere in your code, you can access the participant’s color
  with **`self.participant.vars['color']`**.


---

# oTree Concepts \#2 - Treatments

-   The above code makes a random drawing independently for each player,
    so you may end up with an imbalance between “blue” and “red”.
-   To solve this, you can use itertools.cycle, which alternates. :

```python
import itertools

class Subsession(BaseSubsession):

    def creating_session(self):
        colors = itertools.cycle(['blue', 'red'])
        for p in self.get_players():
            p.color = next(colors)
```

---

# oTree Concepts \#2 - Treatments
## Choosing which treatment to play

-   In the above example, players got randomized to treatments.
-   But it is often useful to choose explicitly which treatment to play.
-   You can create 2 session configs in settings.py that have the same
    keys to session config dictionary, except the treatment key:

```python
SESSION_CONFIGS = [
    {'name':'my_game_blue',
     # other arguments...
     'treatment':'blue'},
    {'name':'my_game_red',
     # other arguments...
     'treatment':'red'}
]
```

---

# oTree Concepts \#2 - Treatments
## Choosing which treatment to play

-   Then in the **`creating_session`** method, you can check which of the 2
    session configs it is:

```python
def creating_session(self):
    for p in self.get_players():
        if 'treatment' in self.session.config:
            # demo mode
            p.color = self.session.config['treatment']
        else:
            # live experiment mode
            p.color = random.choice(['blue', 'red'])
```

-   Then, when someone visits your demo page, they will see the **“red”** and
    **“blue”** treatment.
-   If the demo argument is not passed, the color is randomized.

---

# oTree Concepts \#2 - Rooms

oTree lets you configure “rooms”, which provide:

-   Persistent links that you can assign to participants or workstations.
-   A “waiting room” that lets you see how many people are waiting to start a
    session.
-   Short links that are easy for participants to type

\centerline{\includegraphics[height=150px]{imgs/room-combined.png}}

---

# oTree Concepts \#2 - Rooms
## Creating rooms

-   You can create multiple rooms – say, for for different classes you teach,
    or different labs you manage.
-   To create a room, add to your **`settings.py`** a setting **`ROOMS`**
    (and, optionally, **`ROOM_DEFAULTS`**).
-   **`ROOMS`** should be a list of dictionaries; each dictionary defines
    the configuration of a room.

```python
ROOM_DEFAULTS = {}

ROOMS = [
    {'name': 'econ101',
     'display_name': 'Econ 101 class',
     'participant_label_file': 'econ101.txt'
    },
    {'name': 'econ_lab',
     'display_name': 'Experimental Economics Lab'}]
```

---

# oTree Concepts \#2 - Rooms
## Creating rooms - Available properties

-   **`name`** and **`display_name`** (required)
    The internal name and display name, respectively.
-   **`participant_label_file`** (optional)
    A path to a text file with the “guest list” for this room.
    Path can be either absolute or relative to the project’s root directory.
    The file should contain one participant label per line. For example:

```
PC_1
PC_2
PC_3
...
```

If you omit **`participant_label_file`**, then anyone can join as long as
they know the room-wide URL.

---

# oTree Concepts \#2 - Rooms
## Creating rooms - Available properties:

-   **`use_secure_urls`** (optional)
    This setting provides an extra layer of security on top of the
    participant_label_file. For example, if you are not using secure URLs,
    your start URLs would look something like this:

```
http://host/room/econ101/?participant_label=Student1
http://host/room/econ101/?participant_label=Student2
```

The issue is that if Student1 is mischievous, he might change his
URL’s participant_label from “Student1” to “Student2”, so that he can
impersonate playing as Student2.

However, if you set **`'use_secure_urls': True`**, oTree will add a
unique secret key to each participant’s URLs, like this:

```
...?participant_label=Student1&hash=29cd655f
...?participant_label=Student1&hash=46d9f31d
```

---

# oTree Concepts \#2 - Rooms
## Using rooms

In the admin interface, click “Rooms” in the header bar, and click the
room you created. Scroll down to the section with the participant URLs.

\centerline{\includegraphics[height=150px]{imgs/room.png}}

---

# oTree Concepts \#2 - Rooms
## Using rooms - If you have a **`participant_label_file`**

-   Have each participant open the URLs. Then, in the room’s admin page,
    check how many people are present, and create a session for that
    number of people.
-   You can either use the room-wide URL, or the participant-specific URLs.
-   The participant-specific URLs already contain the participant label, so
    as soon as they are clicked, the participant will go straight to the
    waiting page. For example one participant can open URL
    **`http://.../?participant_label=Student1`**

---

# oTree Concepts \#2 - Rooms
## Using rooms - If you have a **`participant_label_file`**

-   Or, you can give both students the room-wide URL, which does not contain
    participant_label: **`http://127.0.0.1:8000/room/econ101/`**
-   and when a user clicks the room-wide URL, they are prompted to enter
    their participant label:

\centerline{\includegraphics[height=120px]{imgs/room-combined.png}}


---

# oTree Concepts \#2 - Rooms
## Using rooms - If you don’t have a **`participant_label_file`**

-   Starting is simple; just have each participant open the room-wide URL.
    Have each participant open the URLs.
-   Then, in the room’s admin page, check how many people are present, and
    create a session for that number of people.
-   Although this option is simple, it is less reliable than using
    participant labels, because someone could easily play twice by opening
    the URL in 2 browser tabs.

---

# oTree Concepts \#2 - Rooms
## Using rooms - Reusing for multiple sessions

-   Room URLs are designed to be reused across sessions.
-   In a lab, you can set the room URL (either room-wide or
    participant-specific) as the browser’s home page.
-   In classroom experiments, you can give each student the room-wide
    URL they can use repeatedly during the semester.


---

# oTree Concepts \#2 - Money & Payoffs
## Money

-   In many experiments, participants play for currency: either real money, or
    points.
-   oTree supports both
-   You can switch from points to real money by
    setting **`USE_POINTS = False`** in **`settings.py`**.

\centerline{\includegraphics[height=130px]{imgs/money.png}}

---

# oTree Concepts \#2 - Money & Payoffs
## Money

-   If you have a value that represents an amount of currency (either points
    or dollars, etc), you should mark it with **`c()`**, e.g.

```python
c(1) + c(0.2) == c(1.2)
```

-   The advantage is that when it’s displayed to users, it will automatically
    formatted as **$1.20** or **1,20 €**, etc., depending on your
    **`REAL_WORLD_CURRENCY_CODE`** and **`LANGUAGE_CODE`** settings.
-   Money amounts are displayed with 2 decimal places by default; you can
    change this with the setting **`REAL_WORLD_CURRENCY_DECIMAL_PLACES`**.
    (If you change the number of decimal places, you must resetdb.)

---

# oTree Concepts \#2 - Money & Payoffs

-   If a model field is a currency amount, you should define it as a
    **`CurrencyField`**.

```python
class Player(BasePlayer):
    random_bonus = models.CurrencyField()
    def some_method(self):
        self.random_bonus = c(random.randint(1, 10))
```

-   **NOTE:** instead of using Python’s built-in range function, you should
    use oTree’s **`currency_range`**

```python
class Player(BasePlayer):
  contribution = models.CurrencyField(
    choices=currency_range(c(0), c(0.10), c(0.02)))
    # [$0.00, $0.02, $0.04, $0.06, $0.08, $0.10]
```

-   **`currency_range`** takes 3 arguments (start, stop, step), just like range.
    However, unlike range(), the returned list includes the stop value as
    shown above.

---

# oTree Concepts \#2 - Money & Payoffs
## Money

-   In templates use the |c filter. For example, **`{{ 20|c }}`** displays as
    **20 points**.

\centerline{\includegraphics[height=150px]{imgs/money2.png}}

---

# oTree Concepts \#2 - Money & Payoffs
## payoffs

-   Each player has **` payoff`** field, which is a **`CurrencyField`**. If your
    player makes money, you should store it in this field.
-   **`self.participant.payoff`** automatically stores the sum of payoffs from all
    subsessions.
-   You can modify self.participant.payoff directly, e.g. to round the final
    payoff to a whole number.

---

# oTree Concepts \#2 - Money & Payoffs
## payoffs

- At the end of the experiment, a participant’s total profit can be accessed by

```python
self.participant.payoff_plus_participation_fee()
```

-   it is calculated by  converting **`self.participant.payoff`** to
    real-world currency (if **`USE_POINTS`** is **`True`**),
    and then adding **`self.session.config['participation_fee']`**.

---

# oTree Concepts \#2 - Money & Payoffs
## payoffs - Points (i.e. “experimental currency”)

-   Sometimes it is preferable for players to play games for points or
    “experimental currency units”, which are converted to real money at the
    end of the session.
-   You can set **`USE_POINTS = True`** in **`settings.py`**, and then in-game
    currency amounts will be expressed in points rather than dollars or euros,
    etc.

>   c(10) is displayed as 10 points.

-   To change the exchange rate to real money, go to **`settings.py`** and set
    **`real_world_currency_per_point`** in the session config.
-   For example, if you pay the user 2 cents per point, you would set

```python
'real_world_currency_per_point': 0.02
```

---

# oTree Concepts \#2 - Money & Payoffs
## payoffs - Points (i.e. “experimental currency”)

-   Points are integers by default.
-   You can change this by setting **`POINTS_DECIMAL_PLACES = 2`**, or
    whatever number of decimal places you desire.
-   If you change the number of decimal places, you must resetdb.


---

# oTree Concepts \#2 - Money & Payoffs
## payoffs - Points (i.e. “experimental currency”)

-   If you switch your language setting to one of oTree’s supported languages,
    the name “points” is automatically translated, e.g. “puntos” in Spanish.
-   To further customize the name “points” to something else like “tokens” or
    “credits”, set **`POINTS_CUSTOM_NAME`**, e.g.

```python
POINTS_CUSTOM_NAME = 'tokens
```


---

# oTree Concepts \#2 - Money & Payoffs
## payoffs - Points (i.e. “experimental currency”)

-   You can convert a points amount to money using the method:

```python
>>> c(10).to_real_world_currency(self.session)
$0.20
```

-   It requires self.session to be passed, because different sessions can have
    different conversion rates).

----------------------------------------------------------------------

# References

-   http://otree.readthedocs.io/en/latest/
-   http://blog.easylearning.guru/implementing-mtv-model-in-python-django/
-   https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
-   https://en.wikipedia.org/wiki/Django_(web_framework)
-   https://www.quora.com/What-is-a-Full-Stack-Web-framework
