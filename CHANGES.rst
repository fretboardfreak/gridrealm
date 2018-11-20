====================
GridRealm Change Log
====================

- 0.0: Getting Started - 181015

  - begin writing documentation on the project "src/docs"

  - begin writing client webpage

  - begin game api server

- 0.1: Walking Skeleton - 181120

  - implement build system using makefile

  - use babel and rollup.js to transpile ES6 javascript into a browser
    compatible library.

  - use node-sass, and autoprefixer to compile customized bootstrap stylesheets

  - include feature to compile PlantUML diagrams for the documentation

  - add static routes to serve static files such as javascript, stylesheets and
    asset files.

  - add randomImage, randomActionImage, randomInventoryImage API endpoints to
    help fill in the client with stand-in content.

  - add ini config file support for gridrealm.

  - add version api endpoint.

  - add front end scripts for CLI and uWSGI use.

  - implement server sent events and print them to the chat panel.

  - implement user login/logout events.

  - add sqlite database back end for persistent storage.

  - add Map Tiles with text based representations.

  - add location and move endpoints to enable the client to see the map and
    move around it.

  - use Postman to test the API without the client.

  - add tabs to the multipanel in the client.

  - use gunicorn to run the game engine locally
