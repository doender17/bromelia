# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp.ts_129_061
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in ETSI TS 129 061.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ...base import DiameterAVP
from ...constants.etsi_3gpp.ts_129_061 import *
from ...types import *


class X3gppChargingCharacteristicsAVP(DiameterAVP, UTF8StringType):
    """Implementation of 3GPP-Charging-Characteristics AVP in Section 16.4.7.2 
    of ETSI TS 129 061 V10.11.0 (2014-10).

    The 3GPP-Charging-Characteristics AVP (AVP Code 13) is of type UTF8String.
    """
    code = X_3GPP_CHARGING_CHARACTERISTICS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             X3gppChargingCharacteristicsAVP.code,
                             X3gppChargingCharacteristicsAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)

class X3gppSgsnMccMncAVP(DiameterAVP, UTF8StringType):
    """Implementation of 3GPP-SGSN-MCC-MNC AVP in Section 16a5
    of ETSI TS 129 061 V17.06.0 (2022-05).

    The 3GPP-SGSN-MCC-MNC AVP (AVP Code 18) is of type UTF8String.
    """
    code = X_3GPP_SGSN_MCC_MNC_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             X3gppSgsnMccMncAVP.code,
                             X3gppSgsnMccMncAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)

class X3gppUserLocationInfoAVP(DiameterAVP, OctetStringType):
    """Implementation of 3GPP-User-LocationInfo AVP in Section 16a5
    of ETSI TS 129 061 V17.06.0 (2022-05).

    The User-Location-Info AVP (AVP Code 22) is of type UTF8String.
    """
    code = X_3GPP_USER_LOCAION_INFO_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             X3gppUserLocationInfoAVP.code,
                             X3gppUserLocationInfoAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)

class X3gppMsTimezoneAVP(DiameterAVP, OctetStringType):
    """Implementation of 3GPP-MS-Timezone AVP in Section 16a5
    of ETSI TS 129 061 V17.06.0 (2022-05).

    The MS-TimeZone AVP (AVP Code 23) is of type OctetString.
    """
    code = X_3GPP_MS_TIMEZONE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             X3gppMsTimezoneAVP.code,
                             X3gppMsTimezoneAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)
