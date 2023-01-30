import matplotlib.pyplot as plt
import numpy as np


def r2p(x):                         # function returns absolute numbers and angles
    return np.abs(x), np.angle(x)


PI = 3.141592

x = np.zeros(512)

for i in range(0, 412):
    #x[i] = (0.54-0.46*np.cos(2*PI*(i-128)/256)) #*np.sin(2*PI*100*i/512)
    x[i] = np.sin(2*PI*100*i/512)
    #x[i] = 1

#sp = np.fft.rfft(np.sin(2*PI*100*t/512)
sp = np.fft.rfft(x)                 # creates DFT
mag, phase = r2p(sp)                # changes to polar form
mag = 20*np.log10(mag/256)          # change to log scale
print(mag)
plt.plot(mag)
plt.title('Rectangular Window')
plt.xlabel('Frequency samples (N)')
plt.ylabel('Spectral Density (dB)')
plt.show()


