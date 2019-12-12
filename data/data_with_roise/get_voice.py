import numpy as np
import librosa.display
import librosa.output
import matplotlib.pyplot as plt
import sys

def get_file_audio(in_path, out_path):
    data, sr = librosa.load(in_path, sr=44100)
    _noise = np.array([])
    _data = np.array([])
    _flag_start = False
    for d in data:
        if _flag_start:
            _data = np.append(_data, [d])
        else:
            _noise = np.append(_data, [d])
        if d > 0.08 and not _flag_start:
            _flag_start = True
    _n_data = np.array([])
    _flag_start = False
    for item in reversed(_data):
        if _flag_start:
            _n_data = np.append(_n_data, [item])
        if item > 0.08 and not _flag_start:
            _flag_start = True
    _n_data = _n_data[::-1]
    librosa.output.write_wav(out_path, np.asfortranarray(_n_data), sr)


def main():
    # print command line arguments
    get_file_audio(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()