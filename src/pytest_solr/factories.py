import os
import pysolr
import pytest
import subprocess
from mirakuru import HTTPExecutor


def solr_process(
    executable=None,
    host='localhost',
    port=18983,
    core='solr',
    timeout=60
):

    @pytest.fixture(scope='session')
    def solr_process_fixture(request):
        if not os.environ.get('SOLR_VERSION'):
            solr_version = '6.5.0'
        else:
            solr_version = os.environ['SOLR_VERSION']
        if not executable:
            local_executable = 'downloads/solr-{}/bin/solr'.format(solr_version)  # noqa
        solr_executor = HTTPExecutor(
            '{} -f -p {}'.format(executable or local_executable, port),
            'http://{host}:{port}/solr/'.format(
                host=host,
                port=port
            ),
            timeout=timeout,
        )

        solr_executor.start()

        def finalize_solr():
            solr_executor.stop()
            # shutil.rmtree(home_path)

        request.addfinalizer(finalize_solr)

        return solr_executor

    return solr_process_fixture


def solr_core(process_fixture_name, solr_core_name='substring_match'):

    @pytest.fixture
    def solr_core_fixture(request):
        process = request.getfixturevalue(process_fixture_name)
        if not process.running():
            process.start()

        solr_executable = process.command_parts[0]
        solr_core_directory = 'tests/{}'.format(solr_core_name)
        solr_port = str(process.port)

        def create_solr_colr():
            subprocess.check_output(
                [
                    solr_executable,
                    'create_core',
                    '-p',
                    solr_port,
                    '-c',
                    solr_core_name,
                    '-d',
                    solr_core_directory
                ],
            )

        def drop_solr_core():
            subprocess.check_output(
                [
                    solr_executable,
                    'delete',
                    '-p',
                    solr_port,
                    '-c',
                    solr_core_name,
                ],
            )

        try:
            create_solr_colr()
        except subprocess.CalledProcessError:
            drop_solr_core()
            create_solr_colr()

        request.addfinalizer(drop_solr_core)

        return process

    return solr_core_fixture


def solr(process_fixture_name, documents=[]):

    @pytest.fixture
    def solr_fixture(request):
        solr_core = process_fixture_name
        process = request.getfixturevalue(process_fixture_name)
        if not process.running():
            process.start()

        client = pysolr.Solr(
            'http://{0!s}:{1!s}/solr/{2!s}'.format(
                process.host,
                process.port,
                solr_core
            )
        )

        client.add(documents)

        def drop_indexes():
            client.delete(q='*:*')

        request.addfinalizer(drop_indexes)

        return client

    return solr_fixture
