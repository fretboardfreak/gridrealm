/*
 * Grid Realm Client - Core
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */

import * as auth from "./auth.js";
import * as resize from "./resize.js";
import { get_cookie } from "./util.js";


/* On DOM Ready*/
$(document).ready(function(){
  if (auth.is_logged_in()) {
    console.log("Logged in as: " + get_cookie('username'));
    $("body").removeClass("tiled_bg")
    auth.login();
  } else {
    console.log('Not logged in.');
    $("body").addClass("tiled_bg")
  }
});

/* Resize the game panels when browser window is resized. */
$(window).resize(resize.resize_panels);
