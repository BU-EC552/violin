import ttg
import pathlib


path = str(pathlib.Path(__file__).parent.absolute()) +  '\truthTable.csv'
TruthTableDefine = ttg.Truths(['in1', 'in2'], ['in1 and in2', 'in1 or in2', '(in1 or (~in2)) => (~in1)'], ints=True)


print(TruthTableDefine)
print(TruthTableDefine.as_pandas().to_csv(r'truthTable.csv', index = False))