# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

recent_content = solr_core('solr_process', 'recent_content')
solr = solr('recent_content')


def test_recent_content(solr):
    solr.add([{'id': '1', 'title': 'bananas'}])
    solr.add([{'id': '2', 'title': 'bananas'}])
    assert 2 == solr.search('title:bananas').hits
    assert [1,2] == [x.id for x in solr.search('title:bananas')]

def test_recent_content_with_effective(solr):
    solr.add([{'id': '1', 'title': 'bananas', 'effective': '1970/12/31 00:00:00 UTC'}])
    solr.add([{'id': '2', 'title': 'bananas', 'effective': '2023/01/01 00:00:00 UTC'}])
    assert 2 == solr.search('title:bananas').hits
    assert [2,1] == [x.id for x in solr.search('title:bananas')]
    # assert 1 == solr.search('title:bananas')[1].id
    # assert 2 == solr.search('title:bananas')[0].id
