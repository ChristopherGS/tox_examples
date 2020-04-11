from squarer.ml_squarer import square


def test_ml_squarer_does_not_produce_negative_numbers():
    # When
    subject = square()

    # Then
    assert subject > 0
