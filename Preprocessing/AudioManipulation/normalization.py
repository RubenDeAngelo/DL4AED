from rms import calc_avarage_rms, adjust_noise


def normalization():
    # clac avarage rms of segment speech
    speech_path = "processed_data/Segment_speech"
    avrg_speech_rms = calc_avarage_rms(speech_path)

    # adjust the noise segment with gauß
    dest_dBFS_noise = "processed_data/dBFS_Normalized_noise"
    noise_path = "processed_data/Segment_noise"
    adjust_noise(noise_path, avrg_speech_rms, dest_dBFS_noise)
