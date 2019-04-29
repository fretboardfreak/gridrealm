/*
 * Copyright 2019 Curtis Sand <curtissand@gmail.com>,
 *                Dennison Gaetz <djgaetz@gmail.com>
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Grid Realm Client - Auth Library
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
