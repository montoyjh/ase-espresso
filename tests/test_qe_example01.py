
# test adapted from Quantum Espresso PWASCF v.5.3.0 (svn rev. 11974)

from __future__ import print_function

import numpy as np

from ase.lattice import bulk
from ase.units import Rydberg, Bohr
from espresso import Espresso


def test_example01_al_scf_david():

    al = bulk('Al', 'fcc', 7.5 * Bohr)
    kpts = np.asarray([[0.0625000, 0.0625000, 0.0625000, 1.00],
                       [0.0625000, 0.0625000, 0.1875000, 3.00],
                       [0.0625000, 0.0625000, 0.3125000, 3.00],
                       [0.0625000, 0.0625000, 0.4375000, 3.00],
                       [0.0625000, 0.0625000, 0.5625000, 3.00],
                       [0.0625000, 0.0625000, 0.6875000, 3.00],
                       [0.0625000, 0.0625000, 0.8125000, 3.00],
                       [0.0625000, 0.0625000, 0.9375000, 3.00],
                       [0.0625000, 0.1875000, 0.1875000, 3.00],
                       [0.0625000, 0.1875000, 0.3125000, 6.00],
                       [0.0625000, 0.1875000, 0.4375000, 6.00],
                       [0.0625000, 0.1875000, 0.5625000, 6.00],
                       [0.0625000, 0.1875000, 0.6875000, 6.00],
                       [0.0625000, 0.1875000, 0.8125000, 6.00],
                       [0.0625000, 0.1875000, 0.9375000, 6.00],
                       [0.0625000, 0.3125000, 0.3125000, 3.00],
                       [0.0625000, 0.3125000, 0.4375000, 6.00],
                       [0.0625000, 0.3125000, 0.5625000, 6.00],
                       [0.0625000, 0.3125000, 0.6875000, 6.00],
                       [0.0625000, 0.3125000, 0.8125000, 6.00],
                       [0.0625000, 0.3125000, 0.9375000, 6.00],
                       [0.0625000, 0.4375000, 0.4375000, 3.00],
                       [0.0625000, 0.4375000, 0.5625000, 6.00],
                       [0.0625000, 0.4375000, 0.6875000, 6.00],
                       [0.0625000, 0.4375000, 0.8125000, 6.00],
                       [0.0625000, 0.4375000, 0.9375000, 6.00],
                       [0.0625000, 0.5625000, 0.5625000, 3.00],
                       [0.0625000, 0.5625000, 0.6875000, 6.00],
                       [0.0625000, 0.5625000, 0.8125000, 6.00],
                       [0.0625000, 0.6875000, 0.6875000, 3.00],
                       [0.0625000, 0.6875000, 0.8125000, 6.00],
                       [0.0625000, 0.8125000, 0.8125000, 3.00],
                       [0.1875000, 0.1875000, 0.1875000, 1.00],
                       [0.1875000, 0.1875000, 0.3125000, 3.00],
                       [0.1875000, 0.1875000, 0.4375000, 3.00],
                       [0.1875000, 0.1875000, 0.5625000, 3.00],
                       [0.1875000, 0.1875000, 0.6875000, 3.00],
                       [0.1875000, 0.1875000, 0.8125000, 3.00],
                       [0.1875000, 0.3125000, 0.3125000, 3.00],
                       [0.1875000, 0.3125000, 0.4375000, 6.00],
                       [0.1875000, 0.3125000, 0.5625000, 6.00],
                       [0.1875000, 0.3125000, 0.6875000, 6.00],
                       [0.1875000, 0.3125000, 0.8125000, 6.00],
                       [0.1875000, 0.4375000, 0.4375000, 3.00],
                       [0.1875000, 0.4375000, 0.5625000, 6.00],
                       [0.1875000, 0.4375000, 0.6875000, 6.00],
                       [0.1875000, 0.4375000, 0.8125000, 6.00],
                       [0.1875000, 0.5625000, 0.5625000, 3.00],
                       [0.1875000, 0.5625000, 0.6875000, 6.00],
                       [0.1875000, 0.6875000, 0.6875000, 3.00],
                       [0.3125000, 0.3125000, 0.3125000, 1.00],
                       [0.3125000, 0.3125000, 0.4375000, 3.00],
                       [0.3125000, 0.3125000, 0.5625000, 3.00],
                       [0.3125000, 0.3125000, 0.6875000, 3.00],
                       [0.3125000, 0.4375000, 0.4375000, 3.00],
                       [0.3125000, 0.4375000, 0.5625000, 6.00],
                       [0.3125000, 0.4375000, 0.6875000, 6.00],
                       [0.3125000, 0.5625000, 0.5625000, 3.00],
                       [0.4375000, 0.4375000, 0.4375000, 1.00],
                       [0.4375000, 0.4375000, 0.5625000, 3.00]])

    calc = Espresso(pw=15.0 * Rydberg, calculation='scf', kpts=kpts,
                    tprnfor=True, tstress=True, occupations='smearing',
                    smearing='marzari-vanderbilt', degauss=0.05)

    al.set_calcualtor(calc)

    print(calc.get_potential_energy())
