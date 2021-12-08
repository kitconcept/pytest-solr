# -*- coding: utf-8 -*-
from pytest_solr.factories import solr, solr_core

suffix_search = solr_core("solr_process", "suffix_search")
solr = solr("suffix_search")


def test_exact_term_match(solr):
    solr.add([{"id": "1", "title": "bananas"}])
    assert 1 == solr.search("title:bananas").hits
