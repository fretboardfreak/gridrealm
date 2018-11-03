/*
 * Grid Realm Client - Chat Panel Library
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */

import {APIhelpers} from "./api.js"

export function load_chat_panel() {
  var event_source = new EventSource("/sysmsg");
  event_source.onmessage = function(e) {
    console.log(e.data);
    $("#sys-msgs").prepend('<li>' + e.data + '</li>');
  };
}
