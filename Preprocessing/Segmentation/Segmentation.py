import numpy as np
import glob
import shutil
import tensorflow as tf
from pydub import AudioSegment, effects
from pydub.utils import make_chunks
import librosa
import re
import os
import random
import shutil
from librosa import display
from pathlib import Path
import IPython.display as pd
import matplotlib.pyplot as plt
from Segmentation_tools import move_random_files, segmentation_wav


def segmentation():
    # select random noise files and segment them
    noise_source = "datasets/noise"
    random_noise_path = "processed_data/random_noise"
    noise_files_no = 31000  # Noise Files with 10s Duration ~ 10GB
    noise_prefix = "noise"
    move_random_files(noise_source, random_noise_path, noise_files_no, noise_prefix)

    seg_noise_path = "processed_data/Segment_noise"
    length_ms = 1000
    noise_seg_size = 10
    segmentation_wav(random_noise_path, seg_noise_path, length_ms, noise_seg_size)

    # select random speech files and segment them
    speech_source = "datasets/clean/read_speech"
    random_speech_path = "processed_data/random_speech"
    speech_files = 10000  # Speech Files with 30s Duration ~ 10GB
    speech_prefix = "speech"
    move_random_files(speech_source, random_speech_path, speech_files, speech_prefix)

    seg_speech_path = "processed_data/Segment_speech"
    speech_seg_size = 30
    segmentation_wav(random_speech_path, seg_speech_path, length_ms, speech_seg_size)


