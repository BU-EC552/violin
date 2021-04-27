import click


@click.command()
@click.option('--module', prompt='Name your module', default='Unnamed module', show_default=True )
def cli(module):
    from functions.read_truth_table import compile
    # print(module)
    compile('a')
    click.echo('----DONE----')