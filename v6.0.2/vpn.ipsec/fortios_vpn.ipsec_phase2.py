#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
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
module: fortios_vpn.ipsec_phase2
short_description: Configure VPN autokey tunnel.
description:
    - This module is able to configure a FortiGate or FortiOS by
      allowing the user to configure vpn.ipsec feature and phase2 category.
      Examples includes all options and need to be adjusted to datasources before usage.
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
        default: root
    https:
        description:
            - Indicates if the requests towards FortiGate must use HTTPS
              protocol
        type: bool
        default: false
    vpn.ipsec_phase2:
        description:
            - Configure VPN autokey tunnel.
        default: null
        suboptions:
            state:
                description:
                    - Indicates whether to create or remove the object
                choices:
                    - present
                    - absent
            add-route:
                description:
                    - Enable/disable automatic route addition.
                choices:
                    - phase1
                    - enable
                    - disable
            auto-negotiate:
                description:
                    - Enable/disable IPsec SA auto-negotiation.
                choices:
                    - enable
                    - disable
            comments:
                description:
                    - Comment.
            dhcp-ipsec:
                description:
                    - Enable/disable DHCP-IPsec.
                choices:
                    - enable
                    - disable
            dhgrp:
                description:
                    - Phase2 DH group.
                choices:
                    - 1
                    - 2
                    - 5
                    - 14
                    - 15
                    - 16
                    - 17
                    - 18
                    - 19
                    - 20
                    - 21
                    - 27
                    - 28
                    - 29
                    - 30
                    - 31
            dst-addr-type:
                description:
                    - Remote proxy ID type.
                choices:
                    - subnet
                    - range
                    - ip
                    - name
            dst-end-ip:
                description:
                    - Remote proxy ID IPv4 end.
            dst-end-ip6:
                description:
                    - Remote proxy ID IPv6 end.
            dst-name:
                description:
                    - Remote proxy ID name. Source firewall.address.name firewall.addrgrp.name.
            dst-name6:
                description:
                    - Remote proxy ID name. Source firewall.address6.name firewall.addrgrp6.name.
            dst-port:
                description:
                    - Quick mode destination port (1 - 65535 or 0 for all).
            dst-start-ip:
                description:
                    - Remote proxy ID IPv4 start.
            dst-start-ip6:
                description:
                    - Remote proxy ID IPv6 start.
            dst-subnet:
                description:
                    - Remote proxy ID IPv4 subnet.
            dst-subnet6:
                description:
                    - Remote proxy ID IPv6 subnet.
            encapsulation:
                description:
                    - ESP encapsulation mode.
                choices:
                    - tunnel-mode
                    - transport-mode
            keepalive:
                description:
                    - Enable/disable keep alive.
                choices:
                    - enable
                    - disable
            keylife-type:
                description:
                    - Keylife type.
                choices:
                    - seconds
                    - kbs
                    - both
            keylifekbs:
                description:
                    - Phase2 key life in number of bytes of traffic (5120 - 4294967295).
            keylifeseconds:
                description:
                    - Phase2 key life in time in seconds (120 - 172800).
            l2tp:
                description:
                    - Enable/disable L2TP over IPsec.
                choices:
                    - enable
                    - disable
            name:
                description:
                    - IPsec tunnel name.
                required: true
            pfs:
                description:
                    - Enable/disable PFS feature.
                choices:
                    - enable
                    - disable
            phase1name:
                description:
                    - Phase 1 determines the options required for phase 2. Source vpn.ipsec.phase1.name.
            proposal:
                description:
                    - Phase2 proposal.
                choices:
                    - null-md5
                    - null-sha1
                    - null-sha256
                    - null-sha384
                    - null-sha512
                    - des-null
                    - des-md5
                    - des-sha1
                    - des-sha256
                    - des-sha384
                    - des-sha512
            protocol:
                description:
                    - Quick mode protocol selector (1 - 255 or 0 for all).
            replay:
                description:
                    - Enable/disable replay detection.
                choices:
                    - enable
                    - disable
            route-overlap:
                description:
                    - Action for overlapping routes.
                choices:
                    - use-old
                    - use-new
                    - allow
            selector-match:
                description:
                    - Match type to use when comparing selectors.
                choices:
                    - exact
                    - subset
                    - auto
            single-source:
                description:
                    - Enable/disable single source IP restriction.
                choices:
                    - enable
                    - disable
            src-addr-type:
                description:
                    - Local proxy ID type.
                choices:
                    - subnet
                    - range
                    - ip
                    - name
            src-end-ip:
                description:
                    - Local proxy ID end.
            src-end-ip6:
                description:
                    - Local proxy ID IPv6 end.
            src-name:
                description:
                    - Local proxy ID name. Source firewall.address.name firewall.addrgrp.name.
            src-name6:
                description:
                    - Local proxy ID name. Source firewall.address6.name firewall.addrgrp6.name.
            src-port:
                description:
                    - Quick mode source port (1 - 65535 or 0 for all).
            src-start-ip:
                description:
                    - Local proxy ID start.
            src-start-ip6:
                description:
                    - Local proxy ID IPv6 start.
            src-subnet:
                description:
                    - Local proxy ID subnet.
            src-subnet6:
                description:
                    - Local proxy ID IPv6 subnet.
            use-natip:
                description:
                    - Enable to use the FortiGate public IP as the source selector when outbound NAT is used.
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
  - name: Configure VPN autokey tunnel.
    fortios_vpn.ipsec_phase2:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      vpn.ipsec_phase2:
        state: "present"
        add-route: "phase1"
        auto-negotiate: "enable"
        comments: "<your_own_value>"
        dhcp-ipsec: "enable"
        dhgrp: "1"
        dst-addr-type: "subnet"
        dst-end-ip: "<your_own_value>"
        dst-end-ip6: "<your_own_value>"
        dst-name: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
        dst-name6: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        dst-port: "13"
        dst-start-ip: "<your_own_value>"
        dst-start-ip6: "<your_own_value>"
        dst-subnet: "<your_own_value>"
        dst-subnet6: "<your_own_value>"
        encapsulation: "tunnel-mode"
        keepalive: "enable"
        keylife-type: "seconds"
        keylifekbs: "21"
        keylifeseconds: "22"
        l2tp: "enable"
        name: "default_name_24"
        pfs: "enable"
        phase1name: "<your_own_value> (source vpn.ipsec.phase1.name)"
        proposal: "null-md5"
        protocol: "28"
        replay: "enable"
        route-overlap: "use-old"
        selector-match: "exact"
        single-source: "enable"
        src-addr-type: "subnet"
        src-end-ip: "<your_own_value>"
        src-end-ip6: "<your_own_value>"
        src-name: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
        src-name6: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        src-port: "38"
        src-start-ip: "<your_own_value>"
        src-start-ip6: "<your_own_value>"
        src-subnet: "<your_own_value>"
        src-subnet6: "<your_own_value>"
        use-natip: "enable"
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

