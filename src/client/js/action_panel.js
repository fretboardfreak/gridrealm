/*
 * Grid Realm Client - Action Panel Library
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */

import {APIhelpers} from "./api.js"

export function load_action_panel() {
  APIhelpers.add_random_action_image($("#ap-image"));
}
