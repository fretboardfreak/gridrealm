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
 * Grid Realm Client - API library
 */

import {build_image_tag} from './util.js';

export var URI = {};
URI.logout = 'logout';
URI.version = 'api/version';
URI.randomImage = 'api/randomImage';
URI.randomActionImage = 'api/randomActionImage';
URI.randomInventoryImage = 'api/randomInventoryImage';
URI.location = 'api/location';
URI.move = 'api/move';

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

  static get_location(success) {
    $.ajax({
      url: URI.location,
      data: '',
      type: 'GET',
      success: success,
      error: function (error) {console.log(error);}
    });
  }

  static move(direction, success) {
    $.ajax({
      url: URI.move,
      data: {'direction': direction},
      // dataType: 'text',
      type: 'POST',
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
