import os

def openTruthTable():
    try:
        os.startfile("truthTable.csv")
    except OSError:
        print('Error occured')

def openVerilog():
    try:
        os.startfile("verilog.txt")
    except OSError:
        print('Error occured')

