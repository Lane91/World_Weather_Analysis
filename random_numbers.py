import random


def latitudes(size):
    """Generate a list of random latitude values.

    Each value will be in the range [-90, 90).

    Args:
        size (int): Number of latitude values to generate.

    Returns:
        list[float]: Random latitude values within the range.
    """
    return [random.random() * 180 - 90 for _ in range(size)]
