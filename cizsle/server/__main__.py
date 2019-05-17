"""Cizsle server app main entry point."""


import click
import uvicorn
from crayons import blue
import logging

from cizsle.config import (
    CIZSLE_WEB_SERVICE_AUTO_RELOAD,
    CIZSLE_WEB_SERVICE_BIND_IP,
    CIZSLE_WEB_SERVICE_PORT,
    CIZSLE_WEB_SERVICE_WORKERS,
    DEBUG,
    LOG_LEVEL,
)
from cizsle.server.web import web_service


def main(
    bind_ip: str = CIZSLE_WEB_SERVICE_BIND_IP,
    port: int = CIZSLE_WEB_SERVICE_PORT,
    debug: bool = DEBUG,
    log_level: str = LOG_LEVEL,
    workers: int = CIZSLE_WEB_SERVICE_WORKERS,
    reload: bool = CIZSLE_WEB_SERVICE_AUTO_RELOAD,
):
    """Cizsle server main entry point.

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
        web_service,
        host=bind_ip,
        port=port,
        debug=debug,
        log_level=logging.getLevelName(log_level),
        workers=workers,
        reload=reload,
    )


@click.command()
@click.option(
    "-i", "--ip-address", default=CIZSLE_WEB_SERVICE_BIND_IP, show_default=True
)
@click.option(
    "-p", "--port", default=CIZSLE_WEB_SERVICE_PORT, show_default=True
)
@click.option(
    "-w",
    "--workers",
    type=int,
    default=CIZSLE_WEB_SERVICE_WORKERS,
    show_default=True,
)
@click.option(
    "--log-level",
    type=click.Choice(["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]),
    default=LOG_LEVEL,
    show_default=True,
)
@click.option("-d", "--debug", is_flag=True, default=DEBUG, show_default=True)
@click.option(
    "-r",
    "--reload",
    is_flag=True,
    default=CIZSLE_WEB_SERVICE_AUTO_RELOAD,
    show_default=True,
)
def server_cli(ip_address, port, workers, debug, log_level, reload):
    click.echo(blue(f"==> Starting cizsle server on {ip_address}:{port}"))
    try:
        main(
            bind_ip=ip_address,
            port=port,
            debug=debug,
            log_level=log_level,
            workers=workers,
            reload=reload,
        )
    except KeyboardInterrupt:
        logging.shutdown()


if __name__ == "__main__":
    main()
