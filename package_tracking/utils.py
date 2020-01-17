from enum import Enum


class CarrierService(Enum):
    UPS = 'UPS'
    USPS = 'USPS'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]