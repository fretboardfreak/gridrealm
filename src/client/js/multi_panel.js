/*
 * Grid Realm Client - Multi Panel Library
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */

import {APIhelpers} from "./api.js"

export function change_multipanel_view(panel) {
  var full_panel_name = "#mp-" + panel;
  // disable all tabs first
  $("#mp-content").children().hide();
  $("#mp-nav-bar").children('nav').children('span').removeClass('active');
  // then enable the one we want to see
  $(full_panel_name + "-lnk").addClass('active');
  $(full_panel_name).show();
}

export function load_multi_panel() {
  change_multipanel_view('navigation'); // default view is nav

  APIhelpers.add_random_inventory_image($("#mp-inventory"));
  APIhelpers.add_random_inventory_image($("#mp-skill"));
  APIhelpers.add_random_inventory_image($("#mp-quest"));
  APIhelpers.add_random_inventory_image($("#mp-social"));
}
