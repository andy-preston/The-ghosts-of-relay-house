#!/bin/python

from os import system

low_frequency = 20.0
high_frequency = 20000.0
band_width = (high_frequency - low_frequency) / 10.0

mid_point = low_frequency
while mid_point < high_frequency:
    filename = '--'.join([
        'grh',
        f'{str(mid_point).replace('.', '-')}',
        f'{str(band_width).replace('.', '-')}',
    ])
    command = ' '.join([
        'sox',
        '/home/andyp/Dropbox/my-stuff/the-ghosts-of-relay-house/ghosts-of-relay-house-small.flac',
        f'{filename}.wav',
        'bandpass',
        f'{mid_point}',
        f'{band_width}',
    ])
    print(command)
    system(command)
    mid_point = mid_point + band_width
