from scipy.io.wavfile import write
from obspy import read
import sys
import numpy as np

st = read(sys.argv[1])
arr = []
samplerate = 48000
print(f"Reading {sys.argv[1]}...")

print(st)
print(st[0].stats)
print(st[0].data)

if(len(sys.argv) > 2):
    samplerate = int(sys.argv[2])

try:
    f = open(f"{sys.argv[1]}_{samplerate}hz.txt", "x") 
except OSError:
    print("Output file already exists. Aborted.")
    sys.exit()
f = open(f"{sys.argv[1]}_{samplerate}hz.txt", "a") 

for trace in st:
    # Access the data samples from the trace
    data_samples = trace.data
    
    # Print each sample
    for sample in data_samples:
        arr.append(sample/256)
        f.write(f"{sample}\n")

write(f"{sys.argv[1]}_{samplerate}hz.wav", samplerate, np.array(arr).astype(np.int16))
print(f"Written {sys.argv[1]}_{samplerate}hz.wav")
