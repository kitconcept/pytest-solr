import os
import pysolr
import pytest
import signal
import subprocess


def solr_process(
    executable=None,
    host="localhost",
    port=18983,
    core="solr",
    version="7.7.3",
    timeout=60,
):
    @pytest.fixture(scope="session")
    def solr_process_fixture(request):
        solr = {
            "host": host,
            "port": port,
        }

        if not os.environ.get("SOLR_VERSION"):
            solr["version"] = version
        else:
            solr["version"] = os.environ["SOLR_VERSION"]

        if not executable:
            local_executable = "downloads/solr-{}/bin/solr".format(solr["version"])

        solr["directory"] = "downloads/solr-{}".format(solr["version"])
        solr["bin"] = "{}/bin/solr".format(solr["directory"])

        devnull = open("/dev/null", "w")
        solr["process"] = subprocess.Popen(
            "{} -f -p {}".format(executable or local_executable, port),
            stdout=devnull,
            stderr=devnull,
            shell=True,
            preexec_fn=os.setsid,
        )

        yield solr

        # tear down
        os.killpg(solr["process"].pid, signal.SIGTERM)

    return solr_process_fixture


def solr_core(solr_process_fixture_name, solr_core_name="default"):
    @pytest.fixture(scope="module")
    def solr_core_fixture(request):
        process = request.getfixturevalue(solr_process_fixture_name)
        solr_executable = process.get("bin")
        solr_core_directory = "tests/{}".format(solr_core_name)
        solr_port = str(process.get("port"))

        def create_solr_colr():
            try:
                subprocess.check_output(
                    [
                        solr_executable,
                        "create_core",
                        "-p",
                        solr_port,
                        "-c",
                        solr_core_name,
                        "-d",
                        solr_core_directory,
                    ],
                )
            except subprocess.CalledProcessError as e:
                print(
                    "Creating Solr Core failed. "
                    + 'Command "{}" failed with the following error: {}'.format(
                        " ".join(e.cmd), e.output
                    )
                )

        def drop_solr_core():
            subprocess.check_output(
                [solr_executable, "delete", "-p", solr_port, "-c", solr_core_name,],
            )

        try:
            create_solr_colr()
        except subprocess.CalledProcessError:
            drop_solr_core()
            create_solr_colr()

        yield process

        drop_solr_core()

    return solr_core_fixture


def solr(solr_core_fixture_name):
    @pytest.fixture(scope="function")
    def solr_fixture(request):
        process = request.getfixturevalue(solr_core_fixture_name)

        client = pysolr.Solr(
            "http://{0!s}:{1!s}/solr/{2!s}".format(
                process.get("host"), process.get("port"), solr_core_fixture_name
            ),
            always_commit=True,
        )

        yield client

        client.delete(q="*:*")

    return solr_fixture
