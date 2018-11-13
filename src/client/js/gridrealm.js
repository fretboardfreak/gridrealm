/*
 * Grid Realm Client - Core
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */

import * as auth from './auth.js';
import {get_cookie} from './util.js';
import {resize_panels} from './resize.js';
import {load_action_panel} from './action_panel.js';
import {load_chat_panel} from './chat_panel.js';
import {load_multi_panel} from './multi_panel.js';

export function load_client() {
  if (auth.is_logged_in()) {
    resize_panels();
    load_action_panel();
    load_multi_panel();
    load_chat_panel();
    $('#logout-lnk').html('Logout: ' + get_cookie('username'));
    $('body').removeClass('tiled_bg');
    console.log('Logged in as: ' + get_cookie('username'));
  }
  else { /* not logged in */
    console.log('Not Logged In. Doing nothing.');
    $('body').addClass('tiled_bg');
  }
}

/* On DOM Ready Load the client. */
$(document).ready(function(){load_client();});

/* Resize the game panels when browser window is resized. */
$(window).resize(resize_panels);
