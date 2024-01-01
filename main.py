import numpy as np
import scipy
from scipy.io import wavfile

from note import Note, Rest
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

    voices[0].append(Rest(2))
    scrambled = [_set[1], _set[3], _set[2], _set[0]]
    for i in range(3):
        for freq in scrambled:
            voices[0].append(Note(freq, 2/3, "tri", 0.5))
        voices[0].append(Rest(1+1/3))
        for freq in transpose(scrambled, (6+i)/5):
            voices[0].append(Note(freq, 1/3, "saw", 0.1))
        voices[0].append(Rest(1+2/3))
    voices[0].append(Rest(1))
    voices[0].append(Note(_set[1]*2, 2, "tri", 0.5))
    voices[0].append(Rest(30))
    for i in range(4):
        voices[0].append(Note(_set[(i+1)%4]*2, 0.25, "tri", 0.5))
        voices[0].append(Rest(0.75))
    for i in range(6):
        for freq in transpose_to(_set, _set[i%4]):
            voices[0].append(Note(freq, 1/6, "saw", 0.3))

    for j in range(10):
        voices[0].append(Note(_set[2]*2, 0.08, "saw", 0.8))
        voices[0].append(Rest(0.02))

    voices[0].append(Rest(3))
    for i in range(3):
        voices[0].append(Note(_set[0], 1, "sin", 0.1))
        voices[0].append(Rest(2))

    for i in range(32):
        for freq in transpose_to(invert(_set), _set[i%len(_set)]):
            voices[1].append(Note(freq, 4/(i+1), "sin", 0.5))

    for i in range(2):
        for freq in transpose(_set, 3/8):
            voices[2].append(Note(freq, 1.5, "sin", 0.2))
        for j in range(3):
            voices[2].append(Rest(1))
            voices[2].append(Note(_set[0]*2/3, 0.75, "sin", 0.4))
            voices[2].append(Rest(0.25))
    for i in range(4):
        voices[2].append(Note(invert(_set)[i]/2, 7.5, "tri", 0.7))
        voices[2].append(Rest(0.5))

    for i in range(4):
        voices[2].append(Note(_set[i], 0.25, "tri", 0.5))
        voices[2].append(Rest(0.75))
    for i in range(4):
        for j in range(9):
            voices[2].append(Note(scrambled[i], 0.08, "tri", 0.8))
            voices[2].append(Rest(0.02))
        voices[2].append(Rest(0.1))

    for j in range(20):
        voices[2].append(Note(_set[0], 0.04, "tri", 0.8))
        voices[2].append(Rest(0.01))
    produce(voices, _mvt_name)


def produce(_voices, _mvt_name):
    """
    Writes a list of voices into wav files
    :param _voices: a list of voices
    :param _mvt_name: the name of the exported wav files
    """
    for i in range(len(_voices)):
        for j in range(len(_voices[i])):
            _voices[i][j] = _voices[i][j].create_signal()

        if _voices[i]:
            _voices[i] = np.concatenate(_voices[i])
        else:
            _voices[i] = np.array(_voices[i])
        print(type(_voices[i]))
        write_wav(_voices[i], _mvt_name + "-voice-" + str(i))


# test: [400, 500, 650, 700]

# rand0: [432, 610, 748, 418]
# harm0: [420, 490, 560, 630]
# dsch: [293.7, 311.2, 261.7, 247]

# rand1: [555, 577, 655, 733]
compose_variations(invert([293.7, 311.2, 261.7, 247]), "mvt2")
