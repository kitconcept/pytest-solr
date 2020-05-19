# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

import json

suggest = solr_core("solr_process", "suggest")
solr = solr("suggest")


def test_suggest_single_term(solr):
    # http://localhost:18983/solr/suggest/suggest?suggest=true&suggest.build=true&suggest.dictionary=mySuggester&suggest.q=b&suggest.cfq=memory
    solr.add([{"id": "1", "title": "bananas"}])

    assert [
        1,
        json.loads(solr._select(params={"q": "b", "wt": "json"}, handler="suggest"))
        .get("suggest")
        .get("mySuggester")
        .get("b")
        .get("numFound"),
    ]
    assert [
        u"bananas",
        json.loads(solr._select(params={"q": "b", "wt": "json"}, handler="suggest"))
        .get("suggest")
        .get("mySuggester")
        .get("b")
        .get("suggestions")[0]
        .get("term"),
    ]


def test_suggest_multiple_terms(solr):
    # colorless -> colorless green
    solr.add([{"id": "1", "title": "colorless green ideas"}])
    solr.add([{"id": "2", "title": "green ideas"}])
    solr.add([{"id": "3", "title": "ideas"}])

    assert [
        1,
        json.loads(solr._select(params={"q": "color", "wt": "json"}, handler="suggest"))
        .get("suggest")
        .get("mySuggester")
        .get("color")
        .get("numFound"),
    ]
    assert [
        u"colorless green ideas",
        json.loads(solr._select(params={"q": "color", "wt": "json"}, handler="suggest"))
        .get("suggest")
        .get("mySuggester")
        .get("color")
        .get("suggestions")[0]
        .get("term"),
    ]


def test_suggest_multiple_terms_unordered_suggestions(solr):
    # green -> colorless green
    # recognizes “shirts” as part of the phrase, like “men’s shirts,” and suggests it to the customer along with “women’s shirts,” “work shirts,” and other phrases that contain “men’s.”
    pass


def test_suggest_multiple_terms_ordered_suggestions(solr):
    # matches everything that contains a subphrase of the complete phrase as long as it’s in the correct order, i.e. “men’s shir,” but not “shirts me.”
    pass
