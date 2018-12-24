# Helper functions, written by GL 12/2018
import easing
import sys
import time
import numpy as np
import wget
from math import log

class Interpolator():
    def __init__(self, fps=60.0):
        self.start = 0.0
        self.end = 0.0
        self.values = []
        self.duration = 1.0
        self.easing = None
        self.start = 0
        self.x = []
        self.fps = 1.0/fps
        self.start_time = None
        
    def animate(self, f, t, d):
        self.start = f
        self.end = t
        self.duration = d
        self.start_time = time.time()
        self.easing = easing.QuadEaseInOut(start=self.start, end=self.end, duration=self.duration)
        self.x = np.arange(0, 1, self.fps)
        self.values = list(map(self.easing.ease, self.x))
        
    def update(self):
        if (self.start_time is not None):
            # find index based on current time diff between start-time + duration
            diff = time.time() - self.start_time
            index = min(len(self.values)-1,int(diff / self.fps))
            return(self.values[index])
        return 0.0
        
def ratio_to_db(ratio, val2=None, using_amplitude=True):
    ratio = float(ratio)
    # accept 2 values and use the ratio of val1 to val2
    if val2 is not None:
        ratio = ratio / val2

    # special case for multiply-by-zero (convert to silence)
    if ratio == 0:
        return -float('inf')

    if using_amplitude:
        return 20 * log(ratio, 10)
    else:  # using power
        return 10 * log(ratio, 10)
        
def dbFS(rms, max_possible_amplitude=1.0):
    return ratio_to_db(rms / max_possible_amplitude)
    
def rangemap(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))