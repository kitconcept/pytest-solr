# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

import json

suggest_n_grams = solr_core("solr_process", "suggest_n_grams")
solr = solr("suggest_n_grams")


def test_suggest_single_term(solr):
    # http://localhost:18983/solr/suggest/suggest?suggest=true&suggest.build=true&suggest.dictionary=mySuggester&suggest.q=b&suggest.cfq=memory
    solr.add([{"id": "1", "title": "bananas"}])

    assert [
        1,
        json.loads(
            solr._select(params={"q": "ba", "wt": "json"}, handler="suggest_topic")
        )
        .get("response")
        .get("numFound"),
    ]
    assert [
        u"bananas",
        json.loads(
            solr._select(params={"q": "ba", "wt": "json"}, handler="suggest_topic")
        )
        .get("response")
        .get("docs")[0]
        .get("title"),
    ]


def test_suggest_multiple_terms(solr):
    solr.add([{"id": "1", "title": "colorless green ideas"}])
    solr.add([{"id": "2", "title": "green ideas"}])

    assert [
        2,
        json.loads(
            solr._select(params={"q": "green", "wt": "json"}, handler="suggest_topic")
        )
        .get("response")
        .get("numFound"),
    ]
    assert [
        u"colorless green ideas",
        json.loads(
            solr._select(params={"q": "green", "wt": "json"}, handler="suggest_topic")
        )
        .get("response")
        .get("docs")[0]
        .get("title"),
    ]


def test_suggest_multiple_terms_boost_direct_matches(solr):
    solr.add([{"id": "1", "title": "colorless green ideas"}])
    solr.add([{"id": "2", "title": "green ideas"}])
    solr.add([{"id": "2", "title": "greener ideas"}])

    assert [
        3,
        json.loads(
            solr._select(params={"q": "green", "wt": "json"}, handler="suggest_topic")
        )
        .get("response")
        .get("numFound"),
    ]
    assert [
        u"green ideas",
        json.loads(
            solr._select(params={"q": "green", "wt": "json"}, handler="suggest_topic")
        )
        .get("response")
        .get("docs")[0]
        .get("title"),
    ]
    assert [
        u"colorless green ideas",
        json.loads(
            solr._select(params={"q": "green", "wt": "json"}, handler="suggest_topic")
        )
        .get("response")
        .get("docs")[0]
        .get("title"),
    ]
    assert [
        u"greener ideas",
        json.loads(
            solr._select(params={"q": "green", "wt": "json"}, handler="suggest_topic")
        )
        .get("response")
        .get("docs")[0]
        .get("title"),
    ]


def test_suggest_multiple_terms_unordered_suggestions(solr):
    # green -> colorless green
    # recognizes “shirts” as part of the phrase, like “men’s shirts,” and suggests it to the customer along with “women’s shirts,” “work shirts,” and other phrases that contain “men’s.”
    pass


def test_suggest_multiple_terms_ordered_suggestions(solr):
    # matches everything that contains a subphrase of the complete phrase as long as it’s in the correct order, i.e. “men’s shir,” but not “shirts me.”
    pass
