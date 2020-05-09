# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr


def test_solr_process(solr_process):
    assert solr_process.get("process").poll() is None


def test_solr_core(solr_core):
    assert solr_core


# def test_solr(solr):
#     assert 0 == solr.search('bananas').hits


# solr_core_custom = solr_core('solr_process', 'minimal')
# solr_custom = solr('solr_core_custom')


# def test_solr_core_custom(solr_custom):
#     solr_custom.add([{'id': '1', 'title': 'bananas'}])
#     assert 1 == solr_custom.search('title:bananas').hits
