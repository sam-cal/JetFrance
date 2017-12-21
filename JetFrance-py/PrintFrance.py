#!/usr/bin/env python

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
#m = Basemap(width=15.e6,height=15.e6,\
#            projection='gnom',lat_0=60.,lon_0=-30.)
m = Basemap(projection='merc',llcrnrlat=41,urcrnrlat=52,\
            llcrnrlon=-6,urcrnrlon=10,lat_ts=15,resolution='c')
m.drawmapboundary(fill_color='aqua')
m.drawcoastlines()
m.fillcontinents(color='green',lake_color='aqua')
m.drawparallels(np.arange(10,90,20))
m.drawmeridians(np.arange(-180,180,30))
m.drawcountries()



m.plot(2.85, 45.9667, 'ro', latlon=True)
m.plot(2.89667, 45.7659, 'ro', latlon=True)
m.plot(3.23333, 45.7667, 'ro', latlon=True)
m.plot(3.43333, 45.7333, 'ro', latlon=True)
m.plot(3.4, 45.75, 'ro', latlon=True)
m.plot(2.58333, 45.9333, 'ro', latlon=True)
m.plot(3.16667, 45.4667, 'ro', latlon=True)
m.plot(3.58333, 45.6667, 'ro', latlon=True)
m.plot(3.3, 45.75, 'ro', latlon=True)
m.plot(3.25, 45.8, 'ro', latlon=True)
m.plot(2.9, 46.0333, 'ro', latlon=True)
m.plot(3.26667, 45.9667, 'ro', latlon=True)
m.plot(3.49973, 45.5506, 'ro', latlon=True)
m.plot(3.21667, 45.75, 'ro', latlon=True)
m.plot(3.58333, 45.6333, 'ro', latlon=True)
m.plot(2.53333, 45.7667, 'ro', latlon=True)
m.plot(2.71111, 46.0378, 'ro', latlon=True)
m.plot(2.61667, 45.7667, 'ro', latlon=True)
m.plot(3.33333, 45.8, 'ro', latlon=True)
m.plot(3.31667, 45.7, 'ro', latlon=True)
m.plot(2.9, 45.5667, 'ro', latlon=True)
m.plot(3.61667, 45.5, 'ro', latlon=True)
m.plot(3.41667, 45.6, 'ro', latlon=True)
m.plot(3.21667, 45.6167, 'ro', latlon=True)
m.plot(3.05, 45.5167, 'ro', latlon=True)
m.plot(3.61695, 45.7228, 'ro', latlon=True)
m.plot(3.91667, 45.5167, 'ro', latlon=True)
m.plot(3.2, 45.4167, 'ro', latlon=True)
m.plot(2.53333, 45.55, 'ro', latlon=True)
m.plot(2.7, 45.5333, 'ro', latlon=True)
m.plot(3.9, 45.4833, 'ro', latlon=True)
m.plot(3.28333, 45.5667, 'ro', latlon=True)
m.plot(3.05, 45.5333, 'ro', latlon=True)
m.plot(3.28333, 45.9, 'ro', latlon=True)
m.plot(3.01667, 45.7833, 'ro', latlon=True)
m.plot(3.06667, 45.8333, 'ro', latlon=True)
m.plot(3.16667, 46.0333, 'ro', latlon=True)
m.plot(2.73333, 45.4167, 'ro', latlon=True)
m.plot(3.25, 45.6167, 'ro', latlon=True)
m.plot(2.95, 45.6, 'ro', latlon=True)
m.plot(2.7, 45.7833, 'ro', latlon=True)
m.plot(2.93417, 45.9962, 'ro', latlon=True)
m.plot(2.68333, 45.6667, 'ro', latlon=True)
m.plot(3.05, 45.9, 'ro', latlon=True)
m.plot(3.5, 45.6833, 'ro', latlon=True)
m.plot(3.23333, 46, 'ro', latlon=True)
m.plot(3.75, 45.55, 'ro', latlon=True)
m.plot(3.13333, 45.95, 'ro', latlon=True)
m.plot(2.93333, 45.9667, 'ro', latlon=True)
m.plot(3.7, 45.8833, 'ro', latlon=True)
m.plot(3.03333, 45.55, 'ro', latlon=True)
m.plot(3.61667, 45.8167, 'ro', latlon=True)
m.plot(3.10445, 45.5628, 'ro', latlon=True)
m.plot(3.08333, 45.7833, 'ro', latlon=True)
m.plot(3.4, 45.7833, 'ro', latlon=True)
m.plot(3.13333, 45.6833, 'ro', latlon=True)
m.plot(3.63333, 45.5667, 'ro', latlon=True)
m.plot(2.55, 45.75, 'ro', latlon=True)
m.plot(2.7, 46.0833, 'ro', latlon=True)
m.plot(2.91667, 45.6833, 'ro', latlon=True)
m.plot(2.86667, 46.2167, 'ro', latlon=True)
m.plot(3.88333, 45.4333, 'ro', latlon=True)
m.plot(3.58333, 45.8167, 'ro', latlon=True)
m.plot(3.13333, 45.6667, 'ro', latlon=True)
m.plot(3.13333, 45.5833, 'ro', latlon=True)
m.plot(3.6, 45.8667, 'ro', latlon=True)
m.plot(3.25, 45.55, 'ro', latlon=True)
m.plot(3.26667, 45.9167, 'ro', latlon=True)
m.plot(2.55, 45.6167, 'ro', latlon=True)
m.plot(2.48333, 45.8, 'ro', latlon=True)
m.plot(3.13333, 45.8667, 'ro', latlon=True)
m.plot(3.25, 45.9333, 'ro', latlon=True)
m.plot(3.03028, 45.4587, 'ro', latlon=True)
m.plot(3.8, 45.5333, 'ro', latlon=True)
m.plot(3.13333, 45.5333, 'ro', latlon=True)
m.plot(3.94464, 45.4667, 'ro', latlon=True)
m.plot(3.11667, 45.6167, 'ro', latlon=True)
m.plot(2.95, 46.0333, 'ro', latlon=True)
m.plot(3.55, 45.7167, 'ro', latlon=True)
m.plot(3.75, 45.3833, 'ro', latlon=True)
m.plot(3.3, 46.0167, 'ro', latlon=True)
m.plot(3.01723, 46.0567, 'ro', latlon=True)
m.plot(3.18333, 45.4833, 'ro', latlon=True)
m.plot(2.73333, 45.6, 'ro', latlon=True)
m.plot(3.21667, 46.0333, 'ro', latlon=True)
m.plot(3.5, 45.9333, 'ro', latlon=True)
m.plot(2.83333, 46.15, 'ro', latlon=True)
m.plot(3.33333, 45.5167, 'ro', latlon=True)
m.plot(3.43333, 46.0333, 'ro', latlon=True)
m.plot(3.48333, 45.8833, 'ro', latlon=True)
m.plot(2.86667, 45.7, 'ro', latlon=True)
m.plot(2.56806, 45.7103, 'ro', latlon=True)
m.plot(2.56667, 45.5, 'ro', latlon=True)
m.plot(3.23333, 45.4167, 'ro', latlon=True)
m.plot(3.25, 46.0333, 'ro', latlon=True)
m.plot(2.53333, 45.8, 'ro', latlon=True)
m.plot(3.1, 45.85, 'ro', latlon=True)
m.plot(3.3, 46, 'ro', latlon=True)
m.plot(3.1, 45.9667, 'ro', latlon=True)
m.plot(3.1, 45.6833, 'ro', latlon=True)
m.plot(3.23333, 45.7, 'ro', latlon=True)
m.plot(3.38333, 45.9167, 'ro', latlon=True)
m.plot(3.1, 45.8833, 'ro', latlon=True)
m.plot(2.775, 45.6833, 'ro', latlon=True)
m.plot(2.68333, 46, 'ro', latlon=True)
m.plot(3.06667, 45.7333, 'ro', latlon=True)
m.plot(3.53333, 45.6167, 'ro', latlon=True)
m.plot(3.21667, 45.7667, 'ro', latlon=True)
m.plot(3.21667, 45.9333, 'ro', latlon=True)
m.plot(3.26667, 45.6667, 'ro', latlon=True)
m.plot(3.06667, 45.7833, 'ro', latlon=True)
m.plot(2.81667, 46.1, 'ro', latlon=True)
m.plot(3.3, 45.5667, 'ro', latlon=True)
m.plot(3.31667, 45.7667, 'ro', latlon=True)
m.plot(3.25, 45.7, 'ro', latlon=True)
m.plot(2.88333, 45.6667, 'ro', latlon=True)
m.plot(3.08333, 45.8833, 'ro', latlon=True)
m.plot(3.48333, 45.45, 'ro', latlon=True)
m.plot(3.3, 45.5167, 'ro', latlon=True)
m.plot(3.31667, 45.7833, 'ro', latlon=True)
m.plot(3.3, 45.5333, 'ro', latlon=True)
m.plot(2.73333, 45.65, 'ro', latlon=True)
m.plot(3.6, 45.8833, 'ro', latlon=True)
m.plot(2.47611, 45.8542, 'ro', latlon=True)
m.plot(3.31667, 45.55, 'ro', latlon=True)
m.plot(3.18333, 45.7, 'ro', latlon=True)
m.plot(2.8, 45.9167, 'ro', latlon=True)
m.plot(2.8, 46.1333, 'ro', latlon=True)
m.plot(2.75, 46.2, 'ro', latlon=True)
m.plot(2.86667, 45.8333, 'ro', latlon=True)
m.plot(3.73333, 45.4833, 'ro', latlon=True)
m.plot(3.3, 45.4667, 'ro', latlon=True)
m.plot(3.28333, 45.4833, 'ro', latlon=True)
m.plot(3, 45.4, 'ro', latlon=True)
m.plot(2.75, 46.1833, 'ro', latlon=True)
m.plot(3.68333, 45.6667, 'ro', latlon=True)
m.plot(3.41667, 45.4334, 'ro', latlon=True)
m.plot(3.48333, 45.95, 'ro', latlon=True)
m.plot(3.08333, 45.8333, 'ro', latlon=True)
m.plot(3.45, 45.6833, 'ro', latlon=True)
m.plot(3.21667, 45.9, 'ro', latlon=True)
m.plot(2.9, 46.05, 'ro', latlon=True)
m.plot(3.15, 45.4833, 'ro', latlon=True)
m.plot(2.76667, 46.0667, 'ro', latlon=True)
m.plot(3.16667, 45.8, 'ro', latlon=True)
m.plot(3.38333, 45.5667, 'ro', latlon=True)
m.plot(3.23333, 45.8667, 'ro', latlon=True)
m.plot(3.55, 45.55, 'ro', latlon=True)
m.plot(3.18333, 46.05, 'ro', latlon=True)
m.plot(3.1, 45.65, 'ro', latlon=True)
m.plot(2.68333, 45.8667, 'ro', latlon=True)
m.plot(3.08333, 45.5, 'ro', latlon=True)
m.plot(3.6, 45.6833, 'ro', latlon=True)
m.plot(3.23333, 45.5833, 'ro', latlon=True)
m.plot(3.05, 45.7667, 'ro', latlon=True)
m.plot(2.73333, 46.05, 'ro', latlon=True)
m.plot(3.63333, 45.6667, 'ro', latlon=True)
m.plot(2.93278, 45.5131, 'ro', latlon=True)
m.plot(3.73333, 45.7333, 'ro', latlon=True)
m.plot(2.76667, 45.7667, 'ro', latlon=True)
m.plot(3.23333, 45.7, 'ro', latlon=True)
m.plot(3.15, 45.5, 'ro', latlon=True)
m.plot(3.33333, 45.65, 'ro', latlon=True)
m.plot(3.26667, 45.4667, 'ro', latlon=True)
m.plot(3.18333, 45.9333, 'ro', latlon=True)
m.plot(3.1, 45.45, 'ro', latlon=True)
m.plot(3.05, 45.8, 'ro', latlon=True)
m.plot(3.6, 45.7833, 'ro', latlon=True)
m.plot(3.43333, 45.7, 'ro', latlon=True)
m.plot(3.56667, 45.85, 'ro', latlon=True)
m.plot(3.63333, 45.9, 'ro', latlon=True)
m.plot(3.36667, 45.45, 'ro', latlon=True)
m.plot(2.53333, 45.8667, 'ro', latlon=True)
m.plot(2.60167, 45.4739, 'ro', latlon=True)
m.plot(3.51667, 45.7, 'ro', latlon=True)
m.plot(3.81667, 45.4667, 'ro', latlon=True)
m.plot(3.18333, 45.5, 'ro', latlon=True)
m.plot(3.23333, 45.6667, 'ro', latlon=True)
m.plot(2.85, 45.6833, 'ro', latlon=True)
m.plot(3.1, 45.9333, 'ro', latlon=True)
m.plot(3.48333, 45.7167, 'ro', latlon=True)
m.plot(3.21667, 45.9667, 'ro', latlon=True)
m.plot(2.91667, 45.6333, 'ro', latlon=True)
m.plot(3.15, 45.55, 'ro', latlon=True)
m.plot(3.33333, 45.75, 'ro', latlon=True)
m.plot(3.53333, 45.8, 'ro', latlon=True)
m.plot(3.7, 45.5833, 'ro', latlon=True)
m.plot(3.35, 45.7167, 'ro', latlon=True)
m.plot(3.17334, 45.5623, 'ro', latlon=True)
m.plot(3.23333, 45.5, 'ro', latlon=True)
m.plot(3.35, 45.6167, 'ro', latlon=True)
m.plot(3.08333, 46.05, 'ro', latlon=True)
m.plot(2.63333, 45.5667, 'ro', latlon=True)
m.plot(2.63333, 45.65, 'ro', latlon=True)
m.plot(3.18333, 45.5833, 'ro', latlon=True)
m.plot(3.19, 45.6842, 'ro', latlon=True)
m.plot(3.13333, 46, 'ro', latlon=True)
m.plot(3.23333, 45.4333, 'ro', latlon=True)
m.plot(3.11667, 46, 'ro', latlon=True)
m.plot(3.38333, 45.8333, 'ro', latlon=True)
m.plot(3.1, 45.8333, 'ro', latlon=True)
m.plot(3.05, 45.6167, 'ro', latlon=True)
m.plot(2.81667, 46.0333, 'ro', latlon=True)
m.plot(3.61667, 45.4, 'ro', latlon=True)
m.plot(3.66667, 45.3948, 'ro', latlon=True)
m.plot(3.63778, 45.6334, 'ro', latlon=True)
m.plot(2.55, 45.5333, 'ro', latlon=True)
m.plot(2.76667, 45.9833, 'ro', latlon=True)
m.plot(2.88333, 45.75, 'ro', latlon=True)
m.plot(3.61667, 45.75, 'ro', latlon=True)
m.plot(3.26139, 45.405, 'ro', latlon=True)
m.plot(3.5, 46, 'ro', latlon=True)
m.plot(3.1, 46.0333, 'ro', latlon=True)
m.plot(3.59278, 45.9939, 'ro', latlon=True)
m.plot(2.78333, 45.4667, 'ro', latlon=True)
m.plot(3.46667, 45.6, 'ro', latlon=True)
m.plot(3.05, 45.3333, 'ro', latlon=True)
m.plot(2.71667, 45.9, 'ro', latlon=True)
m.plot(3.35, 45.7667, 'ro', latlon=True)
m.plot(3.33333, 45.4667, 'ro', latlon=True)
m.plot(3.08333, 45.95, 'ro', latlon=True)
m.plot(3.8, 45.4, 'ro', latlon=True)
m.plot(3.58333, 45.5167, 'ro', latlon=True)
m.plot(2.6, 45.9, 'ro', latlon=True)
m.plot(3.36667, 46.0167, 'ro', latlon=True)
m.plot(3.01667, 45.8333, 'ro', latlon=True)
m.plot(2.66667, 45.7, 'ro', latlon=True)
m.plot(2.78333, 45.9, 'ro', latlon=True)
m.plot(2.91667, 45.8833, 'ro', latlon=True)
m.plot(2.93333, 45.45, 'ro', latlon=True)
m.plot(2.66667, 45.8667, 'ro', latlon=True)
m.plot(3.75, 45.6167, 'ro', latlon=True)
m.plot(3.26667, 45.85, 'ro', latlon=True)
m.plot(2.45, 45.8167, 'ro', latlon=True)
m.plot(2.81667, 45.8833, 'ro', latlon=True)
m.plot(3.1, 45.4833, 'ro', latlon=True)
m.plot(3.36667, 45.5167, 'ro', latlon=True)
m.plot(2.81667, 45.6833, 'ro', latlon=True)
m.plot(2.80833, 46.1833, 'ro', latlon=True)
m.plot(3.45, 45.8167, 'ro', latlon=True)
m.plot(3.33333, 45.8667, 'ro', latlon=True)
m.plot(2.73333, 46.1, 'ro', latlon=True)
m.plot(2.68333, 45.7667, 'ro', latlon=True)
m.plot(3.25, 45.6333, 'ro', latlon=True)
m.plot(3.4, 45.7167, 'ro', latlon=True)
m.plot(3.21667, 46.0667, 'ro', latlon=True)
m.plot(3.15, 45.8333, 'ro', latlon=True)
m.plot(3.25, 45.75, 'ro', latlon=True)
m.plot(3.06667, 45.95, 'ro', latlon=True)
m.plot(2.98333, 45.6667, 'ro', latlon=True)
m.plot(3.41667, 45.5, 'ro', latlon=True)
m.plot(2.83333, 45.7333, 'ro', latlon=True)
m.plot(3.67611, 45.8284, 'ro', latlon=True)
m.plot(3.35, 45.4333, 'ro', latlon=True)
m.plot(2.81667, 46, 'ro', latlon=True)
m.plot(2.65, 45.7333, 'ro', latlon=True)
m.plot(3.21667, 45.55, 'ro', latlon=True)
m.plot(3.38333, 45.9, 'ro', latlon=True)
m.plot(3.11667, 45.9, 'ro', latlon=True)
m.plot(3.35, 45.4833, 'ro', latlon=True)
m.plot(3.08333, 45.9333, 'ro', latlon=True)
m.plot(3.05, 45.55, 'ro', latlon=True)
m.plot(3.11667, 45.75, 'ro', latlon=True)
m.plot(2.9, 46.1833, 'ro', latlon=True)
m.plot(3.05, 46.05, 'ro', latlon=True)
m.plot(3, 45.4667, 'ro', latlon=True)
m.plot(3.23333, 45.4333, 'ro', latlon=True)
m.plot(3.31667, 45.9667, 'ro', latlon=True)
m.plot(3.88333, 45.45, 'ro', latlon=True)
m.plot(2.56361, 45.8525, 'ro', latlon=True)
m.plot(3.46667, 45.4333, 'ro', latlon=True)
m.plot(3.63333, 45.85, 'ro', latlon=True)
m.plot(3.46667, 45.4667, 'ro', latlon=True)
m.plot(2.85, 45.8, 'ro', latlon=True)
m.plot(2.9, 46.1, 'ro', latlon=True)
m.plot(2.93333, 45.3833, 'ro', latlon=True)
m.plot(2.55, 46.1167, 'ro', latlon=True)
m.plot(3.68333, 45.7833, 'ro', latlon=True)
m.plot(2.99972, 45.9078, 'ro', latlon=True)
m.plot(3.3, 45.7667, 'ro', latlon=True)
m.plot(3.4, 45.65, 'ro', latlon=True)
m.plot(3.43333, 45.5667, 'ro', latlon=True)
m.plot(3.23333, 45.4833, 'ro', latlon=True)
m.plot(2.51667, 45.6, 'ro', latlon=True)
m.plot(2.63333, 46.0667, 'ro', latlon=True)
m.plot(2.9, 45.7167, 'ro', latlon=True)
m.plot(3.15, 45.6167, 'ro', latlon=True)
m.plot(3.15, 45.55, 'ro', latlon=True)
m.plot(3.38333, 45.4167, 'ro', latlon=True)
m.plot(3.2, 45.4667, 'ro', latlon=True)
m.plot(3.28333, 45.4167, 'ro', latlon=True)
m.plot(3.18333, 45.85, 'ro', latlon=True)
m.plot(2.91667, 46.0667, 'ro', latlon=True)
m.plot(2.9, 46.1, 'ro', latlon=True)
m.plot(3.63333, 45.45, 'ro', latlon=True)
m.plot(2.7, 46.1, 'ro', latlon=True)
m.plot(3.66139, 45.71, 'ro', latlon=True)
m.plot(2.65, 45.9833, 'ro', latlon=True)
m.plot(3.18333, 45.6333, 'ro', latlon=True)
m.plot(3.38333, 45.9333, 'ro', latlon=True)
m.plot(3.68333, 45.6167, 'ro', latlon=True)
m.plot(2.9, 45.85, 'ro', latlon=True)
m.plot(3.66667, 45.5667, 'ro', latlon=True)
m.plot(2.82722, 45.4081, 'ro', latlon=True)
m.plot(3.71667, 45.7167, 'ro', latlon=True)
m.plot(3.77445, 45.4395, 'ro', latlon=True)
m.plot(2.58333, 45.8333, 'ro', latlon=True)
m.plot(3.43333, 45.45, 'ro', latlon=True)
m.plot(3.76667, 45.6, 'ro', latlon=True)
m.plot(2.71667, 45.4667, 'ro', latlon=True)
m.plot(3.1, 45.75, 'ro', latlon=True)
m.plot(2.95, 45.5833, 'ro', latlon=True)
m.plot(3.18333, 45.9167, 'ro', latlon=True)
m.plot(2.73333, 45.7167, 'ro', latlon=True)
m.plot(3.11667, 45.6333, 'ro', latlon=True)
m.plot(3.25, 45.45, 'ro', latlon=True)
m.plot(3.31667, 45.8667, 'ro', latlon=True)
m.plot(3.86667, 45.3833, 'ro', latlon=True)
m.plot(3.81667, 45.5, 'ro', latlon=True)
m.plot(3.43333, 45.7833, 'ro', latlon=True)
m.plot(3.05, 45.8667, 'ro', latlon=True)
m.plot(3.57361, 45.5609, 'ro', latlon=True)
m.plot(3.13333, 46.0333, 'ro', latlon=True)
m.plot(3.33333, 45.9667, 'ro', latlon=True)
m.plot(3.06667, 46.1, 'ro', latlon=True)
m.plot(2.83333, 46.0667, 'ro', latlon=True)
m.plot(3.7, 45.5167, 'ro', latlon=True)
m.plot(2.6, 45.6, 'ro', latlon=True)
m.plot(3.16667, 45.55, 'ro', latlon=True)
m.plot(3.43333, 45.95, 'ro', latlon=True)
m.plot(3.2, 45.7333, 'ro', latlon=True)
m.plot(2.96972, 46.0906, 'ro', latlon=True)
m.plot(3.28333, 45.75, 'ro', latlon=True)
m.plot(2.61667, 46.0333, 'ro', latlon=True)
m.plot(3.17361, 45.9584, 'ro', latlon=True)
m.plot(3.33333, 45.9167, 'ro', latlon=True)
m.plot(2.63333, 46.1083, 'ro', latlon=True)
m.plot(3.7, 45.65, 'ro', latlon=True)
m.plot(3.01667, 45.5333, 'ro', latlon=True)
m.plot(3.15, 45.9333, 'ro', latlon=True)
m.plot(3.33333, 45.4, 'ro', latlon=True)
m.plot(2.86667, 45.7833, 'ro', latlon=True)
m.plot(2.85, 46.2, 'ro', latlon=True)
m.plot(3.1, 45.4167, 'ro', latlon=True)
m.plot(2.80889, 45.5764, 'ro', latlon=True)
m.plot(3.06667, 45.9167, 'ro', latlon=True)
m.plot(2.91667, 46.1667, 'ro', latlon=True)
m.plot(3.41667, 46, 'ro', latlon=True)
m.plot(3.43333, 45.9667, 'ro', latlon=True)
m.plot(3.3, 45.5333, 'ro', latlon=True)
m.plot(3.16667, 45.5833, 'ro', latlon=True)
m.plot(3.55, 45.6833, 'ro', latlon=True)
m.plot(3.8, 45.5833, 'ro', latlon=True)
m.plot(3.41667, 45.6833, 'ro', latlon=True)
m.plot(3.51667, 45.7667, 'ro', latlon=True)
m.plot(3.7, 45.3833, 'ro', latlon=True)
m.plot(2.88111, 45.3942, 'ro', latlon=True)
m.plot(2.68333, 45.6, 'ro', latlon=True)
m.plot(3, 45.6, 'ro', latlon=True)
m.plot(3.16667, 45.6833, 'ro', latlon=True)
m.plot(3.25, 45.6833, 'ro', latlon=True)
m.plot(3.21667, 45.4667, 'ro', latlon=True)
m.plot(3.15, 45.9667, 'ro', latlon=True)
m.plot(3.3, 45.8167, 'ro', latlon=True)
m.plot(3.25, 45.5, 'ro', latlon=True)
m.plot(3.13333, 45.7, 'ro', latlon=True)
m.plot(3.08333, 45.9833, 'ro', latlon=True)
m.plot(3.23333, 45.75, 'ro', latlon=True)
m.plot(3.33333, 45.8333, 'ro', latlon=True)
m.plot(3.61667, 45.4333, 'ro', latlon=True)
m.plot(3.33333, 46.0167, 'ro', latlon=True)
m.plot(3.65, 45.4333, 'ro', latlon=True)
m.plot(3.05, 45.5667, 'ro', latlon=True)
m.plot(2.75, 45.5167, 'ro', latlon=True)
m.plot(3.35, 45.5333, 'ro', latlon=True)
m.plot(3, 46, 'ro', latlon=True)
m.plot(3.2, 45.4833, 'ro', latlon=True)
m.plot(3.7, 45.9, 'ro', latlon=True)
m.plot(2.69806, 46.155, 'ro', latlon=True)
m.plot(3.05, 46.0167, 'ro', latlon=True)
m.plot(3.45, 45.9167, 'ro', latlon=True)
m.plot(3.46667, 45.5167, 'ro', latlon=True)
m.plot(3.55, 45.75, 'ro', latlon=True)
m.plot(3.18333, 45.5167, 'ro', latlon=True)
m.plot(3.01667, 45.7167, 'ro', latlon=True)
m.plot(3.4, 45.4667, 'ro', latlon=True)
m.plot(3.45, 45.65, 'ro', latlon=True)
m.plot(3.2, 45.8167, 'ro', latlon=True)
m.plot(2.75, 45.5833, 'ro', latlon=True)
m.plot(2.66667, 45.8167, 'ro', latlon=True)
m.plot(3.1, 45.5833, 'ro', latlon=True)
m.plot(3.35889, 45.7492, 'ro', latlon=True)
m.plot(3.31667, 45.45, 'ro', latlon=True)
m.plot(3.6, 45.9333, 'ro', latlon=True)
m.plot(3.48333, 45.5167, 'ro', latlon=True)
m.plot(3.05, 45.65, 'ro', latlon=True)
m.plot(3.25, 45.6333, 'ro', latlon=True)
m.plot(3.73333, 45.4167, 'ro', latlon=True)
m.plot(2.6, 46.0667, 'ro', latlon=True)
m.plot(3.25, 45.7333, 'ro', latlon=True)
m.plot(3.16927, 45.9785, 'ro', latlon=True)
m.plot(3.06667, 45.95, 'ro', latlon=True)
m.plot(3.11667, 45.55, 'ro', latlon=True)
m.plot(3.43333, 45.8667, 'ro', latlon=True)
m.plot(3.71667, 45.5333, 'ro', latlon=True)
m.plot(2.63333, 45.8333, 'ro', latlon=True)
m.plot(3.31667, 45.5667, 'ro', latlon=True)
m.plot(3.15, 45.7333, 'ro', latlon=True)
m.plot(3.92195, 45.5003, 'ro', latlon=True)
m.plot(3.31667, 45.4833, 'ro', latlon=True)
m.plot(2.83333, 45.8333, 'ro', latlon=True)
m.plot(2.53333, 45.5, 'ro', latlon=True)
m.plot(3.36667, 45.6833, 'ro', latlon=True)
m.plot(3.21667, 45.5833, 'ro', latlon=True)
m.plot(3.43333, 45.7417, 'ro', latlon=True)
m.plot(3.79167, 45.4667, 'ro', latlon=True)
m.plot(3.2, 45.6667, 'ro', latlon=True)
m.plot(3.77139, 45.4498, 'ro', latlon=True)
m.plot(3.21667, 45.6167, 'ro', latlon=True)
m.plot(3.2, 45.6333, 'ro', latlon=True)
m.plot(3.28333, 45.65, 'ro', latlon=True)
m.plot(3.38333, 46, 'ro', latlon=True)
m.plot(3.3, 45.6, 'ro', latlon=True)
m.plot(3.2, 46.0167, 'ro', latlon=True)
m.plot(3.53333, 45.5167, 'ro', latlon=True)
m.plot(3.4, 45.55, 'ro', latlon=True)
m.plot(3.66667, 45.6, 'ro', latlon=True)
m.plot(3.16667, 45.55, 'ro', latlon=True)
m.plot(3.11667, 45.95, 'ro', latlon=True)
m.plot(3.01667, 46.1167, 'ro', latlon=True)
m.plot(2.93333, 46.0833, 'ro', latlon=True)
m.plot(3.05, 46.0833, 'ro', latlon=True)
m.plot(3.55, 45.4167, 'ro', latlon=True)
m.plot(3.51667, 45.9667, 'ro', latlon=True)
m.plot(2.86667, 45.8833, 'ro', latlon=True)
m.plot(2.63333, 46.05, 'ro', latlon=True)
m.plot(2.91667, 46.1333, 'ro', latlon=True)
m.plot(3.38333, 46.05, 'ro', latlon=True)
m.plot(2.83333, 45.9333, 'ro', latlon=True)
m.plot(3.51667, 45.8167, 'ro', latlon=True)
m.plot(2.64584, 45.9139, 'ro', latlon=True)
m.plot(2.56667, 45.75, 'ro', latlon=True)
m.plot(3.06667, 45.8167, 'ro', latlon=True)
m.plot(3.11667, 45.6667, 'ro', latlon=True)
m.plot(3.01667, 45.5667, 'ro', latlon=True)
m.plot(3.56667, 45.45, 'ro', latlon=True)
m.plot(3.12639, 45.4037, 'ro', latlon=True)
m.plot(3.08333, 45.4, 'ro', latlon=True)
m.plot(3.06667, 45.5833, 'ro', latlon=True)
m.plot(3.01667, 45.9333, 'ro', latlon=True)
m.plot(3.23333, 45.8333, 'ro', latlon=True)
m.plot(3.1, 45.7333, 'ro', latlon=True)
m.plot(3.75, 45.6667, 'ro', latlon=True)
m.plot(2.94084, 45.5517, 'ro', latlon=True)
m.plot(2.56667, 45.65, 'ro', latlon=True)
m.plot(2.76667, 46.1167, 'ro', latlon=True)
m.plot(2.87722, 45.9695, 'ro', latlon=True)
m.plot(3.3975, 45.9259, 'ro', latlon=True)
m.plot(3.28333, 45.45, 'ro', latlon=True)
m.plot(3.26667, 45.8833, 'ro', latlon=True)
m.plot(2.63333, 45.5, 'ro', latlon=True)
m.plot(3.2, 45.4333, 'ro', latlon=True)
m.plot(2.75861, 45.8414, 'ro', latlon=True)
m.plot(3.46667, 45.4167, 'ro', latlon=True)
m.plot(3.15, 45.3833, 'ro', latlon=True)
m.plot(3.05, 45.85, 'ro', latlon=True)
m.plot(2.63333, 45.7833, 'ro', latlon=True)
m.plot(3.51667, 45.65, 'ro', latlon=True)
m.plot(3.26139, 45.835, 'ro', latlon=True)
m.plot(3.63333, 45.3667, 'ro', latlon=True)


m.plot(3.2, 45.7333, 'bo', latlon=True) # le Cendre

plt.title("title")
plt.show()
