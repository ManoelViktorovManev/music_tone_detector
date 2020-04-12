from __future__ import print_function, division
import wave
import numpy as np
import matplotlib.pyplot as plt

wr = wave.open('test1.wav', 'r')
sz = wr.getframerate()
q = 5  
c = 12  
sf = 1.5 

for num in range(c):
    print('Processing from {} to {} s'.format(num*q, (num+1)*q))
    avgf = np.zeros(int(sz/2+1))
    snd = np.array([])
    for j in range(q):
        da = np.fromstring(wr.readframes(sz), dtype=np.int16)
        left, right = da[0::2]*sf, da[1::2]*sf
        lf, rf = abs(np.fft.rfft(left)), abs(np.fft.rfft(right))
        snd = np.concatenate((snd, (left+right)/2))
        avgf += (lf+rf)/2
    avgf /= q
    plt.figure(1)
    a = plt.subplot(211)  
    r = 2**16/2
    a.set_ylim([-r, r])
    a.set_xlabel('time [s]')
    a.set_ylabel('signal [-]')
    x = np.arange(44100*q)/44100
    plt.plot(x, snd)
    b = plt.subplot(212)  # frequencies
    b.set_xscale('log')
    b.set_xlabel('frequency [Hz]')
    b.set_ylabel('|amplitude|')
    plt.plot(abs(avgf))
    plt.savefig('simple{:02d}.png'.format(num))
    plt.clf()