from ansible.module_utils.basic import AnsibleModule

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


def filter_vpn.ipsec_phase2_data(json):
    option_list = ['add-route', 'auto-negotiate', 'comments',
                   'dhcp-ipsec', 'dhgrp', 'dst-addr-type',
                   'dst-end-ip', 'dst-end-ip6', 'dst-name',
                   'dst-name6', 'dst-port', 'dst-start-ip',
                   'dst-start-ip6', 'dst-subnet', 'dst-subnet6',
                   'encapsulation', 'keepalive', 'keylife-type',
                   'keylifekbs', 'keylifeseconds', 'l2tp',
                   'name', 'pfs', 'phase1name',
                   'proposal', 'protocol', 'replay',
                   'route-overlap', 'selector-match', 'single-source',
                   'src-addr-type', 'src-end-ip', 'src-end-ip6',
                   'src-name', 'src-name6', 'src-port',
                   'src-start-ip', 'src-start-ip6', 'src-subnet',
                   'src-subnet6', 'use-natip']
    dictionary = {}

    for attribute in option_list:
        if attribute in json:
            dictionary[attribute] = json[attribute]

    return dictionary


def vpn.ipsec_phase2(data, fos):
    vdom = data['vdom']
    vpn.ipsec_phase2_data = data['vpn.ipsec_phase2']
    filtered_data = filter_vpn.ipsec_phase2_data(vpn.ipsec_phase2_data)
    if vpn.ipsec_phase2_data['state'] == "present":
        return fos.set('vpn.ipsec',
                       'phase2',
                       data=filtered_data,
                       vdom=vdom)

    elif vpn.ipsec_phase2_data['state'] == "absent":
        return fos.delete('vpn.ipsec',
                          'phase2',
                          mkey=filtered_data['name'],
                          vdom=vdom)


