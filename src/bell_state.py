"""
Simple Bell state demo using Qiskit (v1.x).
Creates a Bell pair, simulates it, prints counts, and shows the statevector.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

from qiskit.visualization import plot_bloch_multivector

def show_bloch_sphere(statevector):
    plot_bloch_multivector(statevector)
    plt.show()

def create_bell_circuit():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc


def simulate_counts(qc, shots=1024):
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=shots)
    result = job.result()
    counts = result.get_counts()
    return counts


def show_statevector(qc):
    sv = Statevector.from_instruction(qc.remove_final_measurements(inplace=False))
    print("\nStatevector:\n", sv)
    return sv


if __name__ == "__main__":
    qc = create_bell_circuit()
    counts = simulate_counts(qc)
    show_statevector(qc)

    print("\nBell State Measurement Results:", counts)
    plot_histogram(counts)
    plt.show()
