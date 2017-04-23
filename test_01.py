import numpy as np

zahlen = [[0,15,-15],[15,0,-15],[15,0,-15]]
np.savetxt("zahlen.txt",zahlen)

zahlenIn = np.loadtxt("zahlen.txt")
print(zahlenIn)
