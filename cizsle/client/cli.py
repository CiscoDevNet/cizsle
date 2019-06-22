"""Cizsle client command line interface (CLI)."""


import logging
import sys

import click
from crayons import blue

import cizsle
import cizsle.client
import cizsle.config
from cizsle.utils import init_client_logging, log_levels


@click.group("cizsle-client")
@click.option(
    "--log-level",
    type=click.Choice(log_levels.keys()),
    default=cizsle.config.log_level,
    help="Output logging messages >= this log-level to the console.",
    show_default=True,
)
def cli(log_level: str):
    """Cizsle client command line interface."""
    click.echo(blue(f"Cisco ZTP Server LE v{cizsle.__version__}"))

    cizsle.config.log_level = log_level
    init_client_logging(log_level)


@cli.command("main")
def main():
    try:
        cizsle.client.main()
    except KeyboardInterrupt:
        logging.shutdown()


if __name__ == '__main__':
    cli(sys.argv[1:])
