from app.main import get_human_age


def test_should_return_zero_for_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_before_fifteen() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_age_is_fifteen() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_until_twenty_three() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_age_is_twenty_four() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_until_next_conversion() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_should_convert_before_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_convert_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]
