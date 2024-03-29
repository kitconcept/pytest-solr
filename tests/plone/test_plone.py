# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

plone = solr_core("solr_process", "plone")
solr = solr("plone")


def test_title(solr):
    solr.add([{"id": "1", "Title": "bananas"}])
    assert 1 == solr.search("Title:bananas").hits


def test_description(solr):
    solr.add([{"id": "1", "Description": "bananas"}])
    assert 1 == solr.search("Description:bananas").hits


def test_search_ignores_lowercase(solr):
    solr.add([{"id": "1", "Title": "Bananas"}])
    assert 1 == solr.search("Title:bananas").hits


def test_search_ignores_uppercase(solr):
    solr.add([{"id": "1", "Title": "bananas"}])
    assert 1 == solr.search("Title:Bananas").hits


def test_title_indexed_in_searchable_text(solr):
    solr.add([{"id": "1", "Title": "bananas"}])
    assert 1 == solr.search("default:bananas").hits


def test_description_indexed_in_searchable_text(solr):
    solr.add([{"id": "1", "Description": "bananas"}])
    assert 1 == solr.search("default:bananas").hits


def test_creator_indexed_in_searchable_text(solr):
    solr.add([{"id": "1", "Creator": "bananas"}])
    assert 1 == solr.search("default:bananas").hits
