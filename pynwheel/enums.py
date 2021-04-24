from enum import Enum


class ResponseTypes(Enum):
    employer = 1,
    platform = 2


class JobTypes(Enum):
    direct_deposit_switch = 1,
    direct_deposit_payment = 2,
    direct_deposit_allocations = 3,
    income = 4,
    employment = 5,
    identity = 6,
    paystubs = 7,
    shifts = 8
