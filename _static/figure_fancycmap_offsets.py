
# Example on using user-defined color mapping offsets

import numpy as np
from pylab import *
from envtoolkit.colors import FancyCmap

# defining the five colors of the colormap and the
# mapping offset values
input_cmap = ['Blue', 'Yellow', 'Green', 'Red', 'Black']
offset = [0, 0.05, 0.1,  0.9, 0.95, 1]

# defining the color limits of the plots
cmin = -1.7
cmax = -cmin

# generating two smoothed colormaps. 
# one with user-defined mappings, one without
smooth = True
svgsm = FancyCmap(input_cmap, smooth=smooth)
svgsmbis = FancyCmap(input_cmap, smooth=smooth, list_offset=offset)

# generating two discrete colormaps. 
# one with user-defined mappings, one without
smooth = False
svg = FancyCmap(input_cmap, smooth=smooth)
svgbis = FancyCmap(input_cmap, smooth=smooth, list_offset=offset)

# generating data to plot
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2


# plotting
fig = figure()
subplots_adjust(wspace=0.1, hspace=0.1, 
        bottom=0.01, top=0.95, left=0.01, right=0.97)

ax1 = subplot(2,2,1)
cs = pcolormesh(X,Y,Z, cmap=svg.makecmap(), shading='auto')
cs.set_clim(cmin, cmax)
cb = colorbar(cs)
svg.generate_cbticks(cb)
title('No smoothing, no off. list')

ax2 = subplot(2,2,2)
cs = pcolormesh(X,Y,Z, cmap=svgbis.makecmap(), shading='auto')
cs.set_clim(cmin, cmax)
cb = colorbar(cs)
svgbis.generate_cbticks(cb)
title('No smoothing, with off. list')

ax3 = subplot(2,2,3)
cs = pcolormesh(X,Y,Z, cmap=svgsm.makecmap(), shading='auto')
cs.set_clim(cmin, cmax)
cb = colorbar(cs)
title('With smoothing, no off. list')

ax4 = subplot(2,2,4)
cs = pcolormesh(X,Y,Z, cmap=svgsmbis.makecmap(), shading='auto')
cs.set_clim(cmin, cmax)
cb = colorbar(cs)
title('With smoothing, with off. list')

for ax in [ax1, ax2, ax3, ax4]:
    setp(ax.get_xticklabels(), visible=False)
    setp(ax.get_yticklabels(), visible=False)

savefig('_static/figure_fancycmap_offsets.png')
