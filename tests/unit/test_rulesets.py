import pytest

from rules.predicates import always_false, always_true
from rules.rulesets import (
    RuleSet,
    add_rule,
    default_rules,
    remove_rule,
    rule_exists,
    set_rule,
)
from rules.rulesets import test_rule as _test_rule


def test_shared_ruleset():
    add_rule("somerule", always_true)
    assert "somerule" in default_rules
    assert rule_exists("somerule")
    assert _test_rule("somerule")

    with pytest.raises(KeyError):
        add_rule("somerule", always_false)

    set_rule("somerule", always_false)
    assert not _test_rule("somerule")

    remove_rule("somerule")
    assert not rule_exists("somerule")


def test_ruleset():
    ruleset = RuleSet()
    ruleset.add_rule("somerule", always_true)
    assert "somerule" in ruleset
    assert ruleset.rule_exists("somerule")
    assert ruleset.test_rule("somerule")

    with pytest.raises(KeyError):
        ruleset.add_rule("somerule", always_true)

    ruleset.set_rule("somerule", always_false)
    assert not ruleset.test_rule("somerule")

    ruleset.remove_rule("somerule")
    assert not ruleset.rule_exists("somerule")
