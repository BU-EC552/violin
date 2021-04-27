import ttg
import pathlib

def create_empty_truth_table():
    # create truth table with input only, fill in output by yourself
    path = str(pathlib.Path(__file__).parent.absolute()) +  '\truthTable.csv'
    TruthTableDefine = ttg.Truths(['in1', 'in2', 'in3'], ints=True)


    print(TruthTableDefine)
    print(TruthTableDefine.as_pandas().to_csv(r'truthTable.csv', index = False))