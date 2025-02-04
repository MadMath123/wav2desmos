#Code from https://github.com/klyshko/signal_processing/blob/master/Practical6.ipynb
''''''import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
outFile = open("out.txt","w")
sampFreq, sound = wavfile.read(input('file name: '))
sound = sound / 2.0**15
length_in_s = sound.shape[0] / sampFreq
time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s
arrCount = int(input('tone count: '))
F = [[] for i in range(arrCount)]
V = [[] for i in range(arrCount)]
diffLen=int(input("Amount of Data Joined: "))
step=int(input("step: "))
outFile.write("t=0\nt\\to0\n")
for i in range(0, len(sound), step):
	signal = sound[:,0][i:i+diffLen]
	fft_spectrum = np.fft.rfft(signal)
	freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
	fft_spectrum_abs = np.abs(fft_spectrum)
	#End code from https://github.com/klyshko/signal_processing/blob/master/Practical6.ipynb
	amp = fft_spectrum_abs
	inds = amp.argsort()[::-1]
	r = len(freq)
	for i in range(arrCount):
		if i < r:
			F[i].append((freq[inds[i]]*256)//1/256)
			V[i].append(amp[inds[i]]//1/256)
		else:
			F[i].append(0)
			V[i].append(0)

for i in range(len(F)):
	outFile.write("f_{req"+str(i)+"}="+str(F[i]).replace("[","\\left[").replace("]","\\right]")+"\n")
	outFile.write("a_{mp"+str(i)+"}="+str(V[i]).replace("[","\\left[").replace("]","\\right]")+"\n")

for i in range(len(F)):
	outFile.write("\\operatorname{tone}\\left(f_{req"+str(i)+"}\\left[t\\right],a_{mp"+str(i)+"}\\left[t\\right]\\right)\n")
print("Done")
