from fifteen import get_a, get_b, get_sum, assertion

def test_get_a():
    assert get_a(2) == "133"
    assert get_a(0) == "1"

def test_get_b():
    assert get_b(0) == "5"
    assert get_b(3) == "5333"

def test_get_sum():
    assert get_sum(1, 5) == 15
    assert get_sum(13, 53) == 1353

def test_assertion():
    assert assertion(15, 15) == "pass"
    assert assertion(12, 1) == "fails"

