/*
 * Copyright 2019 Curtis Sand <curtissand@gmail.com>,
 *                Dennison Gaetz <djgaetz@gmail.com>
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Grid Realm Client - Core
 */

import * as auth from './auth.js';
import {get_cookie} from './util.js';
import {resize_panels} from './resize.js';
import {load_action_panel} from './action_panel.js';
import {load_chat_panel} from './chat_panel.js';
import {load_multi_panel} from './multi_panel.js';
import {change_multipanel_view} from './multi_panel.js';
import {load_minimap} from './multi_panel.js';
import {load_nav_buttons} from './multi_panel.js';
import {URI} from './api.js';
import {API} from './api.js';

export function update_client(data) {
  console.log('minimap: ' + data['minimap']);
  load_minimap(data['minimap']);
  load_nav_buttons(data['movement']);
}

export function load_client() {
  if (auth.is_logged_in()) {
    resize_panels();
    load_action_panel();
    load_multi_panel();
    load_chat_panel();
    $('#logout-lnk').html('Logout: ' + get_cookie('username'));
    $('body').removeClass('tiled_bg');
    console.log('Logged in as: ' + get_cookie('username'));

    API.get_location(function (response) {
      console.log(response);
      update_client(response);
    });
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

// Set Movement button events
$('#north-btn').click(function () {
  console.log('Attempting to move North.');
  API.move('north', function (response) {
    console.log('response: ' + response);
    update_client(response);
    console.log('moved');
  });
});
$('#south-btn').click(function () {
  console.log('Attempting to move South.');
  API.move('south', function (response) {
    console.log('response: ' + response);
    update_client(response);
    console.log('moved');
  });
});
$('#east-btn').click(function () {
  console.log('Attempting to move East.');
  API.move('east', function (response) {
    console.log('response: ' + response);
    update_client(response);
    console.log('moved');
  });
});
$('#west-btn').click(function () {
  console.log('Attempting to move West.');
  API.move('west', function (response) {
    console.log('response: ' + response);
    update_client(response);
    console.log('moved');
  });
});
