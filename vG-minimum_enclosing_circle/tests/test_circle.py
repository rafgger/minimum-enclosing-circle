import numpy as np
from mec.circle import mec

def test_three_points():
    points = [np.array([0, 0]), np.array([0, 2]), np.array([2, 0])]
    center, radius = mec(points)
    assert np.allclose(np.linalg.norm(points[0] - center), radius, atol=1e-5)
    assert np.allclose(np.linalg.norm(points[1] - center), radius, atol=1e-5)
    assert np.allclose(np.linalg.norm(points[2] - center), radius, atol=1e-5)