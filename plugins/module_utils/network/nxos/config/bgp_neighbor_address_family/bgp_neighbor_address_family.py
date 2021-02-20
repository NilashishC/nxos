#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The nxos_bgp_neighbor_address_family config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.resource_module import (
    ResourceModule,
)
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.facts.facts import (
    Facts,
)
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.rm_templates.bgp_neighbor_address_family import (
    Bgp_neighbor_address_familyTemplate,
)


class Bgp_neighbor_address_family(ResourceModule):
    """
    The nxos_bgp_neighbor_address_family config class
    """

    def __init__(self, module):
        super(Bgp_neighbor_address_family, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="bgp_neighbor_address_family",
            tmplt=Bgp_neighbor_address_familyTemplate(),
        )
        self.parsers = []

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """ Generate configuration commands to send based on
            want, have and desired state.
        """
        for entry in self.want, self.have:
            self._bgp_list_to_dict(entry)

        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            wantd = dict_merge(self.have, self.want)

        # if state is deleted, empty out wantd and set haved to wantd
        if self.state == "deleted":
            pass

        # remove superfluous config for overridden and deleted
        if self.state in ["overridden", "deleted"]:
            pass

        for k, want in iteritems(wantd):
            self._compare(want=want, have=self.have.pop(k, {}))

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Bgp_neighbor_address_family network resource.
        """
        self.compare(parsers=self.parsers, want=want, have=have)

    def _bgp_list_to_dict(self, data):
        if "neighbors" in data:
            for nbr in data["neighbors"]:
                if "address_family" in nbr:
                    nbr["address_family"] = {
                        (x["afi"], x.get("safi")): x
                        for x in nbr["address_family"]
                    }
            data["neighbors"] = {x["neighbor"]: x for x in data["neighbors"]}

        if "vrfs" in data:
            for vrf in data["vrfs"]:
                self._bgp_list_to_dict(vrf)
            data["vrfs"] = {x["vrf"]: x for x in data["vrfs"]}
