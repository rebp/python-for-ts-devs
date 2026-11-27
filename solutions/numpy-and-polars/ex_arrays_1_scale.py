"""Reference solution for exercise 12.2-1."""

import numpy as np
from numpy.typing import NDArray


def scale_nonnegative(
    values: NDArray[np.float64], factor: float
) -> NDArray[np.float64]:
    """Scale and clip without mutating the input."""
    return np.maximum(values * factor, 0.0)
