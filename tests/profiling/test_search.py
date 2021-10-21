import time
import unittest
import numpy as np
from mpl_plotter.two_d import comparison

from matmos import ISA


def profile(f):
    def profiled(*args, **kwargs):
        n = 10
        t0 = time.time()
        for i in range(n):
            rs = f(*args, **kwargs)
        rt = (time.time() - t0)/n
        print(f'Average execution time ({n} run{"s" if n>1 else ""}): {rt:.10f} s')
        return rs, rt
    return profiled


class Profilers(unittest.TestCase):

    @profile
    def f_binary(self, **kwargs):
        return ISA(**kwargs)

    @profile
    def f_numpy(self, **kwargs):
        return ISA(**kwargs, solve=False)

    def test_1(self):
        self.f_binary(
                      # p=np.array([0, 99000]),
                      p=99000,
                      n=1000000
                      )

    def test_2(self):
        self.f_numpy (
                      # p=np.array([0, 99000]),
                      p=99000,
                      n=1000000
                      )

    def test_profile_precision(self):
        n = np.linspace(1, 100000, 10).astype(int)
        rt_b = np.zeros(n.size)
        rt_n = np.zeros(n.size)
        for i in range(n.size):
            print(f'%{i/n.size*100:.0f}')
            p = 99000
            _, rt_b[i] = self.f_binary(p=p, n=n[i])
            _, rt_n[i] = self.f_numpy(p=p, n=n[i])

        comparison(n,
                   [rt_b, rt_n],
                   plot_labels=['BS', 'NS'],
                   y_tick_ndecimals=5, y_tick_number=5,
                   x_tick_ndecimals=0, x_tick_number=2,
                   y_label='runtime [s]',
                   x_label='$n$',
                   figsize=(6, 4),
                   legend_loc=(0.765, 0.7),
                   aspect=1,
                   top=0.95,
                   bottom=0.15,
                   left=0.13,
                   right=0.75,
                   hspace=0.35,
                   wspace=0.6,
                   show=True
                   )

    def test_profile_array_size(self):
        n = np.linspace(1, 1000, 10).astype(int)
        rt_b = np.zeros(n.size)
        rt_n = np.zeros(n.size)
        for i in range(n.size):
            print(f'%{i/n.size*100}')
            p = np.linspace(101325, 0, n[i])
            _, rt_b[i] = self.f_binary(p=p, n=100)
            _, rt_n[i] = self.f_numpy (p=p, n=100)

        comparison(n,
                   [rt_b, rt_n],
                   plot_labels=['Binary search', 'NumPy search'],
                   y_tick_ndecimals=5, y_tick_number=5,
                   x_tick_ndecimals=0, x_tick_number=4,
                   y_label='runtime [s]',
                   x_label='$n$',
                   legend_loc=(0.675, 0.195),
                   aspect=1,
                   top=1.0,
                   bottom=0.055,
                   left=0.165,
                   right=0.75,
                   hspace=0.35,
                   wspace=0.6,
                   show=True)
