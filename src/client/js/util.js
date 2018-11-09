/*
 * Grid Realm Client - Util library
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */

export function get_font_size() {
  return parseFloat(getComputedStyle($('html')[0]).fontSize);
}

export function build_image_tag(source, height) {
  if (typeof height === 'undefined') height = "auto";
  return ("<img class=\"img-fluid mx-auto\" style\"" +
          " height: " + height + ";\" src=\"" + source + "\"/>");
}

export function get_cookie(a) {
  var b = document.cookie.match('(^|;)\\s*' + a + '\\s*=\\s*([^;]+)');
  return b ? b.pop() : '';
}

export function bootstrap_enabled () {
  return (typeof $().emulateTransitionEnd == 'function');
}
