from vggish_input import waveform_to_examples
import numpy as np
from keras.models import load_model
import vggish_params
import pyaudio
from pathlib import Path
import time
import tensorflow as tf
import wave
import wget
import ubicoustics

# Variables
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = RATE
float_dtype = '>f4'

###########################
# Download model, if it doesn't exist
###########################
MODEL_URL = "https://www.dropbox.com/s/cq1d7uqg0l28211/example_model.hdf5?dl=1"
MODEL_PATH = "models/example_model.hdf5"
print("=====")
print("Checking model... ")
print("=====")
model_filename = "models/example_model.hdf5"
ubicoustics_model = Path(model_filename)
if (not ubicoustics_model.is_file()):
    print("Downloading example_model.hdf5 [867MB]: ")
    wget.download(MODEL_URL,MODEL_PATH)

# Load Model
context = ubicoustics.everything
context_mapping = ubicoustics.context_mapping
trained_model = model_filename
other = True
selected_file = 'example.wav'
selected_context = 'everything'

print("Using deep learning model: %s" % (trained_model))
model = load_model(trained_model)
graph = tf.get_default_graph()
wf = wave.open(selected_file, 'rb')

context = context_mapping[selected_context]
label = dict()
for k in range(len(context)):
    label[k] = context[k]

# Setup Callback
def audio_samples(input, frame_count, time_info, status_flags):
    global graph
    in_data = wf.readframes(frame_count)
    np_wav = np.fromstring(in_data, dtype=np.int16) / 32768.0
    x = waveform_to_examples(np_wav, RATE)
    predictions = []

    with graph.as_default():
        if x.shape[0] != 0:
            x = x.reshape(len(x), 96, 64, 1)
            pred = model.predict(x)
            predictions.append(pred)

        for prediction in predictions:
            m = np.argmax(prediction[0])
            if (m < len(label)):
                p = label[m]
                print("Prediction: %s (%0.2f)" % (ubicoustics.to_human_labels[label[m]], prediction[0,m]))
                n_items = prediction.shape[1]
            else:
                print("KeyError: %s" % m)

    return (in_data, pyaudio.paContinue)

# Setup pyaudio waveread stream
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK, stream_callback=audio_samples)

# Start non-blocking stream
print("Beginning prediction for %s (use speakers for playback):" % selected_file)
stream.start_stream()
while stream.is_active():
    time.sleep(0.1)
