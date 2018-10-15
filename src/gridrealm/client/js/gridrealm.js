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
  init_panels();
  load_action_panel();
  load_multi_panel();
  load_chat_panel();
}

function logout() {
  LOGGED_IN = false;
  init_panels();
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
  get_api_version(function (response) {
    alert("Creating an account using API version: " + response.version);
  });
};

/* /Authentication Code */
/* -------------------------------------------------------------------- */
/* API Requests */

var api = {};
api.version = "api/version";
api.randomImage = "api/randomImage";

function get_random_image(success) {
  $.ajax({
    url: api.randomImage,
    data: '',
    type: 'GET',
    success: success,
    error: function (error) {console.log(error);}
  });
};

function get_api_version(success) {
  $.ajax({
    url: api.version,
    data: '',
    type: 'GET',
    success: success,
    error: function (error) {console.log(error);}
  });
};

/* /API Requests */
/* -------------------------------------------------------------------- */
/* General Code */

function resize_panels() {
  var window_height = $(window).height();
  $("#action-panel").height(window_height * 0.6);
  $("#multi-panel").height(window_height * 0.9);
  $("#chat-panel").height(window_height * 0.3);

  var window_width = $(window).width();
  $("#action-panel").width(window_width * 0.6);
  $("#multi-panel").width(window_width * 0.3);
  $("#chat-panel").width(window_width * 0.6);

  resize_multipanel_content();
  update_size_record();
}

function resize_multipanel_content() {
  var height = $("#multi-panel").height();
  var content_height = height * 0.8;
  var nav_height = height * 0.2;
  $("#mp-content").height(content_height);
  $("#mp-nav-bar").height(nav_height);


  var width = $("#multi-panel").width();
  $("#mp-content").width(width);
  $("#mp-nav-bar").width(width);

  $("#mp-content").children("div").height(content_height);

  var tab_icon_width = width * 0.14;
  ($("#mp-nav-bar").children('nav').children("span")
      ).children("img").width(tab_icon_width);
}

function init_panels() {
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

function build_image_tag(source, height) {
  if (typeof height === 'undefined') height = "auto";
  return ("<img class=\"img-fluid mx-auto\" style\"object-fit:contain;" +
          " height: " + height + ";\" src=\"" + source + "\"/>");
}

function add_random_image(tag, height) {
  if (typeof height === 'undefined') height = "auto";
  get_random_image(function (response){
    tag.html(build_image_tag(response.randomImage, height));
  });
}

function change_multipanel_view(panel) {
  var full_panel_name = "#mp-" + panel;
  // disable all tabs first
  $("#mp-content").children().hide();
  $("#mp-nav-bar").children('nav').children('span').removeClass('active');
  // then enable the one we want to see
  $(full_panel_name + "-lnk").addClass('active');
  $(full_panel_name).show();
}

function load_action_panel() {
  add_random_image($("#ap-image"));
}

function load_multi_panel() {
  change_multipanel_view('navigation'); // default view is nav
  $("#mp-content").children("div").each(function () {
    add_random_image($(this));
  });
}

function load_chat_panel() {
  add_random_image($("#chat-panel"));
}

/* /General Code */
/* -------------------------------------------------------------------- */
/* Debug Code */

function add_size(panel_id) {
  return (panel_id + ": " + $(panel_id).innerWidth() + "x" +
          $(panel_id).innerHeight());
}

function update_size_record() {
  $("#size-record").text(add_size("#action-panel") + " | " +
                         add_size("#multi-panel") + " | " +
                         add_size("#chat-panel"));
}

/* /Debug Code */
/* -------------------------------------------------------------------- */
/* Events */

/* On DOM Ready*/
$(document).ready(function(){
  console.log("initializing page.");
  init_panels();
  resize_panels();
});

/* Resize the game panels when browser window is resized. */
$(window).resize(resize_panels);
