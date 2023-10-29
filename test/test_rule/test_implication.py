from archist.rule.be_rule import be
from archist.rule.evaluation import Fail, Ok
from archist.rule.implication import Implication
from archist.rule.source.modules import modules


def test_implication_evaluates_successfully(
    a_basic_module
):
    assert Ok() == Implication(
        modules,
        be(lambda _: True)
    ).evaluate([
        a_basic_module
    ])


def test_implication_fails_with_reasons(
    a_basic_module
):
    failed_implication = Implication(
        modules,
        be(lambda _: False)
    ).evaluate([a_basic_module])

    assert isinstance(failed_implication, Fail)
    assert "was not as expected" in failed_implication.reason
