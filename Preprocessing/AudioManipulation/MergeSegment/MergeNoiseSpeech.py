for i in range(0, len(speech_seg_path)):
    # Load Noise Segement
    noise_seg_path_random = random.choice(noise_seg_path)
    noise_seg_data = AudioSegment.from_file(noise_seg_path_random, ".wav") - 3  # -3dB

    # Load Speech Segment
    speech_seg_data = AudioSegment.from_file(speech_seg_path[i], ".wav")

    # Mix  Audio
    noisy_speech_segment = speech_seg_data.overlay(noise_seg_data)

    # Create Name Suffix
    noise_name = os.path.splitext(noise_seg_path_random)[0]
    speech_name = os.path.splitext(speech_seg_path[i])[0]

    speech_name = speech_name.split('/')[-1]
    index = speech_name.split("_")

    if len(index[-1]) == 1:
        index[-1] = str(0) + index[-1]

    final_speech_name = index[0] + "_"

    for i in range(1, len(index)):
        final_speech_name += index[i]
        final_speech_name += "_"

    file_name = "/Users/daniel/datasets/Segment_noisy_speech/" + final_speech_name + noise_name.split('/')[-1] + '.wav'

    # Export Audio
    noisy_speech_segment.export(file_name, format="wav")

