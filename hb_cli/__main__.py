import click
from .utils import create_env

@click.group()
def cli():
    pass

@click.command()
def run():
    create_env()
    from .bot import run
    run()

cli.add_command(run)
