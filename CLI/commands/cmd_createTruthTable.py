import click
from create_truth_table.create_truth_table import create_truth_table

# negation: 'not', '-', '~'
# logical disjunction: 'or'
# logical nor: 'nor'
# exclusive disjunction: 'xor', '!='
# logical conjunction: 'and'
# logical NAND: 'nand'
# material implication: '=>', 'implies'
# logical biconditional: '='
@click.command()
@click.option('--n', prompt='how many input do you want?', default=1, show_default=True )
@click.option('--n', prompt='negation: not, -, ~\nlogical disjunction: or\nlogical nor: nor\nexclusive disjunction: xor, !=\nlogical conjunction: and\nlogical NAND: nand\nmaterial implication: >,\nlogical biconditional: =', default=1, show_default=True )

def cli(n):
    create_truth_table(n)
    click.echo('----DONE----')