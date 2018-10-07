/*
 * Grid Realm Core Client Library
 * documentation: http://fretboardfreak.com/gridrealm/
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 * Date: 2018-10-04-11:00
 */

/* -------------------------------------------------------------------- */
/* Authentication Code */

/* TODO: The whole authentication process needs to be implemented. This is just
 * a stand in to start getting the client behaviour correct.
 */
var LOGGED_IN = false;

/* TODO: use this function to retrieve the authenticated session token if the
 * user is logged in. Return false otherwise.
 */
function is_logged_in() {
  return LOGGED_IN;
}

function login() {
  LOGGED_IN = true;
  alert("Loggin In...");
  init_panels();
  $("#login-link").text('Logout');
  $("#create-account-link").addClass("hidden");
}

function logout() {
  LOGGED_IN = false;
  alert("Logging Out...");
  init_panels();
  $("#login-link").text("Login");
  $("#create-account-link").removeClass("hidden");
}

function toggle_login_state() {
  if (is_logged_in()) {
    logout();
  }
  else {
    login();
  }
}

function create_account() {
  alert("Creating an account...");
}

/* -------------------------------------------------------------------- */

function init_panels() {
  if (is_logged_in()) {
    console.log("disabling nologin content")
    $("#nologin").addClass('hidden');
    console.log("initializing action panel");
    $("#action-panel").removeClass('hidden');
    console.log("initializing multi panel");
    $("#multi-panel").removeClass('hidden');
    console.log("initializing chat panel");
    $("#chat-panel").removeClass('hidden');
  }
  else { /* not logged in */
    console.log("initializing nologin content");
    $("#nologin").removeClass('hidden');
    console.log("disabling action panel");
    $("#action-panel").addClass('hidden');
    console.log("disabling multi panel");
    $("#multi-panel").addClass('hidden');
    console.log("disabling chat panel");
    $("#chat-panel").addClass('hidden');
  }
}


/* On DOM Ready*/
$(document).ready(function(){
  console.log("initializing page.");
  init_panels();
});
