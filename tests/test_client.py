"""Cizsle client tests."""


import pytest
import cizsle.client


pytestmark = [pytest.mark.client]


class TestClient(object):
    """Cizsle client tests."""

    def test_main(self):
        """Call the client main() function; no exception should be raised."""
        cizsle.client.main()
