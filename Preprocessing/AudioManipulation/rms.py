import glob
from random import random
import os
from pydub import AudioSegment
import numpy as np

def rms_of_file(sound):
    sound = AudioSegment.from_file("C:\\Users\\johan\\DL4AED\\processed_data\\Segment_speech\\" + sound)
    # audio = silence.split_on_silence(sound,min_silence_len=0,silence_thresh=-30,keep_silence=0)
    return sound.dBFS


# TODO: implement a threshhold to calc avrg_speech_rms without silence
def calc_avarage_rms(path):
    path_elements = os.listdir(path)
    average = 0
    for sound in path_elements:
        average += rms_of_file(sound)
    return average / len(path)


def adjust_noise(path, average,dest):
    path_elements = os.listdir(path)
    for sound_name in path_elements:
        sound = AudioSegment.from_file(path + sound_name)
        #dont know how tooverwrite the old wav file
        #TODO: check if the sound lands in the directory
        match_target_amplitude(sound, average)



def match_target_amplitude(sound, target_dBFS):
    rand = np.random.normal(loc=1.0, scale=.5, size=None)
    change_in_dBFS = rand * target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)
