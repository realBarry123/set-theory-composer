"""
Functions that perform various operations on a list on numbers (hz)
"""


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


def transpose_to(_set, _freq):
    """
    Transposes a list of frequencies
    :param _set: a list of frequencies
    :param _freq: target frequency for the first note
    :return: the transposed list
    """
    multiplier = _freq/_set[0]
    new_set = _set.copy()
    for i in range(len(new_set)):
        new_set[i] *= multiplier
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
