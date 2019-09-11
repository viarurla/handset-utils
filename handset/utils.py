import re
from random import randint

from fonoapi import FonoAPI

from . import common, database

version_regex = re.compile(r'\d+(\.\d+)+')
os_name = re.compile(r'.+?(?= )')


class SimCard:
    def __init__(self):
        # Currently hardcoded for UK numbers during these early stages
        self.msisdn = '447' + common.randint_length(9)
        self.sim_serial = common.randint_length(17)
        self.imsi = common.randint_length(12)


class Handset(SimCard):
    def __init__(self, token=None, data_source=None, handset=None, brand=""):
        super().__init__()

        if data_source is not None:
            try:
                handset = database.select_random_handset(path_to_db=data_source)
            except:
                raise ValueError('No data source or fonoapi token provided')
        elif token is not None:
            try:
                fon = FonoAPI(token)
                handset_list = fon.getlatest(brand=brand).devices
                handset = handset_list[randint(0, len(handset_list) - 1)]
            except:
                raise ValueError('Error retrieving handset info using fonoapi token, check the token is valid!')
        else:
            raise ValueError('No data source or fonoapi token provided')

        if handset is not None:
            self.brand = handset['Brand']
            self.device_name = handset['DeviceName']
            self.imei = common.randint_length(13)
            try:
                self.platform = os_name.search(handset['os']).group(0)
            except:
                self.platform = 'unknown'
            try:
                self.os_version = version_regex.search(handset['os']).group(0)
            except:
                self.os_version = '4.0.4'
