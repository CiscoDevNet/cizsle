"""Cizsle server command line interface (CLI)."""


import logging
import sys

import click
from crayons import blue

import cizsle
import cizsle.config
import cizsle.server
from cizsle.utils import init_server_logging, log_levels


@click.group("cizsle-server")
@click.option(
    "--log-level",
    type=click.Choice(log_levels.keys()),
    default=cizsle.config.log_level,
    help="Output logging messages >= this log-level to the console.",
    show_default=True,
)
def cli(log_level: str):
    """Cizsle server command line interface."""
    click.echo(blue(f"Cisco ZTP Server LE v{cizsle.__version__}"))

    cizsle.config.log_level = log_level
    init_server_logging(log_level)


@cli.command("run")
@click.option(
    "-i", "--ip-address",
    type=click.STRING,
    default=cizsle.config.CIZSLE_SERVER_BIND_IP,
    help="Bind the web service to this IP address.",
    show_default=True,
)
@click.option(
    "-p", "--port",
    type=click.INT,
    default=cizsle.config.CIZSLE_SERVER_HTTP_PORT,
    help="Bind the web service to this TCP port.",
    show_default=True,
)
@click.option(
    "-w",
    "--workers",
    type=click.INT,
    default=cizsle.config.CIZSLE_WEB_SERVICE_WORKERS,
    help="Quantity of web service workers to create.",
    show_default=True,
)
@click.option(
    "-d", "--debug",
    is_flag=True,
    type=click.BOOL,
    default=cizsle.config.debug,
    help="Enable application debugging.",
)
@click.option(
    "-r",
    "--reload",
    is_flag=True,
    type=click.BOOL,
    default=cizsle.config.CIZSLE_WEB_SERVICE_AUTO_RELOAD,
    help="Auto-reload the web service on code changes (used for development).",
)
def run(ip_address: str, port: int, workers: int, debug: bool, reload: bool):
    cizsle.config.debug = debug
    if cizsle.config.debug:
        cizsle.config.log_level = "DEBUG"

    click.echo(blue(f"\n==> Running cizsle server on {ip_address}"))
    try:
        cizsle.server.run(
            bind_ip=ip_address,
            port=port,
            debug=cizsle.config.debug,
            log_level=cizsle.config.log_level,
            workers=workers,
            reload=reload,
        )
    except KeyboardInterrupt:
        logging.shutdown()


if __name__ == '__main__':
    cli(sys.argv[1:])
