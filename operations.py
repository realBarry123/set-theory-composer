import numpy as np
import scipy
from scipy.io import wavfile


def retrograde(list):
    """
    Retrogrades a list of frequencies
    :param list: a list of frequencies
    :return: the retrograded list
    """
    return reversed(list)


def transpose(list, multiplier):
    """
    Transposes a list of frequencies
    :param list: a list of frequencies
    :param multiplier: multiplier applied to each frequency (e.g. 2 for an octave)
    :return: the transposed list
    """
    for i in range(len(list)):
        list[i].freq *= multiplier
    return list


def invert(list):
    """
    Inverts a list of frequencies
    :param list: a list of frequencies
    :return: the inverted list
    """
    pivot = list[0].freq

    for i in range(len(list)-1):
        list[i+1] *= list[i+1].freq/pivot
    return list

def normalize(list):
    pass