import pytest  # noqa

from pytest_solr import factories

_help_host = 'Solr host'
_help_port = 'Solr port'


def pytest_addoption(parser):
    parser.addini(
        name='solr_host',
        help=_help_host,
        default='127.0.0.1'
    )

    parser.addini(
        name='solr_port',
        help=_help_port,
        default=None,
    )

    parser.addoption(
        '--solr-host',
        action='store',
        dest='solr_host',
        help=_help_host,
    )

    parser.addoption(
        '--solr-port',
        action='store',
        dest='solr_port',
        help=_help_port
    )


solr_process = factories.solr_process()
solr_core = factories.solr_core('solr_process')
solr = factories.solr('solr_core')
