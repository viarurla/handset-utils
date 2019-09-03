import re
from random import randint

from fonoapi import FonoAPI

import common
import database

version_regex = re.compile(r'\d+(\.\d+)+')
os_name = re.compile(r'.+?(?= )')

class SimCard:
    def __init__(self):
        # Currently hardcoded for UK numbers during these early stages
        self.msisdn = '447' + common.randint_length(9)
        self.sim_serial = common.randint_length(17)
        self.imsi = common.randint_length(12)


class Handset(SimCard):
    def __init__(self):
        super().__init__()
        self.brand = None
        self.device_name = None
        self.imei = None
        self.platform = None
        self.os_version = None

    def from_database(self, path_to_db):
        # Must be SQLite3
        handset = database.select_random_handset(path_to_db=path_to_db)
        self.brand = handset['Brand']
        self.device_name = handset['DeviceName']
        self.imei = common.randint_length(13)
        self.platform = os_name.search(handset['os']).group(0)
        self.os_version = version_regex.search(handset['os']).group(0)

    def from_api(self, token, brand=""):
        fon = FonoAPI(token)
        handset_list = fon.getlatest(brand=brand).devices
        handset = handset_list[randint(0, len(handset_list))]
        self.brand = handset['Brand']
        self.device_name = handset['DeviceName']
        self.imei = common.randint_length(13)
        self.platform = os_name.search(handset['os']).group(0)
        self.os_version = version_regex.search(handset['os']).group(0)
