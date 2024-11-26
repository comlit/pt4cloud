import numpy as np
import time
from pt4cloud import pt4cloud_lite

# Mock benchmark function with delay
def mock_benchmark_function():
    """
    Mock benchmark function that returns normally distributed values with a small delay.
    """
    time.sleep(2)  # Simulate a delay of 0.1 seconds
    return np.random.normal(0, 1.2)

def test_pt4cloud_lite():
    """
    Test pt4cloud_lite with stable benchmark data.
    """
    data = pt4cloud_lite(
        benchmark_function=mock_benchmark_function,
        stability_probability=0.9,
        max_intervals=5,
        interval_duration=20,  # Shorter interval for testing
        interval_increase=0.5,
        sampling_portion=0.5,
        validate=True
    )
    assert data is not None, "Expected non-empty data for distribution."
    assert len(data) > 0, "Data collected should have more than zero entries."