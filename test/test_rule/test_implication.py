from archist.rule.implication import Implication


def test_implication_successfully_evaluates_with_dummy_source_and_validator(
    dummy_source,
    dummy_validator
):
    assert Implication(dummy_source, dummy_validator).evaluate([])
