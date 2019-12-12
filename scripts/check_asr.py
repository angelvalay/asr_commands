import sys
import librosa
import numpy as np
from sklearn.externals import joblib

model_load = joblib.load('../models/my_model_2.pkl')

# 0 Avanza, 1 Derecha, 2 Detente, 3 Izquierda, 4 Gira

def get_command(path):
    if path.endswith(".wav"):
        data, sr = librosa.load(path)
        chroma_stft = librosa.feature.chroma_stft(y=data, sr=sr)
        spec_cent = librosa.feature.spectral_centroid(y=data, sr=sr)
        spec_bw = librosa.feature.spectral_bandwidth(y=data, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=data, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(data)
        mfcc = librosa.feature.mfcc(y=data, sr=sr)
        _X=np.array([np.mean(chroma_stft), np.mean(spec_cent), np.mean(spec_bw), np.mean(rolloff), np.mean(zcr)])
        for e in mfcc:
            _X=np.append(_X,[np.mean(e)])
        _Y = model_load.predict([_X])
        return _Y[0]


def main():
    print(get_command(sys.argv[1]))

if __name__ == "__main__":
    main()