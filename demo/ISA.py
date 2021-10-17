import numpy as np

from mpl_plotter import figure
from mpl_plotter.two_d import panes

from matmos import ISA


h = np.linspace(0, 85.99, 10000)

m = ISA(h)

t = m.t
p = m.p
d = m.d

fig = figure((10, 4))

panes([
        t,
        p/1000,
        d
      ],
      h,
      x_labels=['T [K]', 'p [kPa]', r'$\rho$ [kg/m$^3$]'],
      y_label='h [km]',
      aspect=1,
      fig=fig,
      show=True,
      x_tick_ndecimals=2,
      x_tick_number=4,
      y_tick_number=4,
      color='black',
      top=0.962,
      bottom=0.038,
      left=0.083,
      right=0.978,
      hspace=0.35,
      wspace=0.429
      )
