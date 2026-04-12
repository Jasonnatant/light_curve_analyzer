#Start of Program
import numpy as np
import matplotlib.pyplot as plt
import random
# (Step 1) Load or generate light curve data (time, brightness)
time = np.array([3, 4, 5, 6, 7, 8, 9, 10])
brightness = np.array([1, 2, 3, 4, 3, 3, 7, 8])
# (Step 2) Preprocess data (clean or normalize if needed)

# (Step 3) Plot brightness vs time (light curve)
plt.plot( time, brightness )
# (Step 4) Identify brightness anomalies (Dips)
threshold = 3

dip_times = []
dip_values = []

for i in range(len(brightness)):
    if brightness[i] <= threshold:
        dip_times.append(time[i])
        dip_values.append(brightness[i])
        print("Dip times:", dip_times)
        print("Dip values:", dip_values)

# (Step 5) Check if anomalies exist 
plt.scatter(dip_times, dip_values, color='red')


# If yes -> highlight them on graph
# If no -> print "No anomalies detected"
# (Step 6) Display final result 
plt.xlabel("time")
plt.ylabel("brightness")
plt.title("Light Curve")
plt.show()