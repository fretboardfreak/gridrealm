/*
 * Grid Realm Client - Debug library
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */


function add_size(panel_id) {
  return (panel_id + ': ' + $(panel_id).innerWidth() + 'x' +
          $(panel_id).innerHeight());
}

export function update_size_record() {
  $('#size-record').text(add_size('#action-panel') + ' | ' +
                         add_size('#multi-panel') + ' | ' +
                         add_size('#chat-panel'));
}
