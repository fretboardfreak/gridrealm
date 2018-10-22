/*
 * Grid Realm Client - Chat Panel Library
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */

import {APIhelpers} from "./api.js"

export function load_chat_panel() {
  APIhelpers.add_random_action_image($("#chat-panel"));
}
