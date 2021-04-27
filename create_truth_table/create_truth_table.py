import ttg
import pathlib
import os

def create_truth_table():
    TruthTableDefine = ttg.Truths(['in1', 'in2'], ['in1 and in2', 'in1 or in2', '(in1 or (~in2)) => (~in1)'], ints=True)


    print(TruthTableDefine)
    print(TruthTableDefine.as_pandas().to_csv(r'truthTable.csv', index = False))
    print('-------it is now ready to be modify, olease go to truthTable.csv to modify')
    try:
        os.startfile("truthTable.csv")
    except OSError:
        print('Error occured')


create_truth_table()