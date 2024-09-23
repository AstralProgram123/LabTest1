import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import random as r


vehicle_count=np.arange(1440)
for i in vehicle_count:
    vehicle_count[i]=r.randint(1,300)
a=vehicle_count.reshape(24,60)
avg=a.sum(axis=1)/(60)

plt.figure(figsize=(20,10))
plt.plot(vehicle_count)
plt.plot(avg, marker=".")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend
plt.show()
