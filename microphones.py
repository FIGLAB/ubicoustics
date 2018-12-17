# A wrapper for listing all available microphones using pyaudio
import pyaudio

# PyAudio Microphone List
def list_microphones():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    MICROPHONES_LIST = []
    MICROPHONES_DESCRIPTION = []
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            desc = "# %d - %s" % (i, p.get_device_info_by_host_api_device_index(0, i).get('name'))
            MICROPHONES_DESCRIPTION.append(desc)
            MICROPHONES_LIST.append(i)
    
    output = []
    output.append("=== Available Microphones: ===")
    output.append("\n".join(MICROPHONES_DESCRIPTION))
    output.append("======================================")
    return "\n".join(output),MICROPHONES_DESCRIPTION,MICROPHONES_LIST

output,desc,l = list_microphones()
print(output)