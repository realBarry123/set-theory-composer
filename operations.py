import numpy as np
import scipy
from scipy.io import wavfile


def retrograde(_set):
    """
    Retrogrades a list of frequencies
    :param _set: a list of frequencies
    :return: the retrograded list
    """
    new_set = _set.copy()
    return reversed(new_set)


def transpose(_set, _multiplier):
    """
    Transposes a list of frequencies
    :param _set: a list of frequencies
    :param _multiplier: multiplier applied to each frequency (e.g. 2 for an octave)
    :return: the transposed list
    """
    new_set = _set.copy()
    for i in range(len(new_set)):
        new_set[i] *= _multiplier
    return new_set


def invert(_set):
    """
    Inverts a list of frequencies
    :param _set: a list of frequencies
    :return: the inverted list
    """
    new_set = _set.copy()
    pivot = new_set[0]

    for i in range(len(new_set) - 1):
        new_set[i + 1] = pivot/(new_set[i + 1] / pivot)
    return new_set


def normalize(_set):
    """
    Normalizes all frequencies in a given set to a range between 400 and 800 hz
    :param _set: a list of frequencies
    :return: a list of frequencies from 400-800
    """