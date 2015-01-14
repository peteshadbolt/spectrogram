#!/bin/bash
python spectrogram.py test.jpg
sox test.jpg.wav -n highpass 200 gain -l -2 spectrogram
