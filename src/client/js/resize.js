/*
 * Grid Realm Client - Resize library
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */

import {update_size_record} from "./debug.js";
import {get_font_size} from "./util.js";

export function resize_panels() {
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

export function resize_multipanel_content() {
  var height = $("#multi-panel").height();
  var content_height = height * 0.8;
  var nav_height = height * 0.2;
  $("#mp-content").height(content_height);
  $("#mp-nav-bar").height(nav_height);


  var width = $("#multi-panel").width();
  $("#mp-content").width(width);
  $("#mp-nav-bar").width(width);

  $("#mp-content").children("div").height(content_height);
  ($("#mp-content").children("div").children("img")
    ).css("max-height", content_height);

  var tab_icon_width = width / 5.5;
  $("#mp-nav-bar").children('nav').children("span").width(tab_icon_width);
  ($("#mp-nav-bar").children('nav').children("span").children("img")
    ).css("max-height", nav_height - get_font_size());
}