"""Cizsle app server."""


import logging

import uvicorn

import cizsle.config
import cizsle.server.web


def run(
    bind_ip: str = cizsle.config.CIZSLE_SERVER_BIND_IP,
    port: int = cizsle.config.CIZSLE_SERVER_HTTP_PORT,
    debug: bool = cizsle.config.debug,
    log_level: str = cizsle.config.log_level,
    workers: int = cizsle.config.CIZSLE_WEB_SERVICE_WORKERS,
    reload: bool = cizsle.config.CIZSLE_WEB_SERVICE_AUTO_RELOAD,
):
    """Cizsle server run entry point.

    Args:
        bind_ip: Bind the app services to this to this IP address. The default,
            '0.0.0.0', binds the app to all IP interfaces on the host.
        port: The TCP port number for the web service.
        debug: Enable application debugging.
        log_level: Set the application logging level (CRITICAL, ERROR, WARNING,
            INFO, DEBUG).
        workers: The number of web service worker processes to use.
        reload: Enable web service auto-reloading (used for development).
    """
    uvicorn.run(
        cizsle.server.web.web_service,
        host=bind_ip,
        port=port,
        debug=debug,
        log_level=logging.getLevelName(log_level),
        workers=workers,
        reload=reload,
    )
