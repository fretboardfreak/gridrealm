/*
 * Grid Realm Client - API library
 *
 *
 * Copyright Curtis Sand, Dennison Gaetz - 2018
 *
 */

import {build_image_tag} from './util.js';

export var URI = {};
URI.version = 'api/version';
URI.randomImage = 'api/randomImage';
URI.randomActionImage = 'api/randomActionImage';
URI.randomInventoryImage = 'api/randomInventoryImage';
URI.logout = 'logout';

export class API {
  static get_random_image(success) {
    $.ajax({
      url: URI.randomImage,
      data: '',
      type: 'GET',
      success: success,
      error: function (error) {console.log(error);}
    });
  }

  static get_api_version(success) {
    $.ajax({
      url: URI.version,
      data: '',
      type: 'GET',
      success: success,
      error: function (error) {console.log(error);}
    });
  }

  static get_random_action_image(success) {
    $.ajax({
      url: URI.randomActionImage,
      data: '',
      type: 'GET',
      success: success,
      error: function (error) {console.log(error);}
    });
  }

  static get_random_inventory_image(success) {
    $.ajax({
      url: URI.randomInventoryImage,
      data: '',
      type: 'GET',
      success: success,
      error: function (error) {console.log(error);}
    });
  }
}

export class APIhelpers {
  static add_random_image(tag, height) {
    if (typeof height === 'undefined') height = 'auto';
    API.get_random_image(function (response){
      tag.html(build_image_tag(response.image, height));
    });
  }

  static add_random_action_image(tag, height) {
    if (typeof height === 'undefined') height = 'auto';
    API.get_random_action_image(function (response){
      tag.html(build_image_tag(response.image, height));
    });
  }

  static add_random_inventory_image(tag, height) {
    if (typeof height === 'undefined') height = 'auto';
    API.get_random_inventory_image(function (response){
      tag.html(build_image_tag(response.image, height));
    });
  }

}
