import click

# from eve.service import svc_weather
# from eve.utilities import utils as f
# from eve.config import WX_LOCATION


# class Context:
#     def __init__(self, userName, passWord):
#         self.userName = userName
#         self.passWord = passWord


# @click.group()
# @click.option("username", type=str, help="Please Provide Your cello username and password.")
# @click.pass_context
# @click.command()
# @click.option('--password', prompt=True, hide_input=True,
#               confirmation_prompt=True)
# def cli(ctx, userName, passWord):
#     """User Login information"""
#     ctx.obj = Context()
#     ctx.obj.passWord = userName
#     ctx.obj.passWord=passWord


@click.command()
@click.option('--username', prompt='Your CELLO username please')
@click.option('--password', prompt= 'Your CELLO password please', hide_input=True,
              confirmation_prompt=True)
@click.option('--input',
              type=click.Choice(['pLuxStar', 'pTet', 'pTac', 'pBAD'], case_sensitive=False), multiple=True)
@click.option('--output',
              type=click.Choice(['BFP', 'RFP', 'sigmaK1FR', 'sigmaT3',  'sigmaT7', 'sigmaCGG'], case_sensitive=False), multiple=True)
def cli(username, password, input, output):
    click.echo('Hello %s!' % username)
    click.echo('Hello %s!' % password)
    print(type(list(input)))
    click.echo(input)
    click.echo(output)

    click.echo('-----LOGIN IN NOW-----')