import click
from browser.pachong import main

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


@click.command(help='example : violin startCello --input=pTac --input=pBAD --output=sigmaT7')
@click.option('--username', prompt='Your CELLO username please')
@click.option('--password', prompt= 'Your CELLO password please', hide_input=True,
              confirmation_prompt=True)
@click.option('--n', prompt='Name your design please',  default = 'A')
@click.option('--ucf_path', prompt='Your UCF path please', default = '')
@click.option('--showwiring', prompt='Type show_wiring to show wiring')
@click.option('--input',
              type=click.Choice(['pLuxStar', 'pTet', 'pTac', 'pBAD'], case_sensitive=False), multiple=True)
@click.option('--output',
              type=click.Choice(['BFP', 'RFP', 'sigmaK1FR', 'sigmaT3',  'sigmaT7', 'sigmaCGG'], case_sensitive=False), multiple=True)
def cli(username, password, n, ucf_path, showwiring, input, output):
    click.echo('Hello %s!' % username)
    click.echo('Hello %s!' % password)
    print(type(list(input)))
    click.echo(ucf_path)
    click.echo(input)
    click.echo(output)
    click.echo(n)
    print(list(input))
    print(list(output))
    main(username, password, n, list(input), list(output), ucf_path, showwiring)
    click.echo('-----LOGIN IN NOW-----')