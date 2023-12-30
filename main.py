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
        voices[0].append(Note(freq, 1, "sin", 0.5))

    for freq in invert(_set):
        voices[1].append(Note(freq, 1, "sin", 0.5))

    for freq in transpose(_set, 2):
        voices[2].append(Note(freq, 1, "sin", 0.5))

    # create signals and concat
    for i in range(len(voices)):
        for j in range(len(voices[i])):
            voices[i][j] = voices[i][j].create_signal()

        if voices[i]:
            voices[i] = np.concatenate(voices[i])
        else:
            voices[i] = np.array(voices[i])
        print(type(voices[i]))
        write_wav(voices[i], _mvt_name + "-voice-" + str(i))


compose_variations([400, 500, 650, 700], "test")
