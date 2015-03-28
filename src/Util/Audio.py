'''
Audio Outputs
'''
import sys
import pyaudio
import wave

def alert(alertName):
    if alertName=='connected':
        fName = '../../Res/connected.wav'
    elif alertName=='connFailed':
        fName = '../../Res/connFailed.wav'
    wf = wave.open(fName, 'r')
    p = pyaudio.PyAudio()
    
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    
    data = wf.readframes(1024)
    
    while data != '':
        stream.write(data)
        data = wf.readframes(1024)
    
    stream.stop_stream()
    stream.close()
    
    p.terminate
    
    