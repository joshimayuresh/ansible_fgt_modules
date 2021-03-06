#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2019 Fortinet, Inc.
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

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_system_resource_limits
short_description: Configure resource limits in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS by allowing the
      user to set and modify system feature and resource_limits category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.2
version_added: "2.8"
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
            - FortiOS or FortiGate ip address.
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
        default: root
    https:
        description:
            - Indicates if the requests towards FortiGate must use HTTPS
              protocol
        type: bool
        default: true
    system_resource_limits:
        description:
            - Configure resource limits.
        default: null
        suboptions:
            custom-service:
                description:
                    - Maximum number of firewall custom services.
            dialup-tunnel:
                description:
                    - Maximum number of dial-up tunnels.
            firewall-address:
                description:
                    - Maximum number of firewall addresses.
            firewall-addrgrp:
                description:
                    - Maximum number of firewall address groups.
            firewall-policy:
                description:
                    - Maximum number of firewall policies.
            ipsec-phase1:
                description:
                    - Maximum number of VPN IPsec phase1 tunnels.
            ipsec-phase1-interface:
                description:
                    - Maximum number of VPN IPsec phase1 interface tunnels.
            ipsec-phase2:
                description:
                    - Maximum number of VPN IPsec phase2 tunnels.
            ipsec-phase2-interface:
                description:
                    - Maximum number of VPN IPsec phase2 interface tunnels.
            log-disk-quota:
                description:
                    - Log disk quota in MB.
            onetime-schedule:
                description:
                    - Maximum number of firewall one-time schedules.
            proxy:
                description:
                    - Maximum number of concurrent proxy users.
            recurring-schedule:
                description:
                    - Maximum number of firewall recurring schedules.
            service-group:
                description:
                    - Maximum number of firewall service groups.
            session:
                description:
                    - Maximum number of sessions.
            sslvpn:
                description:
                    - Maximum number of SSL-VPN.
            user:
                description:
                    - Maximum number of local users.
            user-group:
                description:
                    - Maximum number of user groups.
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Configure resource limits.
    fortios_system_resource_limits:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      https: "False"
      system_resource_limits:
        custom-service: "3"
        dialup-tunnel: "4"
        firewall-address: "5"
        firewall-addrgrp: "6"
        firewall-policy: "7"
        ipsec-phase1: "8"
        ipsec-phase1-interface: "9"
        ipsec-phase2: "10"
        ipsec-phase2-interface: "11"
        log-disk-quota: "12"
        onetime-schedule: "13"
        proxy: "14"
        recurring-schedule: "15"
        service-group: "16"
        session: "17"
        sslvpn: "18"
        user: "19"
        user-group: "20"
'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule


def login(data, fos):
    host = data['host']
    username = data['username']
    password = data['password']

    fos.debug('on')
    if 'https' in data and not data['https']:
        fos.https('off')
    else:
        fos.https('on')

    fos.login(host, username, password)


def filter_system_resource_limits_data(json):
    option_list = ['custom-service', 'dialup-tunnel', 'firewall-address',
                   'firewall-addrgrp', 'firewall-policy', 'ipsec-phase1',
                   'ipsec-phase1-interface', 'ipsec-phase2', 'ipsec-phase2-interface',
                   'log-disk-quota', 'onetime-schedule', 'proxy',
                   'recurring-schedule', 'service-group', 'session',
                   'sslvpn', 'user', 'user-group']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def system_resource_limits(data, fos):
    vdom = data['vdom']
    system_resource_limits_data = data['system_resource_limits']
    filtered_data = filter_system_resource_limits_data(system_resource_limits_data)

    return fos.set('system',
                   'resource-limits',
                   data=filtered_data,
                   vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_system(data, fos):
    login(data, fos)

    if data['system_resource_limits']:
        resp = system_resource_limits(data, fos)

    fos.logout()
    return not is_successful_status(resp), \
        resp['status'] == "success", \
        resp


def main():
    fields = {
        "host": {"required": True, "type": "str"},
        "username": {"required": True, "type": "str"},
        "password": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "https": {"required": False, "type": "bool", "default": True},
        "system_resource_limits": {
            "required": False, "type": "dict",
            "options": {
                "custom-service": {"required": False, "type": "int"},
                "dialup-tunnel": {"required": False, "type": "int"},
                "firewall-address": {"required": False, "type": "int"},
                "firewall-addrgrp": {"required": False, "type": "int"},
                "firewall-policy": {"required": False, "type": "int"},
                "ipsec-phase1": {"required": False, "type": "int"},
                "ipsec-phase1-interface": {"required": False, "type": "int"},
                "ipsec-phase2": {"required": False, "type": "int"},
                "ipsec-phase2-interface": {"required": False, "type": "int"},
                "log-disk-quota": {"required": False, "type": "int"},
                "onetime-schedule": {"required": False, "type": "int"},
                "proxy": {"required": False, "type": "int"},
                "recurring-schedule": {"required": False, "type": "int"},
                "service-group": {"required": False, "type": "int"},
                "session": {"required": False, "type": "int"},
                "sslvpn": {"required": False, "type": "int"},
                "user": {"required": False, "type": "int"},
                "user-group": {"required": False, "type": "int"}

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

    is_error, has_changed, result = fortios_system(module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
