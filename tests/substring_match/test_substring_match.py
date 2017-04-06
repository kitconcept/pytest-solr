# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

substring_match = solr_core('solr_process', 'substring_match')
solr = solr('substring_match')


def test_exact_term_match(solr):
    solr.add([{'id': '1', 'title': 'bananas'}])
    assert 1 == solr.search('title:bananas').hits


def test_prefix_match(solr):
    solr.add([{'id': '1', 'title': 'bananas'}])
    assert 1 == solr.search('title:ban').hits


# def test_suffix_match(solr):
#     solr.add([{'id': '1', 'title': 'bananas'}])
#     assert 1 == solr.search('title:nas').hits

# def test_search_ignores_lowercase(solr):
#     solr.add([{'id': '1', 'title': 'Bananas'}])
#     assert 1 == solr.search('title:bananas').hits

# def test_search_ignores_uppercase(solr):
#     solr.add([{'id': '1', 'title': 'bananas'}])
#     assert 1 == solr.search('title:Bananas').hits

# def test_synonyms_apples_and_bananas_are_fruits(solr):
#     solr.add([
#         {'id': '1', 'title': 'bananas'},
#         {'id': '2', 'title': 'apples'}
#     ])
#     assert 2 == solr.search('title:fruits').hits


# def test_synonyms_fruits_are_not_apples(solr):
#     solr.add([{'id': '1', 'title': 'fruits'}])
#     assert 0 == solr.search('title:apples').hits


# def test_search_ignores_stopwords(solr):
#     solr.add([{'id': '1', 'title': 'apples and bananas'}])
#     assert 0 == solr.search('title:and').hits


# def test_search_ignores_punctuation(solr):
#     solr.add([
#         {'id': '1', 'title': 'Colorless, Green; Ideas. Sleep? Furiously!'}
#     ])
#     assert 1 == solr.search('title:Colorless Green Ideas Sleep Furiously').hits


# def test_search_replaces_non_ascii_characters(solr):
#     solr.add([{'id': '1', 'title': u'Cölorless Grêen Idéaß Slèep Furiously'}])
#     assert 1 == solr.search('title:Colorless Green Ideass Sleep Furiously').hits  # noqa


# def test_search_ignores_whitespace(solr):
#     index = '  Colorless Green Ideas Sleep Furiously         '
#     query = 'Colorless Green Ideas Sleep Furiously'


# def test_search_ignores_inner_whitespace(solr):
#     index = 'Colorless    Green Ideas Sleep Furiously'
#     query = 'Colorless Green Ideas Sleep Furiously'


# def test_substring_finds_prefix_in_phrase(solr):
#     solr.add([{
#         'id': '1',
#         'substring_match': 'Colorless Green Ideas Sleep Furiously',
#     }])

#     result = solr.search(
#         'substring_match:"Color"'
#     )

#     assert 1 == result.hits
#     assert u'Colorless Green Ideas Sleep Furiously' == \
#         [x.get('substring_match') for x in result][0]


# def test_substring_match_does_not_find_prefix_in_search(solr):
#     """When N-grams are created during search. The result contains elements for
#        all possible substrings of the search query. This is not what the user
#        would expect.
#     """
#     solr.add([{
#         'id': '1',
#         'substring_match': 'Colorless Green Ideas Sleep Furiously',
#     }])
#     solr.add([{
#         'id': '2',
#         'substring_match': 'Color',
#     }])

#     result = solr.search(
#         'substring_match:"Colorless"'
#     )

#     assert 1 == result.hits
#     assert u'Colorless Green Ideas Sleep Furiously' == \
#         [x.get('substring_match') for x in result][0]
