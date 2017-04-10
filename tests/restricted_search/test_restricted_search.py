# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

restricted_search = solr_core('solr_process', 'restricted_search')
solr = solr('restricted_search')


def test_exact_term_match(solr):
    solr.add([{'id': '1', 'title': 'bananas'}])
    assert 1 == solr.search('title:bananas').hits
