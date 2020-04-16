#
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The arg spec for the nxos_ospfv2 module
"""


class Ospfv2Args(object):  # pylint: disable=R0903
    """The arg spec for the nxos_ospfv2 module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "running_config": {"type": "str"},
        "config": {
            "options": {
                "processes": {
                    "elements": "dict",
                    "options": {
                        "areas": {
                            "required_one_of": [['authentication', 'default_cost', 'filter_list',\
                                        'nssa', 'ranges', 'stub']],
                            "elements": "dict",
                            "options": {
                                "area_id": {"type": "str"},
                                "authentication": {
                                    "options": {
                                        "message_digest": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                                "default_cost": {"type": "int"},
                                "filter_list": {
                                    "options": {
                                        "direction": {
                                            "choices": ["in", "out"],
                                            "type": "str",
                                            "required": True
                                        },
                                        "route_map": {"type": "str", "required": True},
                                    },
                                    "type": "list",
                                    "elements": "dict"
                                },
                                "nssa": {
                                    "options": {
                                        "default_information_originate": {"type": "bool"},
                                        "no_redistribution": {"type": "bool"},
                                        "no_summary": {"type": "bool"},
                                        "set": {"type": "bool"},
                                        "translate": {
                                            "options": {
                                                "type7": {
                                                    "mutually_exclusive": [
                                                        ["always", "never"]
                                                    ],
                                                    "options": {
                                                        "always": {"type": "bool"},
                                                        "never": {"type": "bool"},
                                                        "supress_fa": {"type": "bool"},
                                                    },
                                                    "type": "dict",
                                                }
                                            },
                                            "type": "dict",
                                        },
                                    },
                                    "type": "dict",
                                },
                                "ranges": {
                                    "elements": "dict",
                                    "options": {
                                        "cost": {"type": "int"},
                                        "not_advertise": {"type": "bool"},
                                        "prefix": {"type": "str", "required": True},
                                    },
                                    "type": "list",
                                },
                                "stub": {
                                    "options": {
                                        "no_summary": {"type": "bool"},
                                        "set": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                            },
                            "type": "list",
                        },
                        "auto_cost": {
                            "options": {
                                "reference_bandwidth": {"type": "int", "required": True},
                                "unit": {"choices": ["Gbps", "Mbps"], "type": "str"},
                                "required": True,
                            },
                            "type": "dict",
                        },
                        "default_information": {
                            "options": {
                                "originate": {
                                    "options": {
                                        "always": {"type": "bool"},
                                        "route_map": {"type": "str"},
                                        "set": {"type": "bool"},
                                    },
                                    "type": "dict",
                                }
                            },
                            "type": "dict",
                        },
                        "default_metric": {"type": "str"},
                        "distance": {"type": "int"},
                        "flush_routes": {"type": "bool"},
                        "graceful_restart": {
                            "options": {
                                "planned_only": {"type": "bool"},
                                "helper_disable": {"type": "bool"},
                                "set": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "isolate": {"type": "bool"},
                        "log_adjacency_changes": {
                            "options": {
                                "detail": {"type": "bool"},
                                "log": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "max_lsa": {
                            "options": {
                                "ignore_count": {"type": "int"},
                                "ignore_time": {"type": "int"},
                                "max_non_self_generated_lsa": {"type": "int", "required": True},
                                "reset_time": {"type": "int"},
                                "threshold": {"type": "int"},
                                "warning_only": {"type": "bool"},
                            },
                            "type": "dict",
                        },
                        "max_metric": {
                            "options": {
                                "router_lsa": {
                                    "options": {
                                        "external_lsa": {
                                            "options": {
                                                "max_metric_value": {"type": "int"},
                                                "set": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        },
                                        "include_stub": {"type": "bool"},
                                        "on_startup": {
                                            "options": {
                                                "set": {"type": "bool"},
                                                "wait_for_bgp_asn": {"type": "int"},
                                                "wait_period": {"type": "int"},
                                            },
                                            "type": "dict",
                                        },
                                        "set": {"type": "bool"},
                                        "summary_lsa": {
                                            "options": {
                                                "max_metric_value": {"type": "int"},
                                                "set": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        },
                                    },
                                    "type": "dict",
                                }
                            },
                            "type": "dict",
                        },
                        "maximum_paths": {"type": "int"},
                        "mpls": {
                            "options": {
                                "traffic_eng": {
                                    "options": {
                                        "areas": {
                                            "type": "list",
                                            "elements": "dict",
                                            "options": {
                                                "area_id": {"type": "str"},
                                            }
                                        },
                                        "multicast_intact": {"type": "bool"},
                                        "router_id": {"type": "str"},
                                    },
                                    "type": "dict",
                                }
                            },
                            "type": "dict",
                        },
                        "name_lookup": {"type": "bool"},
                        "passive_interface": {
                            "options": {"default": {"type": "bool"}},
                            "type": "dict",
                        },
                        "process_id": {"required": True, "type": "str"},
                        "redistribute": {
                            "elements": "dict",
                            "options": {
                                "id": {"type": "str"},
                                "protocol": {
                                    "choices": [
                                        "bgp",
                                        "direct",
                                        "eigrp",
                                        "isis",
                                        "lisp",
                                        "ospf",
                                        "rip",
                                        "static",
                                    ],
                                    "required": True,
                                    "type": "str",
                                },
                                "route_map": {"type": "str", "required": True},
                            },
                            "type": "list",
                        },
                        "rfc1583compatibility": {"type": "bool"},
                        "router_id": {"type": "str"},
                        "shutdown": {"type": "bool"},
                        "summary_address": {
                            "elements": "dict",
                            "mutually_exclusive": [['not_advertise', 'tag']],
                            "options": {
                                "not_advertise": {"type": "bool"},
                                "prefix": {"type": "str", "required": True},
                                "tag": {"type": "int"},
                            },
                            "type": "list",
                        },
                        "table_map": {
                            "options": {
                                "filter": {"type": "bool"},
                                "name": {"type": "str", "required": True},
                            },
                            "type": "dict",
                        },
                        "timers": {
                            "options": {
                                "lsa_arrival": {"type": "int"},
                                "lsa_group_pacing": {"type": "int"},
                                "throttle": {
                                    "options": {
                                        "lsa": {
                                            "options": {
                                                "hold_interval": {"type": "int"},
                                                "max_interval": {"type": "int"},
                                                "start_interval": {"type": "int"},
                                            },
                                            "type": "dict",
                                        },
                                        "spf": {
                                            "options": {
                                                "initial_spf_delay": {"type": "int"},
                                                "max_wait_time": {"type": "int"},
                                                "min_hold_time": {"type": "int"},
                                            },
                                            "type": "dict",
                                        },
                                    },
                                    "type": "dict",
                                },
                            },
                            "type": "dict",
                        },
                        "vrfs": {
                            "elements": "dict",
                            "options": {
                                "down_bit_ignore": {"type": "bool"},
                                "capability": {
                                    "type": "dict",
                                    "options": {
                                        "vrf_lite": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "evpn": {"type": "bool"}
                                            }
                                        }
                                    }
                                },
                                "areas": {
                                    "required_one_of": [['authentication', 'default_cost', 'filter_list',\
                                        'nssa', 'ranges', 'stub']],
                                    "elements": "dict",
                                    "options": {
                                        "area_id": {"type": "str"},
                                        "authentication": {
                                            "options": {
                                                "message_digest": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        },
                                        "default_cost": {"type": "int"},
                                        "filter_list": {
                                            "options": {
                                                "direction": {
                                                    "choices": ["in", "out"],
                                                    "type": "str",
                                                    "required": True
                                                },
                                                "route_map": {"type": "str", "required": True},
                                            },
                                            "type": "list",
                                            "elements": "dict"
                                        },
                                        "nssa": {
                                            "options": {
                                                "default_information_originate": {
                                                    "type": "bool"
                                                },
                                                "no_redistribution": {"type": "bool"},
                                                "no_summary": {"type": "bool"},
                                                "set": {"type": "bool"},
                                                "translate": {
                                                    "options": {
                                                        "type7": {
                                                            "mutually_exclusive": [
                                                                ["always", "never"]
                                                            ],
                                                            "options": {
                                                                "always": {
                                                                    "type": "bool"
                                                                },
                                                                "never": {
                                                                    "type": "bool"
                                                                },
                                                                "supress_fa": {
                                                                    "type": "bool"
                                                                },
                                                            },
                                                            "type": "dict",
                                                        }
                                                    },
                                                    "type": "dict",
                                                },
                                            },
                                            "type": "dict",
                                        },
                                        "ranges": {
                                            "elements": "dict",
                                            "options": {
                                                "cost": {"type": "int"},
                                                "not_advertise": {"type": "bool"},
                                                "prefix": {"type": "str", "required": True},
                                            },
                                            "type": "list",
                                        },
                                        "stub": {
                                            "options": {
                                                "no_summary": {"type": "bool"},
                                                "set": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        },
                                    },
                                    "type": "list",
                                },
                                "auto_cost": {
                                    "options": {
                                        "reference_bandwidth": {"type": "int", "required": True},
                                        "unit": {
                                            "choices": ["Gbps", "Mbps"],
                                            "type": "str",
                                            "required": True,
                                        },
                                    },
                                    "type": "dict",
                                },
                                "default_information": {
                                    "options": {
                                        "originate": {
                                            "options": {
                                                "always": {"type": "bool"},
                                                "route_map": {"type": "str"},
                                                "set": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        }
                                    },
                                    "type": "dict",
                                },
                                "default_metric": {"type": "int"},
                                "distance": {"type": "int"},
                                "graceful_restart": {
                                    "options": {
                                        "planned_only": {"type": "boot"},
                                        "helper_disable": {"type": "bool"},
                                        "set": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                                "log_adjacency_changes": {
                                    "options": {
                                        "detail": {"type": "bool"},
                                        "log": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                                "max_lsa": {
                                    "options": {
                                        "ignore_count": {"type": "int"},
                                        "ignore_time": {"type": "int"},
                                        "max_non_self_generated_lsa": {"type": "int", "required": True},
                                        "reset_time": {"type": "int"},
                                        "threshold": {"type": "int"},
                                        "warning_only": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                                "max_metric": {
                                    "options": {
                                        "router_lsa": {
                                            "options": {
                                                "external_lsa": {
                                                    "options": {
                                                        "max_metric_value": {
                                                            "type": "int"
                                                        },
                                                        "set": {"type": "bool"},
                                                    },
                                                    "type": "dict",
                                                },
                                                "include_stub": {"type": "bool"},
                                                "on_startup": {
                                                    "options": {
                                                        "set": {"type": "bool"},
                                                        "wait_for_bgp_asn": {
                                                            "type": "int"
                                                        },
                                                        "wait_period": {"type": "int"},
                                                    },
                                                    "type": "dict",
                                                },
                                                "set": {"type": "bool"},
                                                "summary_lsa": {
                                                    "options": {
                                                        "max_metric_value": {
                                                            "type": "int"
                                                        },
                                                        "set": {"type": "bool"},
                                                    },
                                                    "type": "dict",
                                                },
                                            },
                                            "type": "dict",
                                        }
                                    },
                                    "type": "dict",
                                },
                                "maximum_paths": {"type": "int"},
                                "name_lookup": {"type": "bool"},
                                "passive_interface": {
                                    "options": {"default": {"type": "bool"}},
                                    "type": "dict",
                                },
                                "redistribute": {
                                    "elements": "dict",
                                    "options": {
                                        "id": {"type": "str"},
                                        "protocol": {
                                            "choices": [
                                                "bgp",
                                                "direct",
                                                "eigrp",
                                                "isis",
                                                "lisp",
                                                "ospf",
                                                "rip",
                                                "static",
                                            ],
                                            "required": True,
                                            "type": "str",
                                        },
                                        "route_map": {"type": "str", "required": True},
                                    },
                                    "type": "list",
                                },
                                "rfc1583compatibility": {"type": "bool"},
                                "router_id": {"type": "str"},
                                "shutdown": {"type": "bool"},
                                "summary_address": {
                                    "elements": "dict",
                                    "options": {
                                        "not_advertise": {"type": "bool"},
                                        "prefix": {"type": "str", "required": True},
                                        "tag": {"type": "int"},
                                    },
                                    "type": "list",
                                },
                                "table_map": {
                                    "options": {
                                        "filter": {"type": "bool"},
                                        "name": {"type": "str", "required": True},
                                    },
                                    "type": "dict",
                                },
                                "timers": {
                                    "options": {
                                        "lsa_arrival": {"type": "int"},
                                        "lsa_group_pacing": {"type": "int"},
                                        "throttle": {
                                            "options": {
                                                "lsa": {
                                                    "options": {
                                                        "hold_interval": {
                                                            "type": "int"
                                                        },
                                                        "max_interval": {"type": "int"},
                                                        "start_interval": {
                                                            "type": "int"
                                                        },
                                                    },
                                                    "type": "dict",
                                                },
                                                "spf": {
                                                    "options": {
                                                        "initial_spf_delay": {
                                                            "type": "int"
                                                        },
                                                        "max_wait_time": {
                                                            "type": "int"
                                                        },
                                                        "min_hold_time": {
                                                            "type": "int"
                                                        },
                                                    },
                                                    "type": "dict",
                                                },
                                            },
                                            "type": "dict",
                                        },
                                    },
                                    "type": "dict",
                                },
                                "vrf": {"required": True, "type": "str"},
                            },
                            "type": "list",
                        },
                    },
                    "type": "list",
                }
            },
            "type": "dict",
        },
        "state": {
            "choices": ["merged", "replaced", "overridden", "deleted", "gathered", "rendered", "parsed"],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
