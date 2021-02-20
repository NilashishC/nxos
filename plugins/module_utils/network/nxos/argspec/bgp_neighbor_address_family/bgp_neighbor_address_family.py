# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
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
The arg spec for the nxos_bgp_neighbor_address_family module
"""


class Bgp_neighbor_address_familyArgs(object):  # pylint: disable=R0903
    """The arg spec for the nxos_bgp_neighbor_address_family module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "running_config": {"type": "str"},
        "config": {
            "type": "dict",
            "options": {
                "as_number": {"type": "str"},
                "neighbors": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "neighbor": {"type": "str", "required": True},
                        "address_family": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "afi": {
                                    "type": "str",
                                    "choices": [
                                        "ipv4",
                                        "ipv6",
                                        "link-state",
                                        "vpnv4",
                                        "vpnv6",
                                        "l2vpn",
                                    ],
                                    "required": True,
                                },
                                "safi": {
                                    "type": "str",
                                    "choices": [
                                        "unicast",
                                        "multicast",
                                        "mvpn",
                                        "evpn",
                                    ],
                                },
                                "no_advertise_local_labeled_route": {
                                    "type": "bool"
                                },
                                "advertise_map": {
                                    "type": "dict",
                                    "options": {
                                        "route_map": {
                                            "type": "str",
                                            "required": True,
                                        },
                                        "exist_map": {"type": "str"},
                                        "non_exist_map": {"type": "str"},
                                    },
                                },
                                "advertisement_interval": {"type": "int"},
                                "allowas_in": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "max_occurences": {"type": "int"},
                                    },
                                },
                                "no_advertise_gw_ip": {"type": "bool"},
                                "as_override": {"type": "bool"},
                                "capability": {
                                    "type": "dict",
                                    "options": {
                                        "additional_paths": {
                                            "type": "dict",
                                            "options": {
                                                "receive": {
                                                    "type": "str",
                                                    "choices": [
                                                        "enable",
                                                        "disable",
                                                    ],
                                                },
                                                "send": {
                                                    "type": "str",
                                                    "choices": [
                                                        "enable",
                                                        "disable",
                                                    ],
                                                },
                                            },
                                        }
                                    },
                                },
                                "default_originate": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "route_map": {"type": "str"},
                                    },
                                },
                                "disable_peer_as_check": {"type": "bool"},
                                "filter_list": {
                                    "type": "dict",
                                    "options": {
                                        "in": {"type": "str"},
                                        "out": {"type": "str"},
                                    },
                                },
                                "inherit": {
                                    "type": "dict",
                                    "options": {
                                        "template": {"type": "str"},
                                        "sequence": {"type": "int"},
                                    },
                                },
                                "maximum_prefix": {
                                    "type": "dict",
                                    "options": {
                                        "max_prefix_limit": {"type": "int"},
                                        "generate_warning_threshold": {
                                            "type": "int"
                                        },
                                        "restart_interval": {"type": "int"},
                                        "warning_only": {"type": "bool"},
                                    },
                                },
                                "next_hop_self": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "all_routes": {"type": "bool"},
                                    },
                                },
                                "next_hop_third_party": {"type": "bool"},
                                "prefix_list": {
                                    "type": "dict",
                                    "options": {
                                        "in": {"type": "str"},
                                        "out": {"type": "str"},
                                    },
                                },
                                "rewrite_evpn_rt_asn": {"type": "bool"},
                                "route_map": {
                                    "type": "dict",
                                    "options": {
                                        "in": {"type": "str"},
                                        "out": {"type": "str"},
                                    },
                                },
                                "route_reflector_client": {"type": "bool"},
                                "send_community": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "extended": {"type": "bool"},
                                        "standard": {"type": "bool"},
                                        "both": {"type": "bool"},
                                    },
                                },
                                "soft_reconfiguration_inbound": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "always": {"type": "bool"},
                                    },
                                },
                                "soo": {"type": "str"},
                                "suppress_inactive": {"type": "bool"},
                                "unsuppress_map": {"type": "str"},
                                "weight": {"type": "int"},
                            },
                        },
                    },
                },
                "vrfs": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "vrf": {"type": "str"},
                        "neighbors": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "neighbor": {"type": "str", "required": True},
                                "address_family": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {
                                        "afi": {
                                            "type": "str",
                                            "choices": [
                                                "ipv4",
                                                "ipv6",
                                                "link-state",
                                                "vpnv4",
                                                "vpnv6",
                                                "l2vpn",
                                            ],
                                            "required": True,
                                        },
                                        "safi": {
                                            "type": "str",
                                            "choices": [
                                                "unicast",
                                                "multicast",
                                                "mvpn",
                                                "evpn",
                                            ],
                                        },
                                        "no_advertise_local_labeled_route": {
                                            "type": "bool"
                                        },
                                        "advertise_map": {
                                            "type": "dict",
                                            "required_one_of": [
                                                ("exist_map", "non_exist_map")
                                            ],
                                            "options": {
                                                "route_map": {
                                                    "type": "str",
                                                    "required": True,
                                                },
                                                "exist_map": {"type": "str"},
                                                "non_exist_map": {
                                                    "type": "str"
                                                },
                                            },
                                        },
                                        "advertisement_interval": {
                                            "type": "int"
                                        },
                                        "allowas_in": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "max_occurences": {
                                                    "type": "int"
                                                },
                                            },
                                        },
                                        "no_advertise_gw_ip": {"type": "bool"},
                                        "as_override": {"type": "bool"},
                                        "capability": {
                                            "type": "dict",
                                            "options": {
                                                "additional_paths": {
                                                    "type": "dict",
                                                    "options": {
                                                        "receive": {
                                                            "type": "str",
                                                            "choices": [
                                                                "enable",
                                                                "disable",
                                                            ],
                                                        },
                                                        "send": {
                                                            "type": "str",
                                                            "choices": [
                                                                "enable",
                                                                "disable",
                                                            ],
                                                        },
                                                    },
                                                }
                                            },
                                        },
                                        "default_originate": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "route_map": {"type": "str"},
                                            },
                                        },
                                        "disable_peer_as_check": {
                                            "type": "bool"
                                        },
                                        "filter_list": {
                                            "type": "dict",
                                            "options": {
                                                "in": {"type": "str"},
                                                "out": {"type": "str"},
                                            },
                                        },
                                        "inherit": {
                                            "type": "dict",
                                            "options": {
                                                "template": {"type": "str"},
                                                "sequence": {"type": "int"},
                                            },
                                        },
                                        "maximum_prefix": {
                                            "type": "dict",
                                            "options": {
                                                "max_prefix_limit": {
                                                    "type": "int"
                                                },
                                                "generate_warning_threshold": {
                                                    "type": "int"
                                                },
                                                "restart_interval": {
                                                    "type": "int"
                                                },
                                                "warning_only": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "next_hop_self": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "all_routes": {"type": "bool"},
                                            },
                                        },
                                        "next_hop_third_party": {
                                            "type": "bool"
                                        },
                                        "prefix_list": {
                                            "type": "dict",
                                            "options": {
                                                "in": {"type": "str"},
                                                "out": {"type": "str"},
                                            },
                                        },
                                        "rewrite_evpn_rt_asn": {
                                            "type": "bool"
                                        },
                                        "route_map": {
                                            "type": "dict",
                                            "options": {
                                                "in": {"type": "str"},
                                                "out": {"type": "str"},
                                            },
                                        },
                                        "route_reflector_client": {
                                            "type": "bool"
                                        },
                                        "send_community": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "extended": {"type": "bool"},
                                                "standard": {"type": "bool"},
                                                "both": {"type": "bool"},
                                            },
                                        },
                                        "soft_reconfiguration_inbound": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "always": {"type": "bool"},
                                            },
                                        },
                                        "soo": {"type": "str"},
                                        "suppress_inactive": {"type": "bool"},
                                        "unsuppress_map": {"type": "str"},
                                        "weight": {"type": "int"},
                                    },
                                },
                            },
                        },
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
                "parsed",
                "gathered",
                "rendered",
            ],
            "default": "merged",
        },
    }  # pylint: disable=C0301
