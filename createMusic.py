from functools import total_ordering
import numpy as np
import soundfile as sf
from sklearn.preprocessing import MinMaxScaler
samplerate = 44100
data = np.random.uniform(-1, 1, size=(samplerate * 10, 2))

from PIL import Image
import numpy 
image = Image.open("RC.jpg")
array = numpy.asarray(image)

# Write out audio as 24bit PCM WAV
# sf.write('./output/stereo_file1.wav', array, samplerate, subtype='PCM_16')

# Write out audio as 24bit Flac
# sf.write('stereo_file.flac', data, samplerate, format='flac', subtype='PCM_16')

# Write out audio as 16bit OGG
# sf.write('stereo_file.ogg', data, samplerate, format='ogg', subtype='vorbis')

scaler = MinMaxScaler(feature_range=(-1, 1))
# 减少一列
dataset = np.delete(array, -1, axis=2)
total = dataset.size
arr = dataset.reshape(total,2)
normalized_arr = scaler.fit_transform(arr).flatten()
sf.write('./output/stereo_file1.wav', arr, total, subtype='PCM_16')
