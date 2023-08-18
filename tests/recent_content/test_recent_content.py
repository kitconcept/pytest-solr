# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

recent_content = solr_core('solr_process', 'recent_content')
solr = solr('recent_content')


def test_recent_content_default_order(solr):
    solr.add([{'id': '1', 'title': 'bananas'}])
    solr.add([{'id': '2', 'title': 'bananas'}])
    result = solr.search('title:bananas')
    assert 2 == result.hits
    assert ['1','2'] == [x['id'] for x in result.raw_response['response']['docs']]

def test_recent_content_rank_newer_content_first(solr):
    solr.add([{'id': '1', 'title': 'bananas', 'effective': '1970/12/31 00:00:00 UTC'}])
    solr.add([{'id': '2', 'title': 'bananas', 'effective': '2023/01/01 00:00:00 UTC'}])
    result = solr.search('title:bananas AND _val_:"recip(ord(effective),1,100,100)"')
    assert 2 == result.hits
    assert ['2','1'] == [x['id'] for x in result.raw_response['response']['docs']]
