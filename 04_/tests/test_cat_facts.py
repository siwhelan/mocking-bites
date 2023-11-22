from unittest.mock import Mock
from lib.cat_facts import CatFacts


def test_cat_facts_provide():
    mock_requester = Mock()
    fact1 = "Cats sleep 70% of their lives."
    mock_requester.get.return_value.json.return_value = {"fact": fact1}

    cat_facts = CatFacts(requester=mock_requester)
    result = cat_facts.provide()
    assert result == f"Cat fact: {fact1}"
