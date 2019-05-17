"""Cizsle app configuration settings and defaults."""


import os

import cizsle.utils


# Common client/server app configuration settings
DEBUG = bool(os.environ.get("DEBUG", False))
LOG_LEVEL = os.environ.get("LOG_LEVEL", "WARNING")
assert LOG_LEVEL in cizsle.utils.log_levels


# Web Service
CIZSLE_WEB_SERVICE_BIND_IP = os.environ.get(
    "CIZSLE_WEB_SERVICE_BIND_IP", "0.0.0.0"
)
CIZSLE_WEB_SERVICE_PORT = int(os.environ.get(
    "CIZSLE_WEB_SERVICE_PORT", 8000
))
CIZSLE_WEB_SERVICE_WORKERS = int(os.environ.get(
    "CIZSLE_WEB_SERVICE_WORKERS", 4
))
CIZSLE_WEB_SERVICE_AUTO_RELOAD = bool(os.environ.get(
    "CIZSLE_WEB_SERVICE_AUTO_RELOAD", False
))
