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
cc_request_number = 0

def buildInitialCCR(imsi, msisdn, framedIP, apn, sgsn_mcc_mnc, type="I", session_id_avp = None):
    subscriptionMSISDNIdData = SubscriptionIdDataAVP(msisdn)
    subscriptionMSISDNIdType = SubscriptionIdTypeAVP(END_USER_E164)
    subscriptionIMSIIdData = SubscriptionIdDataAVP(imsi)
    subscriptionIMSIIdType = SubscriptionIdTypeAVP(END_USER_E164)
    global cc_request_number
    attrs = {
        "cc_request_number" : cc_request_number,
        "origin_state_id": 500,
        "framed_ip_addr": FramedIpAddressAVP(framedIP),
        "network_request_support": NETWORK_REQUEST_SUPPORTED,
        "ip_can_type": IP_CAN_TYPE_3GPP_EPS,
        "rat_type": RAT_TYPE_EUTRAN,
        "user_equipment_info": [UserEquipmentInfoTypeAVP(USER_EQUIPMENT_INFO_TYPE_IMEISV),
                                UserEquipmentInfoValueAVP("3507310119985311")],
        "qos_information": [ApnAggregateMaxBitrateUlAVP(128000000), ApnAggregateMaxBitrateDlAVP(128000000)],
        "default_eps_bearer_qos": [QosClassIdentifierAVP(QCI_9),
                                   AllocationRetentionPriorityAVP(
                                       [PriorityLevelAVP(9),
                                        PreEmptionCapabilityAVP(PRE_EMPTION_CAPABILITY_ENABLED),
                                        PreEmptionVulnerabilityAVP(PRE_EMPTION_VULNERABILITY_ENABLED)])],
        "x3gpp_sgsn_mcc_mnc": X3gppSgsnMccMncAVP(sgsn_mcc_mnc),
        "an_gw_address": "212.23.107.184",
        "x3gpp_user_location_info": X3gppUserLocationInfoAVP(b"\x82\x62\xf2\x30\x8c\xf0\x62\xf2\x30\x00\xef\xda\x34"),
        "x3gpp_ms_timezone": X3gppMsTimezoneAVP(b"\x80\x01"),
        "called_station_id": apn,
        "bearer_usage": BEARER_USAGE_GENERAL,
        "online": ONLINE_DISABLE_ONLINE,
        "offline": OFFLINE_DISABLE_OFFLINE,
        "origination_time_stamp": 3897470733113,
        "maximum_wait_time": 10000,
        "access_network_charging_address": "212.23.101.114",
        "access_network_charging_identifier": AccessNetworkChargingIdentifierGxAVP(
            [AccessNetworkChargingIdentifierValueAVP(b"\x01\x55\x55\x73")]),
    }

    if type=="U":
        attrs["cc_request_type"] = CC_REQUEST_TYPE_UPDATE_REQUEST

    if type=="T":
        attrs["cc_request_type"] = CC_REQUEST_TYPE_TERMINATION_REQUEST

    ccr = CCR(**attrs)
    ccr.append(SubscriptionIdAVP([subscriptionIMSIIdType, subscriptionIMSIIdData]))
    ccr.append(SubscriptionIdAVP([subscriptionMSISDNIdType, subscriptionMSISDNIdData]))
    ccr.append(SupportedFeaturesAVP([VendorIdAVP(VENDOR_ID_3GPP), FeatureListIdAVP(1), FeatureListAVP(8)]))
    ccr.append(SupportedFeaturesAVP([VendorIdAVP(VENDOR_ID_3GPP), FeatureListIdAVP(1), FeatureListAVP(16)]))
    if session_id_avp is not None:
        ccr.update_avp("session_id_avp", session_id_avp.data)

    cc_request_number += 1
    return ccr

if __name__ == "__main__":
    app.run(debug = True)   #: It will be blocked until connection has been established

    ccr = buildInitialCCR("4915775405009", "262200000000001", "100.127.254.17", "vip.onephone.de","26203")
    cca = app.send_message(ccr)
    ccr = buildInitialCCR("4915775405009", "262200000000001", "100.127.254.17", "vip.onephone.de", "26203", type="U", session_id_avp=cca.session_id_avp)
    cca = app.send_message(ccr)
    ccr = buildInitialCCR("4915775405009", "262200000000001", "100.127.254.17", "vip.onephone.de", "26203", type="T", session_id_avp=cca.session_id_avp)
    cca = app.send_message(ccr)
