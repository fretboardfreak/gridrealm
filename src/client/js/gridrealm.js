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
import {change_multipanel_view} from './multi_panel.js';
import {URI} from './api.js';

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

// Browser Events

/* On DOM Ready Load the client. */
$(document).ready(function(){load_client();});

/* Resize the game panels when browser window is resized. */
$(window).resize(resize_panels);

/* Redirect page to logout API when logout button clicked. */
$('#logout-lnk').click(function(){location.href=URI.logout;});

/* Change multi_panel view when tab icons are clicked */
$('#mp-navigation-lnk').children('img').click(function(){
  change_multipanel_view('navigation');
});
$('#mp-inventory-lnk').children('img').click(function(){
  change_multipanel_view('inventory');
});
$('#mp-skill-lnk').children('img').click(function(){
  change_multipanel_view('skill');
});
$('#mp-quest-lnk').children('img').click(function(){
  change_multipanel_view('quest');
});
$('#mp-social-lnk').children('img').click(function(){
  change_multipanel_view('social');
});
