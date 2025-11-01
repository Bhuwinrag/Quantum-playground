import pytest
from src.bell_state import create_bell_circuit, simulate_counts

def test_bell_counts():
    """
    Test that the Bell state circuit produces mostly '00' and '11' outcomes,
    indicating entanglement. Accepts small statistical deviations.
    """
    shots = 512
    qc = create_bell_circuit()
    counts = simulate_counts(qc, shots=shots)

    # Extract probabilities
    p00 = counts.get("00", 0) / shots
    p11 = counts.get("11", 0) / shots
    total_prob = p00 + p11

    # Log for debugging
    print(f"\nTest Bell Counts:\nCounts: {counts}\nP(00): {p00:.3f}, P(11): {p11:.3f}, Total: {total_prob:.3f}")

    # Assert that the Bell state yields mostly '00' and '11'
    assert total_prob > 0.9, "❌ Bell measurement probabilities not as expected (should be > 90%)"
