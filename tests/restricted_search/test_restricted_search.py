# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

import requests

restricted_search = solr_core('solr_process', 'restricted_search')
solr = solr('restricted_search')


def test_edismax_query(solr):
    solr.add([{'id': '1', 'title': 'bananas', 'allowed_to_read': 'john'}])
    assert 1 == requests.get(
        'http://localhost:18983/solr/restricted_search/' +
        'select?' +
        '&q=title:bananas' +
        '&qf=title' +
        '&wt=json'
    ).json()['response']['numFound']
