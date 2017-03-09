def test_solr_process(solr_process):
    assert solr_process.running() is True

def test_solr_core(solr_core):
    assert solr_core

def test_solr(solr):
    assert 0 == solr.search('bananas').hits
