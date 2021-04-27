import ttg
import pathlib
import os

def create_truth_table(intLength:int, logic:str):
    # in1 and in2
    # (in1 or (~in2)) and (~in0)
    list = []
    for i in range(intLength):
        list.append('in' + str(i))
    TruthTableDefine = ttg.Truths(list, [logic], ints=True)


    print(TruthTableDefine)
    print(TruthTableDefine.as_pandas().to_csv(r'truthTable.csv', index = False))
    print('-------it is now ready to be modify, olease go to truthTable.csv to modify')
    # try:
    #     os.startfile("truthTable.csv")
    # except OSError:
    #     print('Error occured')
