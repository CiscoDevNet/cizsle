"""Cizsle app utility classes and functions."""


import logging
import sys
from datetime import datetime, timedelta, tzinfo


# Datetime Helpers
class ZuluTimeZone(tzinfo):
    """Zulu (UTC) Time Zone."""

    def tzname(self, dt: datetime) -> str:
        """Time Zone Name."""
        return "Z"

    def utcoffset(self, dt: datetime) -> timedelta:
        """UTC Offset."""
        return timedelta(0)

    def dst(self, dt: datetime) -> timedelta:
        """Daylight Savings Time Offset."""
        return timedelta(0)

    def __repr__(self):
        """Object's string representation."""
        return "<ZuluTimeZone()>"


# Logging Helpers
class PrecisionTimestampLogFormatter(logging.Formatter):
    """Format logging message timestamps using microsecond precision.

    Uses UTC time for all timestamps and defaults to ISO 8601 formatting.
    """
    time_zone = ZuluTimeZone()
    converter = datetime.utcfromtimestamp

    def formatTime(self, record, datefmt=None):
        dt = self.converter(record.created).replace(tzinfo=self.time_zone)

        if datefmt:
            return dt.strftime(datefmt)
        else:
            return dt.isoformat()


log_levels = {
    "DEBUG": 10,
    "INFO": 20,
    "WARNING": 30,
    "ERROR": 40,
    "CRITICAL": 50,
}


logging_format = "%(asctime)s %(levelname)-8s %(name)s  :  %(message)s"


def init_client_logging(log_level: str):
    """Initialize application client logging.

    This function creates a log handler that outputs all messages of
    severity >= log_level to stderr.
    """
    assert log_level in log_levels

    root_logger = logging.getLogger()
    handler = logging.StreamHandler(stream=sys.stderr)
    formatter = PrecisionTimestampLogFormatter(logging_format)

    handler.setLevel(log_level)
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)


def init_server_logging(log_level: str):
    """Initialize application server logging.

    This function creates a log handler that outputs all messages of
    severity >= log_level stdout (https://12factor.net/logs).
    """
    assert log_level in log_levels.keys()

    root_logger = logging.getLogger()
    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = PrecisionTimestampLogFormatter(logging_format)

    handler.setFormatter(formatter)

    root_logger.setLevel(log_level)
    root_logger.addHandler(handler)
