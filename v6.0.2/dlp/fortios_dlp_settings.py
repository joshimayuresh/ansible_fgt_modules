#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import AnsibleModule
# Copyright 2018 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# the lib use python logging can get it if the following is set in your
# Ansible config.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_dlp_settings
short_description: Designate logical storage for DLP fingerprint database.
description:
    - This module is able to configure a FortiGate or FortiOS by
      allowing the user to configure dlp feature and settings category.
      Examples includes all options and need to be adjusted to datasources before usage.
      Tested with FOS: v6.0.2
version_added: "2.6"
author:
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Requires fortiosapi library developed by Fortinet
    - Run as a local_action in your playbook
requirements:
    - fortiosapi>=0.9.8
options:
    host:
       description:
            - FortiOS or FortiGate ip adress.
       required: true
    username:
        description:
            - FortiOS or FortiGate username.
        required: true
    password:
        description:
            - FortiOS or FortiGate password.
        default: ""
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        default: "root"
    https:
        description:
            - Indicates if the requests towards FortiGate must use HTTPS
              protocol
    dlp_settings:
        description:
            - Designate logical storage for DLP fingerprint database.
        default: null
        suboptions:
            cache-mem-percent:
                description:
                    - Maximum percentage of available memory allocated to caching (1 - 15%).
            chunk-size:
                description:
                    - Maximum fingerprint chunk size.  **Changing will flush the entire database**.
            db-mode:
                description:
                    - Behaviour when the maximum size is reached.
                choices:
                    - stop-adding
                    - remove-modified-then-oldest
                    - remove-oldest
            size:
                description:
                    - Maximum total size of files within the storage (MB).
            storage-device:
                description:
                    - Storage device name. Source: system.storage.name.
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Designate logical storage for DLP fingerprint database.
    fortios_dlp_settings:
      host:  "{{  host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{  vdom }}"
      dlp_settings:
        state: "present"
        cache-mem-percent: "3"
        chunk-size: "4"
        db-mode: "stop-adding"
        size: "6"
        storage-device: "<your_own_value> (source: system.storage.name)"
'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: string
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: string
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: string
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: string
  sample: "key1"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: string
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: string
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: string
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: string
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: string
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: string
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: string
  sample: "v5.6.3"

'''

fos = None


def login(data):
    host = data['host']
    username = data['username']
    password = data['password']

    fos.debug('on')
    if 'https' in data and not data['https']:
        fos.https('off')
    else:
        fos.https('on')

    fos.login(host, username, password)


def filter_dlp_settings_data(json):
    option_list = ['cache-mem-percent', 'chunk-size', 'db-mode',
                   'size', 'storage-device']
    dictionary = {}

    for attribute in option_list:
        if attribute in json:
            dictionary[attribute] = json[attribute]

    return dictionary


def dlp_settings(data, fos):
    vdom = data['vdom']
    dlp_settings_data = data['dlp_settings']
    filtered_data = filter_dlp_settings_data(dlp_settings_data)

    if dlp_settings_data['state'] == "present":
        return fos.set('dlp',
                       'settings',
                       data=filtered_data,
                       vdom=vdom)

    elif dlp_settings_data['state'] == "absent":
        return fos.delete('dlp',
                          'settings',
                          mkey=filtered_data['id'],
                          vdom=vdom)


def fortios_dlp(data, fos):
    host = data['host']
    username = data['username']
    password = data['password']
    fos.https('off')
    fos.login(host, username, password)

    methodlist = ['dlp_settings']
    for method in methodlist:
        if data[method]:
            resp = eval(method)(data, fos)
            break

    fos.logout()
    return not resp['status'] == "success", resp['status'] == "success", resp


def main():
    fields = {
        "host": {"required": True, "type": "str"},
        "username": {"required": True, "type": "str"},
        "password": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "https": {"required": False, "type": "bool", "default": "True"},
        "dlp_settings": {
            "required": False, "type": "dict",
            "options": {
                "state": {"required": True, "type": "str"},
                "cache-mem-percent": {"required": False, "type": "int"},
                "chunk-size": {"required": False, "type": "int"},
                "db-mode": {"required": False, "type": "str",
                            "choices": ["stop-adding", "remove-modified-then-oldest", "remove-oldest"]},
                "size": {"required": False, "type": "int"},
                "storage-device": {"required": False, "type": "str"}

            }
        }
    }

    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)
    try:
        from fortiosapi import FortiOSAPI
    except ImportError:
        module.fail_json(msg="fortiosapi module is required")

    fos = FortiOSAPI()

    is_error, has_changed, result = fortios_dlp(module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
