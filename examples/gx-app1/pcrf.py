# -*- coding: utf-8 -*-
"""
    examples.pcrf
    ~~~~~~~~~~~~~~~~~~~~~

    This module contains an example on how to setup a dummy MME
	by using the Bromelia class features of bromelia library.

    :copyright: (c) 2024 Daniel Bültmann
    :license: MIT, see LICENSE for more details.
"""

import os
import sys

basedir = os.path.dirname(os.path.abspath(__file__))
examples_dir = os.path.dirname(basedir)
bromelia_dir = os.path.dirname(examples_dir)

sys.path.insert(0, bromelia_dir)

from bromelia import Bromelia
from bromelia.avps import *
from bromelia.constants import *
from bromelia.lib.etsi_3gpp_gx import CCR, CCA
from bromelia.lib.etsi_3gpp_rx import RAR, RAA

#: Application initialization
config_file = os.path.join(basedir, "pcrf_config.yaml")
print(config_file)
app = Bromelia(config_file=config_file)
app.load_messages_into_application_id([CCR, CCA], DIAMETER_APPLICATION_Gx)
app.load_messages_into_application_id([RAR, RAA], DIAMETER_APPLICATION_Rx)

CCA = app.gx.CCA  #: Creating CCA alias


@app.route(application_id=DIAMETER_APPLICATION_Gx, command_code=CC_MESSAGE)
def ccr(request):
    print("Got CCR")

    usage_monitoring_key = UsageMonitoringKeyAVP("5150")
    usage_monitoring_level = UsageMonitoringLevelAVP(SESSION_LEVEL)
    granted_service_units = GrantedServiceUnitAVP([CcTotalOctetsAVP(100000000)])

    attrs = {
        "result_code" : DIAMETER_SUCCESS,
        "usage_monitoring_information": [usage_monitoring_key, usage_monitoring_level, granted_service_units]
    }

    return CCA(**attrs)


if __name__ == "__main__":
    app.run()  #: It will be blocked until connection has been established
