from matplotlib import pyplot as plt

import  numpy as np
a=3
xlimit=np.arange(0,10,.001)
ylimit=(4-a)*np.square(1-np.sqrt(xlimit/a))
plt.plot(xlimit,ylimit)
plt.grid(color="gray")
plt.show()