import click
from functions.create_empty_truth_table import create_empty_truth_table


@click.command()
@click.option('--n', prompt='Name your module', default=1, show_default=True )
def cli(n):
    create_empty_truth_table(n)
    click.echo('----DONE----')