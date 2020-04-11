from .squarer import square


def test_square():
    # When
    subject = square(4)

    # Then
    assert subject == 16
