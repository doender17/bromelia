# -*- coding: utf-8 -*-
"""
    examples.bromelia_mme
    ~~~~~~~~~~~~~~~~~~~~~

    This module contains an example on how to setup a dummy MME
	by using the Bromelia class features of bromelia library.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

import os
import sys

basedir = os.path.dirname(os.path.abspath(__file__))
examples_dir = os.path.dirname(basedir)
bromelia_dir = os.path.dirname(examples_dir)

sys.path.insert(0, bromelia_dir)

from bromelia import Bromelia
from bromelia.constants import *
from bromelia.lib.etsi_3gpp_s6a import CLA # CancelLocationAnswer
from bromelia.lib.etsi_3gpp_s6a import CLR # CancelLocationRequest

#: Application initialization 
config_file = os.path.join(basedir, "bromelia_mme_config.yaml")

app = Bromelia(config_file=config_file)
app.load_messages_into_application_id([CLA, CLR], DIAMETER_APPLICATION_S6a)

CLA = app.s6a.CLA   #: Creating CLA alias

@app.route(application_id=DIAMETER_APPLICATION_S6a, command_code=CANCEL_LOCATION_MESSAGE)
def clr(request):
    return CLA(result_code=DIAMETER_SUCCESS)

if __name__ == "__main__":
    app.run()   #: It will be blocked until connection has been established
