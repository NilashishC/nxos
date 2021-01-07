# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The nxos bgp_global fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.rm_templates.bgp_global import (
    Bgp_globalTemplate,
)
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.argspec.bgp_global.bgp_global import (
    Bgp_globalArgs,
)

import q
class Bgp_globalFacts(object):
    """ The nxos bgp_global facts class
    """

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Bgp_globalArgs.argument_spec

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for Bgp_global network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        objs = []

        if not data:
            data = connection.get(
                "show running-config | section '^router bgp'"
            )

        # parse native config using the Bgp_global template
        bgp_global_parser = Bgp_globalTemplate(lines=data.splitlines())
        objs = bgp_global_parser.parse()

        ansible_facts["ansible_network_resources"].pop("bgp_global", None)

        params = utils.remove_empties(
            utils.validate_config(self.argument_spec, {"config": objs})
        )

        facts["bgp_global"] = params["config"]
        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts