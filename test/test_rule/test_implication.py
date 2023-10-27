from archist.rule.be import be
from archist.rule.evaluation_rule import Fail, Ok
from archist.rule.implication import Implication


def test_implication_evaluates_successfully(
    dummy_source,
    build_basic_module
):
    assert Implication(
        dummy_source,
        be(lambda module: module.name.startswith('mod_'))
    ).evaluate([
        build_basic_module(module_name='mod_first'),
        build_basic_module(module_name='mod_second')
    ]) == Ok()


def test_implication_fails_with_reasons(
    dummy_source,
    a_basic_module
):
    assert Implication(
        dummy_source,
        be(lambda _: False)
    ).evaluate([a_basic_module]) == Fail()
