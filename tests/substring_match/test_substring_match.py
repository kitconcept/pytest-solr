def test_solr_process(solr_proc):
    assert solr_proc.running() is True

def test_solr_core(solr_core):
    assert solr_core

def test_solr(solr):
    assert 0 == solr.search('bananas').hits
