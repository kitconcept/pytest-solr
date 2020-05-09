# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

minimal = solr_core("solr_process", "minimal")
solr = solr("minimal")


def test_exact_term_match(solr):
    solr.add([{"id": "1", "title": "bananas"}])
    assert 1 == solr.search("title:bananas").hits
