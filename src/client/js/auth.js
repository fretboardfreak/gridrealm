/*
 * Grid Realm Client - Auth Library
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */

import {API} from './api.js';
import {get_cookie} from './util.js';


// TODO: implement Facebook OAuth Login

export function is_logged_in() {
  var username = get_cookie('username');
  if (username === '') {
    return false;
  } else {
    return true;
  }
}

// TODO: Use a logout method rather than direct link to logout API.
//       This would let us provide messages, etc. on logout.
// export function logout() {
//   alert('logging out needs to be implemented')
//   console.log('logging out needs to be implemented...')
// }

export function create_account() {
  API.get_api_version(function (response) {
    alert('Creating an account using API version: ' + response.version);
  });
}
