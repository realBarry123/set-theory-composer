
import numpy as np
import scipy
from scipy.io import wavfile

# sample rate
FS = 44100
PI = np.pi

class Note:
    def __init__(self, _freq, _dur, _type, _amp):
        self.freq = _freq
        self.dur = _dur
        self.type = _type
        self.amp = _amp
    def create_signal(self):
        samples = np.linspace(0, self.dur, int(FS * self.dur), endpoint=False)

        if self.type == "sin":
            sig = np.sin(2 * PI * self.freq * samples)

        elif self.type == "square":
            sig = scipy.signal.square(2 * PI * self.freq * samples)

        elif self.type == "triangle":
            sig = scipy.signal.sawtooth(2 * PI * self.freq * samples, 0.5)

        elif self.type == "sawtooth":
            sig = scipy.signal.sawtooth(2 * PI * self.freq * samples, 1)

        else:
            raise Exception("wave type not recognized")

        sig *= 32767
        sig = np.int16(sig)

        return sig