#!/usr/env/python3

import os
from subprocess import call

# this script fills folders generated by "arrange_by_folders.py" with insufficient pitches


def pitch_shift_lacking_semitones():
    for dir in os.listdir(script_dir + '/../generated_tunable/'):
        dir_path = script_dir + '/../generated_tunable/' + dir
        samples = [int(os.path.splitext(s)[0]) for s in os.listdir(dir_path)]
        for i in range(24, 108):
            if i not in samples:
                closest = min(samples, key=lambda x: abs(x - i))
                freq_factor = 2**((i - closest) / 12.0)
                cmd = 'rubberband "' + dir_path + '/' + str(closest) + '.wav" -T ' + str(freq_factor) + \
                      ' -f ' + str(freq_factor) + ' "' + dir_path + '/' + str(i) + '.wav"'
                print('huj ', cmd)
                call(cmd, shell=True)

pitch_shift_lacking_semitones()