"""Cizsle server tests."""


import pytest
import cizsle.server.cli


pytestmark = [pytest.mark.server]


class TestServerCLI(object):
    """Cizsle server CLI tests."""

    def test_cizsle_server_cli_root(self):
        """Test calling the cizsle-server CLI command without args.

        SUCCESS: Should display CLI help message and raise SystemExit. No other
        exceptions should be raised.
        """
        with pytest.raises(SystemExit):
            cizsle.server.cli.cli()

    def test_cizsle_server_cli_root_help(self):
        """Test calling the cizsle-server CLI command the `--help` argument.

        SUCCESS: Should display CLI help message and raise SystemExit. No other
        exceptions should be raised.
        """
        with pytest.raises(SystemExit):
            cizsle.server.cli.cli(["--help"])

    def test_cizsle_server_cli_run_help(self):
        """Test calling the cizsle-server `run` command with the `--help` arg.

        SUCCESS: Should display CLI help message and raise SystemExit. No other
        exceptions should be raised.
        """
        with pytest.raises(SystemExit):
            cizsle.server.cli.cli(["run", "--help"])
