"""
Simple Bell state demo using Qiskit (v1.x).

Features:
- Bell pair creation
- Simulation with measurement counts
- Statevector visualization
- Bloch sphere plot
- Entanglement check
- Fidelity comparison with ideal Bell state
- Circuit diagram display
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector, state_fidelity
import matplotlib.pyplot as plt


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
    print("\n🔹 Statevector:\n", sv)
    return sv


def show_bloch_sphere(statevector):
    print("\n🔹 Bloch Sphere Visualization:")
    plot_bloch_multivector(statevector)
    plt.show()


def is_entangled(statevector):
    entangled = not statevector.is_product_state()
    print(f"\n🔹 Entangled: {'Yes' if entangled else 'No'}")
    return entangled


def check_fidelity(statevector):
    bell_state = Statevector([1/2**0.5, 0, 0, 1/2**0.5])
    fidelity = state_fidelity(statevector, bell_state)
    print(f"\n🔹 Fidelity with ideal Bell state: {fidelity:.4f}")
    return fidelity


def show_circuit_diagram(qc):
    print("\n🔹 Quantum Circuit Diagram:")
    qc.draw(output='mpl')
    plt.show()


if __name__ == "__main__":
    qc = create_bell_circuit()
    counts = simulate_counts(qc)
    statevector = show_statevector(qc)

    print("\n🔹 Bell State Measurement Results:", counts)
    plot_histogram(counts)
    plt.show()

    show_bloch_sphere(statevector)
    is_entangled(statevector)
    check_fidelity(statevector)
    show_circuit_diagram(qc)
