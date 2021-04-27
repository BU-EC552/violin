from csv import reader
from csv import DictReader
# read truth table and save them in Verilog format
moduleName = 'A'

def read_truth_table():
    with open('truthTable.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        csv_dict_reader = DictReader(read_obj)
        # get column names from a csv file
        column_names = csv_dict_reader.fieldnames
        # print(column_names[1])
        # Get the detailed output start index
        # Iterate over each header check in or out in the csv using reader object
        index = 0
        outputStartAt = 0
        Line = 'module ' + moduleName + '(output '
        inputList = []
        outputList = []
        # get module
        for input_outbut in column_names:

            if not(('in' in input_outbut) and (len(input_outbut) == 3)):
                outputStartAt = index
                break
                # print(input_outbut)
            # else:
                # print(index)

                # print(index)
                # print(input_outbut)
            index += 1

        for input_outbut in column_names:

            if not(('in' in input_outbut) and (len(input_outbut) == 3)):
                outputStartAt = index;
                break
                # print(input_outbut)
            # else:
                # print(index)

                # print(index)
                # print(input_outbut)
            index += 1
        if (outputStartAt == 0):
            print('ERROR ----- NO output found -----')
        print(Line)

        print('out put index is ' + str(outputStartAt))
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            index = 0
            while (index < outputStartAt):
                print(row[index])
                index += 1

read_truth_table()