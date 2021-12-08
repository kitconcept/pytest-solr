# -*- coding: utf-8 -*-
from pytest_solr.factories import solr, solr_core

suffix_search = solr_core("solr_process", "suffix_search")
solr = solr("suffix_search")


def test_suffix_term_match(solr):
    solr.add([{"id": "1", "suffix": "bananas"}])
    assert 1 == solr.search("suffix:ananas").hits


def test_suffix_term_match_multiple_terms(solr):
    solr.add([{"id": "1", "suffix": "oranges and bananas"}])
    assert 1 == solr.search("suffix:ananas").hits
