"""
Strategies are given the following input:
* history ... a list of the past action the other player took.
and returns 0 (coorporative) or 1 (defective) action.
"""
from random import choice


COORPERATIVE_ACT = 0
DEFECTIVE_ACT = 1
ALL_ACT = [COORPERATIVE_ACT, DEFECTIVE_ACT]


def tit_for_tat(history):
    """
    TIT FOR TAT simply does whatever the other player did on the preceding move.
    """
    if history:
        return history[-1]
    return COORPERATIVE_ACT


def random(history):
    return choice(ALL_ACT)


def all_d(history):
    return DEFECTIVE_ACT


def all_c(history):
    return COORPERATIVE_ACT


def cd(history):
    if len(history) % 2 == 0:
        return COORPERATIVE_ACT
    else:
        return DEFECTIVE_ACT
