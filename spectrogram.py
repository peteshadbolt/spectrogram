#!/usr/bin/python
import numpy as np
import matplotlib.image as mpimg
import wave
from array import array
from progressbar import ProgressBar

def write_column(output_file, pixels, rescale=.1):
    """ Write a single column of sound """
    curve = np.fft.ifft(pixels, len(pixels)*2).real
    curve = np.array((curve-np.average(curve))*rescale, dtype=int)
    data = array("h", curve).tostring()
    output_file.writeframes(data)


def make_wav(image_filename):
    """ Make a WAV file having a spectrogram resembling an image """
    image = mpimg.imread(image_filename)
    image = np.sum(image, axis = 2).T[:, ::-1]
    image = image**2

    output_file = wave.open(image_filename+".wav", "w")
    output_file.setparams((1, 2, 44100, 0, "NONE", "not compressed"))

    pb = ProgressBar().start()
    n = float(len(image))
    for index, column in enumerate(image):
        write_column(output_file, column)
        pb.update(index*100/n)

    output_file.close()
    print "Wrote %s.wav" % image_filename


if __name__ == "__main__":
    import sys
    make_wav(sys.argv[1])

