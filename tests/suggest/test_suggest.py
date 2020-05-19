# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

import json

suggest = solr_core("solr_process", "suggest")
solr = solr("suggest")


def test_suggest(solr):
    # http://localhost:18983/solr/suggest/suggest?suggest=true&suggest.build=true&suggest.dictionary=mySuggester&suggest.q=b&suggest.cfq=memory
    solr.add([{"id": "1", "title": "bananas"}])
    solr._select(params={"q": "b", "wt": "json"}, handler="suggest")

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
