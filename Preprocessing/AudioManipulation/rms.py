import glob
import pydub

import os
from pydub import AudioSegment,silence

def rms_of_file(sound):
    sound = AudioSegment.from_file("C:\\Users\\johan\\DL4AED\\processed_data\\random_speech\\"+sound)
    audio = sound.silence.split_on_silence(min_silence_len=0,silence_thresh=-20,keep_silence=0)
    return None


def calc_avarage_rms():
    path = os.listdir("C:\\Users\\johan\\DL4AED\\processed_data\\random_speech")
    avarage = 0
    for sound in path:
        avarage += rms_of_file(sound)
    print(avarage/len(path))