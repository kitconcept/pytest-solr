from pytest_solr.factories import solr_proc
from pytest_solr.factories import solr_core
from pytest_solr.factories import solr


def test_solr_process(solr_proc):
    assert solr_proc.running() is True


def test_solr_core(solr_core):
    assert solr_core


def test_solr(solr):
    assert 0 == solr.search('bananas').hits

solr_core_custom = solr_core('solr_proc', 'substring_match')
solr_custom = solr('solr_core_custom')

def test_solr_core_custom(solr_core_custom):
    assert solr_core_custom

# def test_solr_custom(solr_custom):
#     assert 0 == solr_custom.search('bananas').hits