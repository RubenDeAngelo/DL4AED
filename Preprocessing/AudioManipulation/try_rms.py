from Preprocessing.AudioManipulation.rms import calc_avarage_rms
from rms import calc_avarage_rms, adjust_noise

avrg_speech_rms = calc_avarage_rms("C:\\Users\\johan\\DL4AED\\processed_data\\Segment_speech")
print(avrg_speech_rms)

dest_dBFS_noise = "processed_data/dBFS_Normalized_noise"
noise_path = "C:\\Users\\johan\\DL4AED\\processed_data\\Segment_noise\\"
adjust_noise(noise_path, avrg_speech_rms, dest_dBFS_noise)