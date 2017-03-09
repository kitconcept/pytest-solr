import pysolr
import pytest
import subprocess
from mirakuru import HTTPExecutor


def solr_process(
    executable='downloads/solr-6.4.1/bin/solr',
    host='localhost',
    port=18983,
    core='solr',
    timeout=60
):

    @pytest.fixture(scope='session')
    def solr_process_fixture(request):
        solr_executor = HTTPExecutor(
            '{} -f -p {}'.format(executable, port),
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


def solr_core(process_fixture_name, solr_core_name='test'):

    @pytest.fixture
    def solr_core_fixture(request):
        process = request.getfixturevalue(process_fixture_name)
        if not process.running():
            process.start()

        solr_executable = process.command_parts[0]
        solr_core_directory = 'tests/substring_match'

        subprocess.check_output(
            [
                solr_executable,
                'create_core',
                '-p',
                '18983',
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
                    '18983',
                    '-c',
                    solr_core_name,
                ],
            )

        request.addfinalizer(drop_solr_core)

        return process

    return solr_core_fixture


def solr(process_fixture_name):

    @pytest.fixture
    def solr_fixture(request):
        solr_core = 'test'
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

        def drop_indexes():
            client.delete(q='*:*')

        request.addfinalizer(drop_indexes)

        return client

    return solr_fixture
