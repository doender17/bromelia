# -*- coding: utf-8 -*-
"""
    bromelia.constants.etsi_3gpp.ts_129_061
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains constants defined in ETSI TS 129 061.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_4_bytes


#: Diameter AVPs
X_3GPP_CHARGING_CHARACTERISTICS_AVP_CODE = convert_to_4_bytes(13)
X_3GPP_SGSN_MCC_MNC_AVP_CODE = convert_to_4_bytes(18)
X_3GPP_USER_LOCAION_INFO_AVP_CODE = convert_to_4_bytes(22)
X_3GPP_MS_TIMEZONE_AVP_CODE = convert_to_4_bytes(23)