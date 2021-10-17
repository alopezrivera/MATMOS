import numpy as np

from mpl_plotter.two_d import panes

from matmos import ISA


h = np.linspace(0, 85.99, 10000)

m = ISA(h)

t = m.t
p = m.p
d = m.d

panes([
        t,
        p/1000,
        d
      ],
      h,
      x_labels=['T [K]', 'p [kPa]', r'$\rho$ [kg/m$^3$]'],
      y_label='h [km]',
      plot_label='ISA',
      legend_loc=(0.875, 0.8),
      aspect=1,
      show=True,
      x_tick_ndecimals=2,
      x_tick_number=4,
      y_tick_number=4,
      color='black',
      )
