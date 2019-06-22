"""Cizsle client CLI tests."""


import pytest
import cizsle.client.cli


pytestmark = [pytest.mark.client]


class TestClientCLI(object):
    """Cizsle client CLI tests."""

    def test_cizsle_client_cli_root(self):
        """Test calling the cizsle CLI command without args.

        SUCCESS: Should display CLI help message and raise SystemExit. No other
        exceptions should be raised.
        """
        with pytest.raises(SystemExit):
            cizsle.client.cli.cli()

    def test_cizsle_client_cli_root_help(self):
        """Test calling the cizsle CLI command the `--help` argument.

        SUCCESS: Should display CLI help message and raise SystemExit. No other
        exceptions should be raised.
        """
        with pytest.raises(SystemExit):
            cizsle.client.cli.cli(["--help"])
