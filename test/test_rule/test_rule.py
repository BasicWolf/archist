from rule.rule import Rule, ValidResult


def test_rule_has_valid_result():
    assert Rule().validate() == ValidResult()
