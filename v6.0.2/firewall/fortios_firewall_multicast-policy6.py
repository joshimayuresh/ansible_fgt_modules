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
module: fortios_firewall_multicast-policy6
short_description: Configure IPv6 multicast NAT policies.
description:
    - This module is able to configure a FortiGate or FortiOS by
      allowing the user to configure firewall feature and multicast-policy6 category.
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
    firewall_multicast-policy6:
        description:
            - Configure IPv6 multicast NAT policies.
        default: null
        suboptions:
            action:
                description:
                    - Accept or deny traffic matching the policy.
                choices:
                    - accept
                    - deny
            dstaddr:
                description:
                    - IPv6 destination address name.
                suboptions:
                    name:
                        description:
                            - Address name. Source: firewall.multicast-address6.name.
                        required: true
            dstintf:
                description:
                    - IPv6 destination interface name. Source: system.interface.name system.zone.name.
            end-port:
                description:
                    - Integer value for ending TCP/UDP/SCTP destination port in range (1 - 65535, default = 65535).
            id:
                description:
                    - Policy ID.
                required: true
            logtraffic:
                description:
                    - Enable/disable logging traffic accepted by this policy.
                choices:
                    - enable
                    - disable
            protocol:
                description:
                    - Integer value for the protocol type as defined by IANA (0 - 255, default = 0).
            srcaddr:
                description:
                    - IPv6 source address name.
                suboptions:
                    name:
                        description:
                            - Address name. Source: firewall.address6.name firewall.addrgrp6.name.
                        required: true
            srcintf:
                description:
                    - IPv6 source interface name. Source: system.interface.name system.zone.name.
            start-port:
                description:
                    - Integer value for starting TCP/UDP/SCTP destination port in range (1 - 65535, default = 1).
            status:
                description:
                    - Enable/disable this policy.
                choices:
                    - enable
                    - disable
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Configure IPv6 multicast NAT policies.
    fortios_firewall_multicast-policy6:
      host:  "{{  host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{  vdom }}"
      firewall_multicast-policy6:
        state: "present"
        action: "accept"
        dstaddr:
         -
            name: "default_name_5 (source: firewall.multicast-address6.name)"
        dstintf: "<your_own_value> (source: system.interface.name system.zone.name)"
        end-port: "7"
        id:  "8"
        logtraffic: "enable"
        protocol: "10"
        srcaddr:
         -
            name: "default_name_12 (source: firewall.address6.name firewall.addrgrp6.name)"
        srcintf: "<your_own_value> (source: system.interface.name system.zone.name)"
        start-port: "14"
        status: "enable"
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


def filter_firewall_multicast-policy6_data(json):
    option_list = ['action', 'dstaddr', 'dstintf',
                   'end-port', 'id', 'logtraffic',
                   'protocol', 'srcaddr', 'srcintf',
                   'start-port', 'status']
    dictionary = {}

    for attribute in option_list:
        if attribute in json:
            dictionary[attribute] = json[attribute]

    return dictionary


def firewall_multicast-policy6(data, fos):
    vdom = data['vdom']
    firewall_multicast-policy6_data = data['firewall_multicast-policy6']
    filtered_data = filter_firewall_multicast - \
        policy6_data(firewall_multicast-policy6_data)

    if firewall_multicast-policy6_data['state'] == "present":
        return fos.set('firewall',
                       'multicast-policy6',
                       data=filtered_data,
                       vdom=vdom)

    elif firewall_multicast-policy6_data['state'] == "absent":
        return fos.delete('firewall',
                          'multicast-policy6',
                          mkey=filtered_data['id'],
                          vdom=vdom)


def fortios_firewall(data, fos):
    host = data['host']
    username = data['username']
    password = data['password']
    fos.https('off')
    fos.login(host, username, password)

    methodlist = ['firewall_multicast-policy6']
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
        "firewall_multicast-policy6": {
            "required": False, "type": "dict",
            "options": {
                "state": {"required": True, "type": "str"},
                "action": {"required": False, "type": "str",
                           "choices": ["accept", "deny"]},
                "dstaddr": {"required": False, "type": "list",
                            "options": {
                                "name": {"required": True, "type": "str"}
                            }},
                "dstintf": {"required": False, "type": "str"},
                "end-port": {"required": False, "type": "int"},
                "id": {"required": True, "type": "int"},
                "logtraffic": {"required": False, "type": "str",
                               "choices": ["enable", "disable"]},
                "protocol": {"required": False, "type": "int"},
                "srcaddr": {"required": False, "type": "list",
                            "options": {
                                "name": {"required": True, "type": "str"}
                            }},
                "srcintf": {"required": False, "type": "str"},
                "start-port": {"required": False, "type": "int"},
                "status": {"required": False, "type": "str",
                           "choices": ["enable", "disable"]}

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

    is_error, has_changed, result = fortios_firewall(module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
