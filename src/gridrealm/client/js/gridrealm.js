/*!
 * Grid Realm Core Client Library
 * documentation: http://fretboardfreak.com/gridrealm/
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 * Date: 2018-10-04-11:00
 */

function init_panels() {
  console.log("initializing action panel");
  var canvas = document.getElementById("actionpanel");

  /* TODO: implement initialization */
  var context = canvas.getContext("2d");
  context.font = "30px Arial";
  context.fillText("Hello World", 10, 50);
}

/* On DOM Ready*/
$(document).ready(function(){
  console.log("initializing action panels");
  init_panels();
});
