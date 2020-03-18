# -*- coding: utf-8 -*

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=missing-docstring,invalid-name,no-member
# pylint: disable=attribute-defined-outside-init

from qiskit import QuantumRegister
from qiskit import BasicAer
try:
    from qiskit.compiler import transpile
except ImportError:
    from qiskit.transpiler import transpile
from .utils import build_qft_circuit


class QftTranspileBench:
    params = [1, 2, 3, 5, 8, 13, 14]

    def setup(self, n):
        self.circuit = build_qft_circuit(n)
        self.sim_backend = BasicAer.get_backend('qasm_simulator')

    def time_simulator_transpile(self, _):
        transpile(self.circuit, self.sim_backend)

    def time_ibmq_backend_transpile(self, _):
        # Run with ibmq_16_melbourne configuration
        coupling_map = [[1, 0], [1, 2], [2, 3], [4, 3], [4, 10], [5, 4],
                        [5, 6], [5, 9], [6, 8], [7, 8], [9, 8], [9, 10],
                        [11, 3], [11, 10], [11, 12], [12, 2], [13, 1],
                        [13, 12]]
        transpile(self.circuit,
                  basis_gates=['u1', 'u2', 'u3', 'cx', 'id'],
                  coupling_map=coupling_map)
