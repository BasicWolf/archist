from archist.predicate.be import BePredicate


def test_be_predicate_succeeds_when_supplied_with_valid_argument():
    assert BePredicate[str](lambda s: s != '').test('non-empty-string')


def test_be_predicate_fails_when_supplied_with_invalid_argument():
    assert not BePredicate[str](lambda s: s != '').test('')
