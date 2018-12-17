# Research Code for Ubicoustics
This is the research repository for Ubicoustics: Plug-and-Play Acoustic Activity Recognition (UIST 2018). It contains the base toolchain and demo for Ubicoustics.

![](https://github.com/FIGLAB/ubicoustics/blob/master/media/ubicoustics_a.gif?raw=true)
![](https://github.com/FIGLAB/ubicoustics/blob/master/media/ubicoustics_b.gif?raw=true)

# System Requirements
The deep learning system is written in `python3`, specifically `tensorflow` and `keras`.

To begin, we recommend using `virtualenv` to run a self-contained setup.
```bash
virtualenv ./ubicoustics -p python3
source ubicoustics/bin/activate
```

Once `virtualenv` is activated, install the following dependencies via `pip`

```bash
(ubicoustics)$ pip install numpy==1.14.0
(ubicoustics)$ pip install tensorflow
(ubicoustics)$ pip install keras
(ubicoustics)$ pip install wget
```

Finally, install PyAudio for microphone access.
```bash
(ubicoustics)$ pip install --global-option='build_ext' --global-option='-I/opt/local/include' --global-option='-L/opt/local/lib' pyaudio
```
Keep in mind that `pyaudio` will require `portaudio` and `libasound` as non python dependencies. You'll have to install those separately for your OS.

`IMPORTANT:` When you install `pyaudio` via pip, you need to manually specify the `lib` and `include` directories via the `--global-option` flag. The example above assumes `portaudio` is installed under `/opt/local/include` and `/opt/local/lib`.

# Example Demos
Once the dependencies above are installed, you can run a real-time demo based on an example pre-trained model.  That model is not part of this repo (due to filesize restrictions), but we provide a downloader script to simplify this process.

## Example #0: File Prediction (Simple)
Next, you can run the demo that plays back an audio file via `example_fileprediction_simple.py`:

```shell
(ubicoustics)$ python example_fileprediction_simple.py
```
The script will automatically download a model file called `example_model.hdf5` into the `/models` directory. It's an 865.8MB file, so it might take a while depending on your Internet connection.

The script above will perform audio event detection on `example.wav`. The script will use your computer's speakers to playback the audio file while displaying its predictions. If everything runs correctly, you should get the following output:

```shell
=====
Checking model...
=====
Downloading example_model.hdf5 [867MB]:
100% [.......................................]
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Toilet Flushing (1.00)
Prediction: Toilet Flushing (1.00)
Prediction: Toilet Flushing (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Knocking (1.00)
Prediction: Knocking (0.99)
Prediction: Knocking (0.91)
```

## Example #1: File Prediction (Playback)
Next, you can run the demo that plays back an audio file via `example_fileprediction_playback.py`:

```shell
(ubicoustics)$ python example_fileprediction_playback.py
```

It's similar to the previous example, but it uses `pyaudio`'s' non-blocking mechanism to process audio buffers at a given sample length. We insert `ubicoustics` predictions within that block:

```python
# Audio FORMAT
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = RATE

# Callback
def audio_samples(input, frame_count, time_info, status_flags):
  # Audio Processing Code here
  # ...
  return (in_data, pyaudio.paContinue)

# Non-Blocking Call
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK, stream_callback=audio_samples)

```

And here's what that output looks like:

```shell
=====
Checking model...
=====
Beginning prediction for example.wav (use speakers for playback):
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Coughing (0.06)
Prediction: Toilet Flushing (1.00)
Prediction: Toilet Flushing (1.00)
Prediction: Toilet Flushing (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Chopping (0.96)
Prediction: Knocking (1.00)
Prediction: Knocking (1.00)
Prediction: Knocking (0.99)
```


## Example #2: Live Prediction (Simple)

This next example script will use your system microphone to perform live audio event predictions.

```bash
(ubicoustics)$ python example_liveprediction_simple.py
```

It will check your system for a list of available microphones, and it will prompt you to choose one.

```
=====
1 / 2: Checking Microphones...
=====
=== Available Microphones: ===
# 0 - Built-in Microphone
# 1 - Gierad's Apple AirPods
======================================
Select microphone [0]: 0
```

You can also use the `--mic <mic-id>` flag to specify which local microphone to use.

```
(ubicoustics)$ python example_liveprediction_simple.py --mic 0
```

The system will then perform audio event predictions using the chosen microphone. Your output should look something like this:

```
Using mic: # 0 - Built-in Microphone
=====
2 / 2: Checking model...
=====
# Live Prediction Using Microphone: # 0 - Built-in Microphone
Prediction: Typing (0.97)
Prediction: Typing (0.97)
Prediction: Typing (1.00)
Prediction: Knocking (1.00)
Prediction: Knocking (0.46)
Prediction: Door In-Use (0.15)
Prediction: Door In-Use (0.12)
Prediction: Door In-Use (0.12)
Prediction: Phone Ringing (0.46)
Prediction: Phone Ringing (0.86)
```

This script makes predictions every second. This script should run on most platforms, including a `Raspberry Pi B+` (1GB of memory, 16GB disk space,  with 4GB set as SWAP). If you need help setting up your RPi, send an email to Gierad (gierad.laput@cs.cmu.edu).

To manually grab a list of microphones for your system, use the following command:
```bash
(ubicoustics)$ python microphones.py
```

## Example #3: Live Prediction (Detail View)

If you want to form an intuition on the system's behavior, we've created an example that exposes the system's confidence values, along with audio levels and some parameters that you can tweak (e.g., thresholds).

```
(ubicoustics)$ python example_liveprediction_detail.py
```

Here's an example screenshot:

![](https://github.com/FIGLAB/ubicoustics/blob/master/media/example_liveprediction_detail.gif?raw=true)

Prediction confidence values will be shown in real time. The system checks whether the highest confidence value exceeds a given threshold AND wether or the audio level is significant enough to warrant an event trigger (e.g., > -40dB). These parameters can be adjusted using the `PREDICTION_THRES` and `DBLEVEL_THRES` parameters:

```python
PREDICTION_THRES = 0.8 # confidence
DBLEVEL_THRES = -40 # dB
```

# Reference
Gierad Laput, Karan Ahuja, Mayank Goel, Chris Harrison. 2018. Ubicoustics: Plug-and-Play Acoustic Activity Recognition. In Proceedings of the 31st Annual Symposium on User Interface Software and Technology (UIST '18). ACM, New York, NY, USA.

[Download the paper here](http://www.gierad.com/assets/ubicoustics/ubicoustics.pdf).

BibTex Reference:
```
@inproceedings {ubicoustics,
  author={Laput, G. and Ahuja, K. and Goel, M. and Harrison, C},
  title={Ubicoustics: Plug-and-Play Acoustic Activity Recognition},
  booktitle={Proceedings of the 31st Annual Symposium on User Interface Software and Technology},
  series={USIT '18},
  year={2018},
  location={Berlin, Germany},
  numpages={10},
  publisher={ACM},
  address={New York, NY, USA}
}
```

# License
Due to licensing restrictions, audio `wav` files are currently available by request, and can only be used for research i.e., non-commercial purposes. Otherwise, Ubicoustics is freely available for non-commercial use, and may be redistributed under these conditions. Please see the license for further details. For a commercial license, please contact Gierad Laput and Chris Harrison.
