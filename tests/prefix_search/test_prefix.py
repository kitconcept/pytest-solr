# -*- coding: utf-8 -*-
from pytest_solr.factories import solr, solr_core

prefix_search = solr_core("solr_process", "prefix_search")
solr = solr("prefix_search")


def test_prefix_term_match(solr):
    solr.add([{"id": "1", "prefix": "bananas"}])
    assert 1 == solr.search("prefix:banana").hits


def test_prefix_term_match_minimal_ngram_size(solr):
    """the minimal ngram size is 3"""
    solr.add([{"id": "1", "prefix": "bananas"}])
    assert 1 == solr.search("prefix:ban").hits


def test_prefix_term_do_not_match_below_minimal_ngram_size(solr):
    """the minimal ngram size is 3, a prefix with two characters should not match"""
    solr.add([{"id": "1", "prefix": "bananas"}])
    assert 0 == solr.search("prefix:ba").hits


def test_prefix_term_match_multiple_terms(solr):
    solr.add([{"id": "1", "prefix": "oranges and bananas"}])
    assert 1 == solr.search("prefix:banana").hits
