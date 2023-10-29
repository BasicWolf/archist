from archist.rule.evaluation import Ok, Fail


def pytest_assertrepr_compare(op, left, right):
    """An ugly PyTest assertion to test evaluation result

    We have to use `assert Ok() == evaluation` instead of simple
    `assert evaluation`, since as of PyTest 7.4.3 there is no hook
    for boolean checks.

    See discussion in https://github.com/pytest-dev/pytest/issues/5535
    """
    if isinstance(left, Ok) and isinstance(right, Fail) and op == "==":
        return [
            "Evaluation has failed for the following reason:",
            f"    {right.reason}"
        ]
