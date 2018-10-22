/*
 * Grid Realm Client - API library
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */

import {build_image_tag} from "./util.js"

var version = "api/version";
var randomImage = "api/randomImage";
export var URI = { version, randomImage }

export class API {
  static get_random_image(success) {
    $.ajax({
      url: URI.randomImage,
      data: '',
      type: 'GET',
      success: success,
      error: function (error) {console.log(error);}
    });
  };

  static get_api_version(success) {
    $.ajax({
      url: URI.version,
      data: '',
      type: 'GET',
      success: success,
      error: function (error) {console.log(error);}
    });
  };
}

export class APIhelpers {
  static add_random_image(tag, height) {
    if (typeof height === 'undefined') height = "auto";
    API.get_random_image(function (response){
      tag.html(build_image_tag(response.randomImage, height));
  });
}

}
