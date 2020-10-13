# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the
# cli_rm_builder.
#
# Manually editing this file is not advised.
#
# To update the argspec make the desired changes
# in the module docstring and re-run
# cli_rm_builder.
#
#############################################

"""
The arg spec for the nxos_ospf_interfaces module
"""


class Ospf_interfacesArgs(object):  # pylint: disable=R0903
    """The arg spec for the nxos_ospf_interfaces module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "running_config": {"type": "str"},
        "config": {
            "type": "list",
            "elements": "dict",
            "options": {
                "name": {"type": "str", "required": True},
                "address_family": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "afi": {
                            "type": "str",
                            "choices": ["ipv4", "ipv6"],
                            "required": True,
                        },
                        "processes": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "process_id": {
                                    "type": "str",
                                    "required": True,
                                },
                                "area": {
                                    "type": "dict",
                                    "options": {
                                        "area_id": {
                                            "type": "str",
                                            "required": True,
                                        },
                                        "secondaries": {"type": "bool"},
                                    },
                                },
                                "multi_areas": {
                                    "type": "list",
                                    "elements": "str",
                                },
                            },
                        },
                        "multi_areas": {"type": "list", "elements": "str"},
                        "authentication": {
                            "type": "dict",
                            "options": {
                                "key_chain": {"type": "str"},
                                "message_digest": {"type": "bool"},
                                "enable": {"type": "bool"},
                                "null_auth": {"type": "bool"},
                            },
                        },
                        "authentication_key": {
                            "type": "dict",
                            "options": {
                                "encryption": {"type": "int"},
                                "key": {"type": "str", "required": True},
                            },
                        },
                        "message_digest_key": {
                            "type": "dict",
                            "options": {
                                "key_id": {"type": "int"},
                                "encryption": {"type": "int"},
                                "key": {"type": "str", "required": True},
                            },
                        },
                        "cost": {"type": "int"},
                        "dead_interval": {"type": "int"},
                        "hello_interval": {"type": "int"},
                        "instance": {"type": "int"},
                        "mtu_ignore": {"type": "bool"},
                        "network": {
                            "type": "str",
                            "choices": ["broadcast", "point-to-point"],
                        },
                        "passive_interface": {"type": "bool"},
                        "priority": {"type": "int"},
                        "retransmit_interval": {"type": "int"},
                        "shutdown": {"type": "bool"},
                        "transmit_delay": {"type": "int"},
                    },
                },
            },
        },
        "state": {
            "type": "str",
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "gathered",
                "parsed",
                "rendered",
            ],
            "default": "merged",
        },
    }  # pylint: disable=C0301
