# -*- coding: utf-8 -*-
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr

solr_core_custom = solr_core('solr_process', 'substring_match')
solr_custom = solr(
    'solr_core_custom', 
    [
        {'id': '1', 'title': 'bananas'},
        {'id': '2', 'title': 'apples'},
        {'id': '3', 'title': 'fruits'},
        {'id': '4', 'title': 'Colorless Green Ideas Sleep Furiously'},
        {'id': '5', 'title': 'Cölorless Grêen Idéaß Slèep Furiously'}
    ]
)

# @solr('solr_core_custom', {'id': '1', 'title': 'bananas'})
def test_term_match(solr_custom):
    assert 1 == solr_custom.search('title:bananas').hits

def test_prefix_match(solr_custom):
    assert 1 == solr_custom.search('title:ban').hits

# def test_suffix_match(solr_custom):
#     assert 1 == solr_custom.search('title:nas').hits

def test_synonyms_apples_bananas_are_fruits(solr_custom):
    assert 2 == solr_custom.search('title:fruits').hits

# def test_synonyms_fruits_are_not_apples(solr_custom):
#     assert 1 == solr_custom.search('title:apples').hits

# def test_stopwords(solr_custom):
#    assert 0 == solr_custom.search('title:and').hits

# def test_uppercase(solr_custom):
#     assert 1 == solr_custom.search('title:Bananas').hits

# def test_exact_match(solr):
#     assert 1 == solr_custom.search('title:Bananas').hits

# def test_search_ignores_lowercase(solr):
#     assert 1 == solr_custom.search('title:colorless green ideas sleep furiously').hits

# def test_search_ignores_uppercase(solr):
#     index = 'colorless green ideas sleep furiously'
#     query = 'Colorless Green Ideas Sleep Furiously'


# def test_search_ignores_punctuation(solr):
#     index = 'Colorless, Green; Ideas. Sleep? Furiously!'
#     query = 'Colorless Green Ideas Sleep Furiously'

# def test_search_ignores_whitespace(solr):
#     index = '  Colorless Green Ideas Sleep Furiously         '
#     query = 'Colorless Green Ideas Sleep Furiously'


# def test_search_ignores_inner_whitespace(solr):
#     index = 'Colorless    Green Ideas Sleep Furiously'
#     query = 'Colorless Green Ideas Sleep Furiously'


# def test_search_replaces_non_ascii_characters(solr):
#     index = u'Cölorless Grêen Idéaß Slèep Furiously'
#     query = u'Colorless Green Ideass Sleep Furiously'
#     assert 1 == solr_custom.search(u'title:Cölorless Grêen Idéaß Slèep Furiously').hits


# def test_search_ignores_special_characters(solr):
#     assert 2 == solr_custom.search('title:Colorless Green Ideas Sleep Furiously').hits

# def test_search_finds_prefix(solr):


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
