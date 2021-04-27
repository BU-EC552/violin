import click

@click.command()
@click.option('--username', prompt='Your CELLO username please')
@click.option('--password', prompt= 'Your CELLO password please', hide_input=True,
              confirmation_prompt=True)
def cli(username, password):
    click.echo('Hello %s!' % username)
    click.echo('Hello %s!' % password)
    click.echo('-----LOGIN IN NOW-----')