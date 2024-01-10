import numpy as np
import pytest


# need to load MESA-Web run output, for test loading
@pytest.fixture
def summary_frame():
    return np.array([0.0])
