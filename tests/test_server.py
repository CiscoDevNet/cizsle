"""Cizsle server tests."""


import pytest
import cizsle.server


pytestmark = [pytest.mark.server]


class TestServer(object):
    """Cizsle server tests."""

    def test_main(self):
        """Call the server main() function; no exception should be raised."""
        cizsle.server.main()
