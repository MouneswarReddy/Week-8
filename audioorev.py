from scipy.io import wavfile
#audio format must be .wav or else cant read
(fs, x)= wavfile.read('/home/smouneswar/Documents/week-8/sample-3s.wav')
# Reverse the audio sample
x_reverse = x[::-1]
wavfile.write('aud.wav', fs, x_reverse)
