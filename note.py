"""
Contains class Note and subclass Rest
"""

import numpy as np
import scipy

# sample rate
FS = 44100
PI = np.pi


class Note:
    """
    An object representing a note with a frequency, duration, wave type, and amplitude
    """
    def __init__(self, _freq, _dur, _type, _amp):
        self.freq = _freq
        self.dur = _dur
        self.type = _type
        self.amp = _amp

    def create_signal(self):
        """
        Creates a signal from the note
        :return: signal in np array form
        """
        samples = np.linspace(0, self.dur, int(FS * self.dur), endpoint=False)

        if self.type == "sin":
            sig = np.sin(2 * PI * self.freq * samples)

        elif self.type == "sqr":
            sig = scipy.signal.square(2 * PI * self.freq * samples)

        elif self.type == "tri":
            sig = scipy.signal.sawtooth(2 * PI * self.freq * samples, 0.5)

        elif self.type == "saw":
            sig = scipy.signal.sawtooth(2 * PI * self.freq * samples, 1)

        else:
            raise Exception("wave type not recognized")

        sig *= 32767
        sig *= self.amp
        sig = np.int16(sig)

        return sig


class Rest(Note):
    """
    An object representing a rest of a given duration
    """
    def __init__(self, _dur):
        super().__init__(0, _dur, "sin", 0)
