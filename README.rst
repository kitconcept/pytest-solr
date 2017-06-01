.. image:: https://kitconcept.com/logo.png
   :height: 200px
   :width: 65px
   :alt: kitconcept
   :align: center
   :target: https://www.kitconcept.com/

.. image:: https://travis-ci.org/kitconcept/pytest-solr.svg?branch=master
    :target: https://travis-ci.org/kitconcept/pytest-solr

Solr process and client fixtures for py.test.

Introduction
------------

pytest-solr is a pytest plugin for the Apache Solr search server.
It provides three pytest factories

- solr_process: For starting and stopping the Solr server
- solr_core: For loading and unloading a Solr core configuration
- solr: For connecting to a Solr server during a test


Installation
------------

Install pytest-solr with pip::

  $ pip install pytest-solr


Usage
-----

    # -*- coding: utf-8 -*-
    from pytest_solr.factories import solr_core
    from pytest_solr.factories import solr

    minimal = solr_core('solr_process', 'minimal')
    solr = solr('minimal')


    def test_exact_term_match(solr):
        solr.add([{'id': '1', 'title': 'bananas'}])
        assert 1 == solr.search('title:bananas').hits


Contribute
----------

- `Source code at Github <https://github.com/kitconcept/pytest-solr>`_
- `Issue tracker at Github <https://github.com/kitconcept/pytest-solr/issues>`_


Support
-------

If you are having issues, `please let us know <https://github.com/kitconcept/pytest-solr/issues>`_. If you require professional support feel free to contact us at `info@kitconcept.com. <mailto:info@kitconcept.com>`_
