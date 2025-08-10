from random_numbers import latitudes


def test_latitudes_length():
    size = 10
    result = latitudes(size)
    assert len(result) == size


def test_latitudes_range():
    result = latitudes(100)
    assert all(-90 <= lat < 90 for lat in result)
