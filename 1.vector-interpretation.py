#%%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v2 = [3, -2]
v3 = [4, -3, 2]
v3t = np.transpose(v3)

plt.plot([0,v2[0]],[0,v2[1]])
plt.axis('equal')
plt.plot([-4,4],[0,0],'k--')
plt.plot([0,0],[-4,4],'k--')
plt.grid()
plt.axis((-4,4,-4,4))
plt.show(block=True)

#plot 3D
fig = plt.figure(figsize=plt.figaspect(1))
# ax=fig.gca(projection='3d')
ax=fig.add_subplot(projection='3d')

ax.plot([0,v3[0]],[0,v3[1]],[0,v3[2]],linewidth=3)

ax.plot([0,0],[0,0],[-4,4],'k--')
ax.plot([0,0],[-4,4],[0,0],'k--')
ax.plot([-4,4],[0,0],[0,0],'k--')
plt.show()
# %%
