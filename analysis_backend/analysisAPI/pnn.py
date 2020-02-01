
import numpy as np
from scipy.signal import find_peaks

#*******************************************************
#               Find RRI          
#*******************************************************
def find_RRI(time, data):       
    peaks, _ = find_peaks(np.array(data), distance=25, prominence=50)
    peak_time = np.array(time)[peaks] * 0.001
    RRI = np.diff(peak_time, n = 1)
    return peak_time, RRI
    
#*******************************************************
#               Calculation of PNN
#*******************************************************
def cal_pnn(peak_time, RRI):
    peak_time, RRI = peak_time, RRI        
    diffRRI = np.abs(np.diff(RRI, n=1))
    q = len(diffRRI)
    
    pnn50 = []
    pnn_time = []
    
    for i in range(30, q):
        tmp = diffRRI[i-31:i]
        pnn50.append(len(np.where(tmp > 0.05)[0])/31.0)
        pnn_time.append(peak_time[i])
    return pnn_time, pnn50

