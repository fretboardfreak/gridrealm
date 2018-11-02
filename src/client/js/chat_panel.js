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
    $("#chat-panel").prepend('<div class="alert-info w-100 m-0 row" ' +
                             'role="alert" style="height: 1rem;">' +
                             e.data + '</div>');
  };
}
