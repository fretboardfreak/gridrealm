/*
 * Grid Realm Client - Auth Library
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */

import {resize_panels} from "./resize.js";
import {load_action_panel} from "./action_panel.js";
import {load_chat_panel} from "./chat_panel.js";
import {load_multi_panel} from "./multi_panel.js";
import {API} from "./api.js";

/* TODO: The whole authentication process needs to be implemented. This is just
 * a stand in to start getting the client behaviour correct.
 */
var LOGGED_IN = false;

/* TODO: use this function to retrieve the authenticated session token if the
 * user is logged in. Return false otherwise.
 */
export function is_logged_in() {
  return LOGGED_IN;
}

function login() {
  LOGGED_IN = true;
  init_panels();
  load_action_panel();
  load_multi_panel();
  load_chat_panel();
}

function logout() {
  LOGGED_IN = false;
  init_panels();
}

export function toggle_login_state() {
  if (is_logged_in()) {
    logout();
  }
  else {
    login();
  }
}

export function create_account() {
  API.get_api_version(function (response) {
    alert("Creating an account using API version: " + response.version);
  });
};

export function init_panels() {
  if (is_logged_in()) {
    console.log("disabling nologin content");
    $("#nologin").hide();
    console.log("enabling loggedin content");
    $("#loggedin").show();
    resize_panels();
  }
  else { /* not logged in */
    console.log("initializing nologin content");
    $("#nologin").show();
    console.log("disabling loggedin content");
    $("#loggedin").hide();
  }
}
