from archist.rule.evaluation import Ok, Fail


def test_ok_equals_ok():
    assert Ok() == Ok()


def test_ok_is_true():
    assert Ok()


def test_fail_is_false():
    assert not Fail("something went wrong")


def test_fail_equals_fail():
    assert Fail("a reason") == Fail("a reason")


def test_fail_not_equals_fail():
    assert Fail("a reason") != Fail("other reason")


def test_ok_is_not_fail():
    assert Ok() != Fail("something went wrong")
