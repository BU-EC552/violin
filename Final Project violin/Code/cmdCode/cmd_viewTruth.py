import click
from functions.openFiles import openTruthTable

@click.command()
def cli():
    openTruthTable()
    click.echo('----Open Now----')