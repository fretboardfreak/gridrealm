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
 * Grid Realm Client - Multi Panel Library
 */

export function change_multipanel_view(panel) {
  var full_panel_name = '#mp-' + panel;
  // disable all tabs first
  $('#mp-content').children().hide();
  $('#mp-nav-bar').children('nav').children('span').removeClass('active');
  // then enable the one we want to see
  $(full_panel_name + '-lnk').addClass('active');
  $(full_panel_name).show();
}

export function load_multi_panel() {
  change_multipanel_view('navigation'); // default view is nav
}

export function load_minimap(data) {
  var row;
  var cell;
  var mm_html = '';
  console.log('Loading minimp.');
  $('#minimap').html('');  // clear out old contents of minimap
  for (row in data) {
    mm_html += '<div class="row no-gutters no-wrap">';
    for (cell in data[row]) {
      mm_html += '<img src="_assets/tiles/';
      mm_html += data[row][cell][0];
      mm_html += '" class="img-fluid" style="height: 50px; width: 50px;"/>';
    }
    mm_html += '</div>';
  }
  $('#minimap').html(mm_html);
}

export function load_nav_buttons(data) {
  console.log('Loading nav buttons.');
  var index;
  var btn_id;
  for (index in data) {
    btn_id = '#' + index + '-btn';
    if (data[index]) {
      $(btn_id).removeClass('disabled');
    } else {
      $(btn_id).addClass('disabled');
    }
  }
}
