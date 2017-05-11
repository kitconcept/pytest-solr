# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

spellcheck = solr_core('solr_process', 'spellcheck')
solr = solr('spellcheck')


def test_spellcheck_attribute_is_included(solr):
    solr.add([{'id': '1', 'title': 'bananas'}])
    assert {
        u'bananos': {
            u'numFound': 1,
            u'suggestion': [u'bananas'],
            u'startOffset': 6,
            u'endOffset': 13
        }
    } == solr.search('title:bananos').spellcheck.get('suggestions')
