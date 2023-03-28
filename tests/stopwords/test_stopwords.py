# -*- coding: utf-8 -*-
from pytest_solr.factories import solr, solr_core

stopwords = solr_core("solr_process", "stopwords")
solr = solr("stopwords")


def test_stopwords_are_not_included_in_search_results(solr):
    solr.add([{"id": "1", "title": "Institut für Aeroelastik"}])
    assert 1 == solr.search("title:Institut").hits
    assert 1 == solr.search("title:Aeroelastik").hits
    assert 0 == solr.search("title:für").hits


def test_stopwords_are_not_included_in_search_results_case_insensitive(solr):
    solr.add([{"id": "1", "title": "Institut für Aeroelastik"}])
    assert 0 == solr.search("title:Für").hits


def test_stopwords_are_ignored(solr):
    solr.add([{"id": "1", "title": "Institut für Aeroelastik"}])
    solr.add([{"id": "2", "title": "Institut Aeroelastik"}])
    assert 2 == solr.search("title:Institut für Aeroelastik").hits
