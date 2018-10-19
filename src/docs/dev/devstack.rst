=====================
GR: Development Stack
=====================

:author: Curtis Sand <curtissand@gmail.com>,
         Dennison Gaetz <djgaetz@gmail.com>
:lastedit: 181008-1600

- `Source <devstack.rst>`_
- `Home <../index.html>`_
- `Back to Development <index.html>`_

----

The plan is to create a modular framework of systems designed to build a
functional multiplayer online gaming system. ::

    +--------+
    | Client |
    +--------+
      |
    +---------------------+
    | API Server & Assets |
    +---------------------+
      |
    +-------------+
    | Game Engine |
    +-------------+


Client
------

This is a webpage using javascript and HTML5 to send REST API requests to the
`API Server`_, load asset images, display the game UI and interact with the
user.

To display the game itself the plan is to use HTML5 and javascript/jquery to
load game asset images and create the UI.

API Server
----------

`API Server Page <api_server.html>`_

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

Game Engine
-----------

`Game Engine Page <game_engine.html>`_

The Game Engine is where all the magic happens. Random events in the world,
combat calculations, and everything else that happens in the game is controlled
and mediated by the Game Engine.

The Game Engine will also have a backend layer for persistence. Ideally this
would be a SQL database of some sort.

----

- `Home <../index.html>`_
- `Back to Development <index.html>`_
- `Source <devstack.rst>`_
