/*
 * Grid Realm Client - Multi Panel Library
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
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
  var mm_html;
  console.log('Loading minimp.');
  $('#minimap').html('');  // clear out old contents of minimap
  for (row in data) {
    mm_html += '<tr>';
    for (cell in data[row]) {
      mm_html += '<td class="border"><code>';
      var top = data[row][cell][0];
      top = top.replace(' ', '&nbsp;');
      mm_html += top + '</code><br><code>';
      var bot = data[row][cell][1];
      bot = bot.replace(' ', '&nbsp;');
      mm_html += bot + '</code></td>';
    }
    mm_html += '</tr>';
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
