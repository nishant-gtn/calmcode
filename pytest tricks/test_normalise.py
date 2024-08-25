import time
import pytest
import numpy as np


def normalize(X):
    return (X - X.min()) / (X.max() - X.min())


def threshold(X, min_val=-1, max_val=1):
    result = np.where(X <= min_val, min_val, X)
    return np.where(result >= max_val, max_val, result)


@pytest.fixture(
    params=[(1, 1), (2, 2), (3, 3), (4, 4)], ids=lambda d: f"rows: {d[0]} cols: {d[1]}"
)
def random_numpy_array(request):
    return np.random.normal(request.param)


# add the `slow` mark to the test.
@pytest.mark.slow
@pytest.mark.parametrize("func", [normalize, threshold], ids=lambda d: d.__name__)
def test_shape_same(func, random_numpy_array):
    time.sleep(1)
    X_norm = func(random_numpy_array)
    assert random_numpy_array.shape == X_norm.shape


def test_min_max_normalise(random_numpy_array):
    X_norm = normalize(random_numpy_array)
    assert X_norm.min() == 0.0
    assert X_norm.max() == 1.0


@pytest.mark.parametrize("min_val", [-3, -2, -1], ids=lambda x: f"min_val:{x}")
@pytest.mark.parametrize("max_val", [3, 2, 1], ids=lambda x: f"max_val:{x}")
def test_min_max_threshold(random_numpy_array, min_val, max_val):
    X_norm = threshold(random_numpy_array, min_val, max_val)
    assert X_norm.min() >= min_val
    assert X_norm.max() <= max_val
