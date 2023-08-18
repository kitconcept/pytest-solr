# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr
import json

recent_content = solr_core('solr_process', 'recent_content')
solr = solr('recent_content')


def test_recent_content_default_order(solr):
    solr.add([{'id': '1', 'title': 'bananas'}])
    solr.add([{'id': '2', 'title': 'bananas'}])
    result = solr.search('title:bananas')
    assert 2 == result.hits
    assert ['1','2'] == [x['id'] for x in result.raw_response['response']['docs']]

def test_recent_content_rank_newer_content_first(solr):
    solr.add([{'id': '1', 'title': 'bananas', 'effective': '1990-02-23T17:20:00Z'}])
    solr.add([{'id': '2', 'title': 'bananas', 'effective': '2020-02-23T17:20:00Z'}])
    solr.add([{'id': '3', 'title': 'bananas', 'effective': '2023-02-23T17:20:00Z'}])
    query = 'title:bananas AND _val_:"recip(rord(effective),1,5,1)"'
    result = json.loads(solr._select(params={"q": query, "wt": "json", "fl": "id,title,effective,recip(rord(effective),1,5,1)"}))
    assert 3 == result['response']['numFound']
    assert ['3', '2', '1'] == [x['id'] for x in result['response']['docs']]
    assert [5.0, 2.5, 1.6666666] == [x['recip(rord(effective),1,5,1)'] for x in result['response']['docs']]

    # recip(x,m,a,b) = a / (m*x + b),
    # recip(x, 1, 100, 100)
    # = 100 / (1 * x) + 100
    # id=1 -> 1.6666666
    # id=2 -> 2.5
    # id=3 -> 5.0

def test_newer_content_trumps_term_in_title_twice(solr):
    solr.add([{'id': '1', 'title': 'bananas', 'effective': '2023-02-23T17:20:00Z'}])
    solr.add([{'id': '2', 'title': 'bananas bananas', 'effective': '2015-02-23T17:20:00Z'}])
    query = 'title:bananas AND _val_:"recip(rord(effective),1,5,1)"'
    result = json.loads(solr._select(params={"q": query, "wt": "json", "fl": "id,title,effective,recip(rord(effective),1,5,1)"}))
    assert 2 == result['response']['numFound']
    assert ['1', '2'] == [x['id'] for x in result['response']['docs']]
    # assert [5.0, 2.5, 1.6666666] == [x['recip(rord(effective),1,5,1)'] for x in result['response']['docs']]
