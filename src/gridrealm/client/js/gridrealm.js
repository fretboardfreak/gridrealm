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
  $("#action-panel").height(window_height * 0.6)
  $("#multi-panel").height(window_height * 0.9)
  $("#chat-panel").height(window_height * 0.3)

  var window_width = $(window).width();
  $("#action-panel").width(window_width * 0.6)
  $("#multi-panel").width(window_width * 0.3)
  $("#chat-panel").width(window_width * 0.6)

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
    console.log("initializing action panel");
    $("#action-panel").show();
    console.log("initializing multi panel");
    $("#multi-panel").show();
    console.log("initializing chat panel");
    $("#chat-panel").show();
    $("#size-record").show();
  }
  else { /* not logged in */
    console.log("initializing nologin content");
    $("#nologin").show();
    console.log("disabling action panel");
    $("#action-panel").hide();
    console.log("disabling multi panel");
    $("#multi-panel").hide();
    console.log("disabling chat panel");
    $("#chat-panel").hide();
    $("#size-record").hide();
  }
}

function get_image_style(width, height) {
  /* Build style string for image tags with width and height properties.
   *     <img style="width=100%;height=100%;"/>
   */
  var style_str = "\"";
  if (width) {
    style_str += "width:" + width + ";";
  }
  else {
    style_str += "width:100%;";
  }
  if (height) {
    style_str += "height:" + height + ";";
  }
  else {
    style_str += "height:100%;";
  }
  style_str += "\"";
  return style_str;
}

function load_action_panel() {
  get_random_image(function (response) {
    var temp_content = "<p>action panel</p><img src=\"" + response.randomImage + "\" style=";
    temp_content += get_image_style() + "/>";
    $("#action-panel").html(temp_content);
    console.log('Added image to action panel');
  });
}

function load_multi_panel() {
  get_random_image(function (response) {
    var temp_content = "<p>multi panel</p><img src=\"" + response.randomImage + "\" style=";
    temp_content += get_image_style() + "/>";
    $("#multi-panel").html(temp_content);
    console.log('Added image to multi panel');
  });
}

function load_chat_panel() {
  get_random_image(function (response) {
    var temp_content = "<p>chat panel</p><img src=\"" + response.randomImage + "\" style=";
    temp_content += get_image_style() + "/>";
    $("#chat-panel").html(temp_content);
    console.log('Added image to chat panel');
  });
}

/* /General Code */
/* -------------------------------------------------------------------- */
/* Debug Code */

function add_size(panel_id) {
  var str = panel_id;
  str += ": ";
  str += $(panel_id).innerWidth();
  str += "x";
  str += $(panel_id).innerHeight();
  return str
}

function update_size_record() {
  var str = "";
  str += add_size("#action-panel");
  str += " | ";
  str += add_size("#multi-panel");
  str += " | ";
  str += add_size("#chat-panel");
  $("#size-record").text(str);
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
