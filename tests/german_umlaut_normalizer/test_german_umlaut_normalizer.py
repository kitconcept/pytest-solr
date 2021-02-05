# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

german_umlaut_normalizer = solr_core("solr_process", "german_umlaut_normalizer")
solr = solr("german_umlaut_normalizer")


def test_search_for_title_without_umlaut(solr):
    solr.add([{"id": "1", "title": "Rate"}])

    assert 1 == solr.search("title:Rate").hits


def test_search_for_title(solr):
    solr.add([{"id": "1", "title": "Räte"}])

    assert 1 == solr.search("title:Räte").hits


def test_search_for_title_german_umlaut_normalizer(solr):
    solr.add([{"id": "1", "title": "Räte"}])

    assert 1 == solr.search("title:Raete").hits
