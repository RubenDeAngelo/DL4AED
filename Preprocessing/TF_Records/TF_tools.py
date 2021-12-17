import numpy as np
import tensorflow as tf

def create_tfrecord_from_wavs(wavs, output_file):
  with tf.python_io.TFRecordWriter(output_file) as builder:
    for wav in wavs:
      builder.write(wav.astype(np.float32).tobytes())