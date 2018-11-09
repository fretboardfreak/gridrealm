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

Game World Objects/Behaviors
----------------------------

Action Assets
"""""""""""""

Spawners
^^^^^^^^

- id (database assigned, mostly ignored here in design docs)
- name (unique)
- timing_type
- timing_args

Tool Tier
^^^^^^^^^

Same as rarity set.

Rarity
^^^^^^

To start all resources of the same rarity will have the same required levels
and tool tier.

- common

  - required_levels: None
  - required_tool_tier:

- uncommon

  - required_levels: 5
  - required_tool_tier: common

- rare

  - required_levels: 10
  - required_tool_tier: uncommon

- epic

  - required_levels: 20
  - required_tool_tier: rare

- legendary

  - required_levels: 40
  - required_tool_tier: epic

- godly

  - required_levels: 80
  - required_tool_tier: legendary


Resources
^^^^^^^^^

- id (database assigned, mostly ignored here in design docs)
- name (unique)
- resource_type (hunting/mining/woodcutting)
- required_levels
- required_tools
- rarity (common/uncommon/rare/epic/legendary/godly)
- asset

List of Resources
'''''''''''''''''

(Note: list is::

   RESOURCE_TYPE:
     - NAME
       - required_levels
       - required_tools
       - rarity
       - asset

)




Hunting:

- blueberry

  - required_levels:
  - required_tools:
  - rarity: rare
  - asset: _assets/action/hunting/blueberry.svg

- oleander

  - required_levels:
  - required_tools:
  - rarity: epic
  - asset: _assets/action/hunting/oleander.svg

- redberry

  - required_levels:
  - required_tools:
  - rarity: uncommon
  - asset: _assets/action/hunting/redberry.svg


Mining:

- chromium-large

  - required_levels:
  - required_tools:
  - rarity:
  - asset: _assets/action/mining/chromium-large.svg

- chromium-small

  - required_levels:
  - required_tools:
  - rarity:
  - asset: _assets/action/mining/chromium-small.svg

- coal-large

  - required_levels:
  - required_tools:
  - rarity:
  - asset: _assets/action/mining/coal-large.svg

- coal-small

  - required_levels:
  - required_tools:
  - rarity:
  - asset: _assets/action/mining/coal-small.svg

- copper-large

  - required_levels:
  - required_tools:
  - rarity:
  - asset: _assets/action/mining/copper-large.svg

- copper-small

  - required_levels:
  - required_tools:
  - rarity:
  - asset: _assets/action/mining/copper-small.svg

- gold

  - required_levels:
  - required_tools:
  - rarity:
  - asset: _assets/action/mining/gold.svg

- iron-large

  - required_levels:
  - required_tools:
  - rarity:
  - asset: _assets/action/mining/iron-large.svg

- iron-small

  - required_levels:
  - required_tools:
  - rarity:
  - asset: _assets/action/mining/iron-small.svg

- platinum

  - required_levels:
  - required_tools:
  - rarity:
  - asset: _assets/action/mining/platinum.svg

- silver.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset: _assets/action/mining/silver.svg

- titanium-large.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset: _assets/action/mining/titanium-large.svg

- titanium-small.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset: _assets/action/mining/


Woodcutting:

- aloe.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset:

- cedar-large.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset:

- cedar-small.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset:

- ebony-large.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset:

- ebony-small.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset:

- hawthorne.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset:

- maple-large.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset:

- maple-small.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset:

- nightshade.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset:

- oak-large.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset:

- oak-small.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset:

- pine-large.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset:

- pine-small.svg

  - required_levels:
  - required_tools:
  - rarity:
  - asset:


Engine Class Models
-------------------

TBD

Database ER Design
------------------

I am working on the design using the PlantUML system. At the moment I'm using
the `online tool <https://www.planttext.com/>`_. The image below descripes the
ERD structure of the database.

.. image:: ./database_erd.png
    :target: ./database_erd.puml

----

- `Home <../index.html>`_
- `Back to Development <index.html>`_
- `Source <game_engine.rst>`_
