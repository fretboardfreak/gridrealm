/*
 * Grid Realm Client - Core
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */

import * as auth from "./auth.js";
import * as resize from "./resize.js";


/* On DOM Ready*/
$(document).ready(function(){
  console.log("initializing page.");
  auth.init_panels();
  resize.resize_panels();
});

/* Resize the game panels when browser window is resized. */
$(window).resize(resize.resize_panels);
