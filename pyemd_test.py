EMD
from PyEMD import EMD
import numpy as np

s = np.random.random(100)
emd = EMD()
IMFs = emd(s)


EEMD
from PyEMD import EEMD
import numpy as np

s = np.random.random(100)
eemd = EEMD()
eIMFs = eemd(s)

CEEMDAN
from PyEMD import CEEMDAN
import numpy as np

s = np.random.random(100)
ceemdan = CEEMDAN()
cIMFs = ceemdan(s)


Visualisation
import numpy as np
from PyEMD import EMD, Visualisation

t = np.arange(0, 3, 0.01)
S = np.sin(13*t + 0.2*t**1.4) - np.cos(3*t)

# Extract imfs and residue
# In case of EMD
emd = EMD()
emd.emd(S)
imfs, res = emd.get_imfs_and_residue()

# In general:
#components = EEMD()(S)
#imfs, res = components[:-1], components[-1]

vis = Visualisation()
vis.plot_imfs(imfs=imfs, residue=res, t=t, include_residue=True)
vis.plot_instant_freq(t, imfs=imfs)
vis.show()


EMD2D/BEMD
from PyEMD import EMD2D  #, BEMD
import numpy as np

x, y = np.arange(128), np.arange(128).reshape((-1,1))
img = np.sin(0.1*x)*np.cos(0.2*y)
emd2d = EMD2D()  # BEMD() also works
IMFs_2D = emd2d(img)
