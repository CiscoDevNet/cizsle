"""Cizsle app configuration settings and defaults."""


import os

import cizsle.utils


# Common client/server app configuration settings
debug = bool(os.environ.get("DEBUG", False))
log_level = os.environ.get("LOG_LEVEL", "INFO")
assert log_level in cizsle.utils.log_levels


# Server Configuration
CIZSLE_SERVER_BIND_IP = os.environ.get(
    "CIZSLE_WEB_SERVICE_BIND_IP", "0.0.0.0"
)


# Web Service Configuration
CIZSLE_SERVER_HTTP_PORT = int(os.environ.get(
    "CIZSLE_WEB_SERVICE_PORT", 8000
))
CIZSLE_WEB_SERVICE_WORKERS = int(os.environ.get(
    "CIZSLE_WEB_SERVICE_WORKERS", 4
))
CIZSLE_WEB_SERVICE_AUTO_RELOAD = bool(os.environ.get(
    "CIZSLE_WEB_SERVICE_AUTO_RELOAD", False
))
