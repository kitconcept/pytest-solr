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
It provides three pytest factories:

- solr_process: For starting and stopping the Solr server. This is
session scoped.
- solr_core: For loading and unloading a Solr core configuration. This is module scoped.
- solr: For connecting to a Solr server during a test. This is function scoped.

Solr Process
^^^^^^^^^^^^

The solr_process factory starts and stops a the Solr process.
An existing Solr executable is required for this.

  'executable': path to the Solr executable. Default value is 'downloads/solr-<SOLR_VERSION>/bin/solr'
  'host': hostname where Solr runs. Default value is 'localhost'.
  'port': port Solr uses. Default is value is '18983'.
  'core' Solr core that is used. Default value is 'solr'.
  'timeout': timeout to wait for Solr to start. Default value is '60' (seconds).

Solr Core
^^^^^^^^^

The solr_core factory adds and removes a Solr core configuration.
It expects two parameters, the Solr Process fixture name and the Solr core name.

  'solr_process_fixture_name': String with the name of the Solr Process. This is a required parameter.
  'solr_core_name': String with the name of the Solr core. This is a required parameter.


Installation
------------

Install pytest-solr with pip::

  $ pip install pytest-solr


Usage
-----

Create a solr core with the name 'minimal' and inject the use the solr factory into a test function to use it::

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
