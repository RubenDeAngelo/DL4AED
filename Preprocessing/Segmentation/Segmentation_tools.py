import numpy as np
import glob
import shutil
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


def move_random_files(source: str, dest: str, files_no: int, name_prefix: str):
    for i in range(files_no):
        random_file = os.renames(random.choice(os.listdir(source)), name_prefix + str(i).zfill(5))
        source_file = "%s/%s" % (source, random_file)
        shutil.move(source_file, dest)


def segmentation_wav(source_path: str, dest_path: str, length_ms: int, seg_size: int):
    data_names = sorted(glob.glob(source_path))
    for m in range(0, len(data_names)):
        audio_data = AudioSegment.from_file(data_names[m], "wav")
        chunks = make_chunks(audio_data, length_ms)
        file_path = os.path.splitext(data_names[m])[0]

        for i, chunk in enumerate(chunks):
            if i < seg_size:
                file_name = file_path.split('/')[-1] + '_' + str(i).zfill(2)
                segment_name = dest_path + file_name + ".wav"
                chunk.export(segment_name, format="wav")
