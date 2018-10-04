=====================
GR: Development Stack
=====================

:author: Curtis Sand <curtissand@gmail.com>,
         Dennison Gaetz <djgaetz@gmail.com>
:lastedit: 181003-1800

- `Home <http://www.fretboardfreak.com/gridrealm>`_
- `Back to Development <http://www.fretboardfreak.com/gridrealm/dev>`_
- `Source <http://www.fretboardfreak.com/gridrealm/dev/devstack.rst>`_

----

The plan is to create a modular framework of systems designed to build a
functional multiplayer online gaming system. ::

    +--------+
    | Client |
    +--------+______________
      |                     \
    +------------+        +--------------+
    | API Server |        | Asset Server |
    +------------+        +--------------+
      |
    +-------------+
    | Game Engine |
    +-------------+
      |
    +--------------------+
    | Persistence Engine |
    +--------------------+


Client
------

This is a webpage using javascript and HTML5 to send REST API requests to the
`API Server`_, load asset images from the `Asset Server`_ then display the game
UI and interact with the user.

To display the game itself the plan is to use the HTML5 canvas to load game
asset images to create the UI.

TODO: need to determine how to register clicks on areas within the canvas!

API Server
----------

`API Server Page <http://fretboardfreak.com/gridrealm/dev/api_server.html>`_

The API Server is a web connected server that talks a request language called
RESTfull. (I think REST will suit our needs for now.) The purpose of the API
Server is to bridge the gap between the `Client`_ and the `Game Engine`_.

For example a type of request the client might send is "For player X with
encrypted session ID Y, please send me details about the map". The API Server
then verifies the login and session IDs with the `Game Engine`_ and calls a
routine to lookup and send back info on the map assets that the client needs to
load from the `Asset Server`_ in order to respond to the user.

The API Server will be written in Python 3 using `Flask
<http://flask.pocoo.org>`_ to perform the RESTfull communication.

Asset Server
------------

`API Server Page <http://fretboardfreak.com/gridrealm/dev/asset_server.html>`_

The Asset Server will be a simple NGINX webserver containing the game assets.
The Asset Server will serve up the assets to the client pages as described by
what the `API Server`_ tells the client to load.

TODO: determine how to include authentication here to prevent the Asset Server
from being accessed outside the game's intended use.

Game Engine
-----------

`Game Engine Page <http://fretboardfreak.com/gridrealm/dev/game_engine.html>`_

The Game Engine is where all the magic happens. Random events in the world,
combat calculations, and everything else that happens in the game is controlled
and mediated by the Game Engine.

Persistence Engine
------------------

`Persistence Engine Page
<http://fretboardfreak.com/gridrealm/dev/persistence_engine.html>`_

The Persistence Engine is a fancy -- possibly overblown -- name for a layer
that saves and loads the information about the game's configuration and status
to disk. This includes all the info about a player and their inventory as well
as all the data about the entire world or more.

----

- `Home <http://www.fretboardfreak.com/gridrealm>`_
- `Back to Development <http://www.fretboardfreak.com/gridrealm/dev>`_
- `Source <http://www.fretboardfreak.com/gridrealm/dev/devstack.rst>`_
