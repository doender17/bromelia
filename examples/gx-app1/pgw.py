# -*- coding: utf-8 -*-
"""
    pgw
    ~~~

    This module contains an example on how to setup a dummy HSS
	by using the Bromelia class features of bromelia library.
    
    :copyright: (c) 2024 Daniel Bültmann.
    :license: MIT, see LICENSE for more details.
"""

import os
import sys

basedir = os.path.dirname(os.path.abspath(__file__))
examples_dir = os.path.dirname(basedir)
bromelia_dir = os.path.dirname(examples_dir)

sys.path.insert(0, bromelia_dir)

import bromelia.lib.etsi_3gpp_gx

basedir = os.path.dirname(os.path.abspath(__file__))
examples_dir = os.path.dirname(basedir)
bromelia_dir = os.path.dirname(examples_dir)

sys.path.insert(0, bromelia_dir)

from bromelia import Bromelia
from bromelia.avps import *
from bromelia.constants import *
from bromelia.lib.etsi_3gpp_s6a import *
from bromelia.lib.etsi_3gpp_gx import CCR, CCA

#: Application initialization 
config_file = os.path.join(basedir, "pgw_config.yaml")

app = Bromelia(config_file=config_file)
app.load_messages_into_application_id([CCR, CCA], DIAMETER_APPLICATION_Gx)

CCR = app.gx.CCR  #: Creating CCR alias

if __name__ == "__main__":
    app.run()   #: It will be blocked until connection has been established

    subscriptionMSISDNIdData = SubscriptionIdDataAVP("49157700000001")
    subscriptionMSISDNIdType = SubscriptionIdTypeAVP(END_USER_E164)
    subscriptionIMSIIdData = SubscriptionIdDataAVP("262200000000001")
    subscriptionIMSIIdType = SubscriptionIdTypeAVP(END_USER_E164)
    attrs = {
        "origin_state_id" : OriginStateIdAVP(data=1),
        "framed_ip_addr" : FramedIpAddressAVP("100.127.254.17"),
    }

    ccr = CCR(**attrs)
    ccr.append(SubscriptionIdAVP([subscriptionIMSIIdType, subscriptionIMSIIdData]))
    ccr.append(SubscriptionIdAVP([subscriptionMSISDNIdType, subscriptionMSISDNIdData]))
    cca = app.send_message(ccr)
