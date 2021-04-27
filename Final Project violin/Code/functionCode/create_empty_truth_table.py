import ttg
import pathlib
import os

def create_empty_truth_table(intLength:int):
    list = []
    for i in range(intLength):
        list.append('in' + str(i))
    # create truth table with input only, fill in output by yourself
    path = str(pathlib.Path(__file__).parent.absolute()) +  '\truthTable.csv'
    TruthTableDefine = ttg.Truths(list, ints=True)
    try:
        os.startfile("truthTable.csv")
    except OSError:
        print('Error occured')

    print(TruthTableDefine)
    print(TruthTableDefine.as_pandas().to_csv(r'truthTable.csv', index = False))
