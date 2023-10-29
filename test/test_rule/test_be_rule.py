from archist.rule import be


def test_be_filter():
    be_rule = be(lambda s: s == 'Hello')
    assert ['Hello'] == list(be_rule.filter(['Hello', 'World']))
