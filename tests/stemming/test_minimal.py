# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

stemming = solr_core('solr_process', 'stemming')
solr = solr('stemming')


def test_exact_term_match(solr):
    solr.add([{'id': '1', 'title': 'bananas'}])
    assert 1 == solr.search('title:bananas').hits
