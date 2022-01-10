import time
import uuid
from random import randint


class Utils:
    @staticmethod
    def create_uuid():
        return uuid.uuid1().__str__().replace('-', '')

    @staticmethod
    def millis():
        return int(round(time.time() * 1000))

    @staticmethod
    def create_uuid_int():
        return '{}{}'.format(Utils.millis(), randint(1000, 9999))
