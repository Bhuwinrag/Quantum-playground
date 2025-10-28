from src.bell_state import create_bell_circuit, simulate_counts

def test_bell_counts():
    qc = create_bell_circuit()
    counts = simulate_counts(qc, shots=512)
    p00 = counts.get("00", 0) / 512
    p11 = counts.get("11", 0) / 512
    assert p00 + p11 > 0.9, "Bell measurement probabilities not as expected"
