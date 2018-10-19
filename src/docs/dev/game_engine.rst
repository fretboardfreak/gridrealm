===============
GR: Game Engine
===============

:author: Curtis Sand <curtissand@gmail.com>,
         Dennison Gaetz <djgaetz@gmail.com>
:lastedit: 181003-2300

- `Source <game_engine.rst>`_
- `Home <../index.html>`_
- `Back to Development <index.html>`_

----

Engine Class Models
-------------------

TBD

Database ER Design
------------------

I am working on the design using the PlantUML system. At the moment I'm using the `online tool <https://www.planttext.com/>`_.

.. note:: TODO: find the link to embed this plantUML in the built docs.

::
    @startuml

    class Player {
    # username varchar
    + x_location int : FK World
    + y_location int : FK World
    }

    class World {
      # x_location int
      # y_location int
      + bg_asset varchar
    }

    World::x_location --> Player::x_location : FK
    World::y_location --> Player::y_location : FK

    @enduml

.. note:: In the uml above a "class" represents a table, and the items within the class represent the columns. The columns with the # are the primary keys. Foreign keys are marked with an FK and with a relationship line.

----

- `Home <../index.html>`_
- `Back to Development <index.html>`_
- `Source <game_engine.rst>`_
