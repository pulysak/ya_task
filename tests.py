from main import get_unique_elements, remove_zeros


def test_get_unique_elements():
    # arrange
    l1 = [1, 2, 3, 4, 5]
    l2 = [4, 5, 6]
    expected = [1, 2, 3]

    # act
    result = get_unique_elements(l1=l1, l2=l2)

    # assert
    assert result == expected


test_get_unique_elements()


def test_remove_zeros():
    # arrange
    l = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]
    expected = [1, 4, 5, 6, 7, 8, -4]

    # act
    remove_zeros(l)

    # assert
    assert l == expected


def test_remove_zeros__all_zeros():
    # arrange
    l = [0, 0, 0, 0]
    expected = []

    # act
    remove_zeros(l)

    # assert
    assert l == expected


test_remove_zeros__all_zeros()
