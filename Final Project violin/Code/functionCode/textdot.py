def text(text_to_print,num_of_dots,num_of_loops):
    from time import sleep
    import keyboard
    import sys
    shell = sys.stdout.shell
    shell.write(text_to_print,'stdout')
    dotes = int(num_of_dots) * '.'
    for last in range(0,num_of_loops):
        for dot in dotes:
            keyboard.write('.')
            sleep(0.1)
        for dot in dotes:
            keyboard.write('\x08')
            sleep(0.1)

# import os
# print (os.getcwd())
# path = Path(os.getcwd())
# path = Path(str(path.parent.absolute()) + '/functions/verilog.txt')
# f = open(path,"r")

def progbar(curr, total, full_progbar):
    frac = curr/total
    filled_progbar = round(frac*full_progbar)
    print('\r', '#'*filled_progbar + '-'*(full_progbar -filled_progbar), '[{:>7.2%}]\n'.format(frac), end='')