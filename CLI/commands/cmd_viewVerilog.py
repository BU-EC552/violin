import click
from functions.openFiles import openVerilog

@click.command()
def cli():
    openVerilog()
    click.echo('----Open Now----')