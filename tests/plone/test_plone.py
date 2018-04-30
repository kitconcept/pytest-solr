# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

minimal = solr_core('solr_process', 'minimal')
solr = solr('minimal')


def test_title(solr):
    solr.add([{'id': '1', 'Title': 'bananas'}])
    assert 1 == solr.search('Title:bananas').hits


def test_description(solr):
    solr.add([{'id': '1', 'Description': 'bananas'}])
    assert 1 == solr.search('Description:bananas').hits