def fortios_vpn.ipsec(data, fos):
    login(data)

    methodlist = ['vpn.ipsec_phase2']
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
        "https": {"required": False, "type": "bool", "default": "False"},
        "vpn.ipsec_phase2": {
            "required": False, "type": "dict",
            "options": {
                "state": {"required": True, "type": "str",
                          "choices": ["present", "absent"]},
                "add-route": {"required": False, "type": "str",
                              "choices": ["phase1", "enable", "disable"]},
                "auto-negotiate": {"required": False, "type": "str",
                                   "choices": ["enable", "disable"]},
                "comments": {"required": False, "type": "str"},
                "dhcp-ipsec": {"required": False, "type": "str",
                               "choices": ["enable", "disable"]},
                "dhgrp": {"required": False, "type": "str",
                          "choices": ["1", "2", "5",
                                      "14", "15", "16",
                                      "17", "18", "19",
                                      "20", "21", "27",
                                      "28", "29", "30",
                                      "31"]},
                "dst-addr-type": {"required": False, "type": "str",
                                  "choices": ["subnet", "range", "ip",
                                              "name"]},
                "dst-end-ip": {"required": False, "type": "str"},
                "dst-end-ip6": {"required": False, "type": "str"},
                "dst-name": {"required": False, "type": "str"},
                "dst-name6": {"required": False, "type": "str"},
                "dst-port": {"required": False, "type": "int"},
                "dst-start-ip": {"required": False, "type": "str"},
                "dst-start-ip6": {"required": False, "type": "str"},
                "dst-subnet": {"required": False, "type": "str"},
                "dst-subnet6": {"required": False, "type": "str"},
                "encapsulation": {"required": False, "type": "str",
                                  "choices": ["tunnel-mode", "transport-mode"]},
                "keepalive": {"required": False, "type": "str",
                              "choices": ["enable", "disable"]},
                "keylife-type": {"required": False, "type": "str",
                                 "choices": ["seconds", "kbs", "both"]},
                "keylifekbs": {"required": False, "type": "int"},
                "keylifeseconds": {"required": False, "type": "int"},
                "l2tp": {"required": False, "type": "str",
                         "choices": ["enable", "disable"]},
                "name": {"required": True, "type": "str"},
                "pfs": {"required": False, "type": "str",
                        "choices": ["enable", "disable"]},
                "phase1name": {"required": False, "type": "str"},
                "proposal": {"required": False, "type": "str",
                             "choices": ["null-md5", "null-sha1", "null-sha256",
                                         "null-sha384", "null-sha512", "des-null",
                                         "des-md5", "des-sha1", "des-sha256",
                                         "des-sha384", "des-sha512"]},
                "protocol": {"required": False, "type": "int"},
                "replay": {"required": False, "type": "str",
                           "choices": ["enable", "disable"]},
                "route-overlap": {"required": False, "type": "str",
                                  "choices": ["use-old", "use-new", "allow"]},
                "selector-match": {"required": False, "type": "str",
                                   "choices": ["exact", "subset", "auto"]},
                "single-source": {"required": False, "type": "str",
                                  "choices": ["enable", "disable"]},
                "src-addr-type": {"required": False, "type": "str",
                                  "choices": ["subnet", "range", "ip",
                                              "name"]},
                "src-end-ip": {"required": False, "type": "str"},
                "src-end-ip6": {"required": False, "type": "str"},
                "src-name": {"required": False, "type": "str"},
                "src-name6": {"required": False, "type": "str"},
                "src-port": {"required": False, "type": "int"},
                "src-start-ip": {"required": False, "type": "str"},
                "src-start-ip6": {"required": False, "type": "str"},
                "src-subnet": {"required": False, "type": "str"},
                "src-subnet6": {"required": False, "type": "str"},
                "use-natip": {"required": False, "type": "str",
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

    global fos
    fos = FortiOSAPI()

    is_error, has_changed, result = fortios_vpn.ipsec(module.params, fos)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
