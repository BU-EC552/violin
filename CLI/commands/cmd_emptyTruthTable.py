import click
from create_truth_table.create_empty_truth_table import create_empty_truth_table


@click.command()
@click.option('--n', prompt='how many input do you want?', default=1, show_default=True )
def cli(n):
    create_empty_truth_table(n)
    click.echo('----DONE----')