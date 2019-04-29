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
 * Grid Realm Client - Util library
 */

export function get_font_size() {
  return parseFloat(getComputedStyle($('html')[0]).fontSize);
}

export function build_image_tag(source, height) {
  if (typeof height === 'undefined') height = 'auto';
  return ('<img class="img-fluid mx-auto" style="' +
          ' height: ' + height + ';" src="' + source + '"/>');
}

export function get_cookie(a) {
  var b = document.cookie.match('(^|;)\\s*' + a + '\\s*=\\s*([^;]+)');
  return b ? b.pop() : '';
}

export function bootstrap_enabled () {
  return (typeof $().emulateTransitionEnd == 'function');
}
