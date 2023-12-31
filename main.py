import numpy as np
import scipy
from scipy.io import wavfile

from note import Note
from operations import *

# sample rate
FS = 44100


def write_wav(_sig, _name):
    """
    Writes a signal as a wav file
    :param _sig: np array of signal
    :param _name: name of the wav file
    """
    wavfile.write(str(_name + ".wav"), FS, _sig)


def compose_variations(_set, _mvt_name):
    """
    Composes a movement based on the provided frequency set and writes as 3 wav files
    :param _set: the frequency set used in the composition
    """
    voices = [[], [], []]
    for freq in _set:
        voices[0].append(Note(freq, freq/500, "sin", 0.5))

    for i in range(len(_set)):
        for freq in transpose_to(invert(_set), _set[i]):
            voices[1].append(Note(freq, freq/500, "sin", 0.5))

    for freq in transpose(_set, 2):
        voices[2].append(Note(freq, freq/500, "sin", 0.3))

    produce(voices, _mvt_name)


def produce(_voices, _mvt_name):
    for i in range(len(_voices)):
        for j in range(len(_voices[i])):
            _voices[i][j] = _voices[i][j].create_signal()

        if _voices[i]:
            _voices[i] = np.concatenate(_voices[i])
        else:
            _voices[i] = np.array(_voices[i])
        print(type(_voices[i]))
        write_wav(_voices[i], _mvt_name + "-voice-" + str(i))

compose_variations([400, 500, 650, 700], "test")
