from csv import reader
from csv import DictReader
from functions import textdot
from functions import readFileFunctions
# read truth table and save them in Verilog format

def compile(moduleName):
    print('---Start Working on conversion ---')
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
        line = 'module ' + moduleName + '(output '
        input_output_list = []
        titleList = []
        # get module output start position
        for input_outbut in column_names:

            if not(('in' in input_outbut) and (len(input_outbut) == 3)):
                outputStartAt = index

                break
                # print(input_outbut)

            index += 1

        # initialize
        for input_outbut in column_names:
            titleList.append(input_outbut)
            input_output_list.append([])
        print('title looks like this: ' + str(titleList))


        # Case no output defined
        if outputStartAt==0:
            print('Error ---- NO OUTPUT FOUND ---')
        else:
            print('Found ' + str(outputStartAt) + 'inputs')
            print('Found ' + str(len(titleList) - outputStartAt) + 'output')


        # save it to local list
        for col in csv_dict_reader:
            for i in range(len(titleList)):
                # print(titleList[i])
                # print(col[titleList[i]])
                input_output_list[i].append(col[titleList[i]])

           # input_outbut_list = row
        #
        # print(input_output_list)
        # initialize 1st line
        # out
        for i in range(outputStartAt ,len(titleList)):
            line += ((titleList[i])+', ')
        line += 'input '
        # in
        for i in range(outputStartAt):
            line += ((titleList[i])+', ')
        line += '); \n  always@(*)\n       begin\n           case({'
        for i in range(outputStartAt):
            if (i == outputStartAt-1): line+= ((titleList[i]))
            else: line+= ((titleList[i])+', ')
        line += '})\n'


        for k in range(len(input_output_list[0])):
            # print progress
            textdot.progbar(k, len(input_output_list[0]), 20)
            line += '               ' + str(outputStartAt) + '\'b'
            # in
            for i in range(outputStartAt):
                line += (input_output_list[i][k])
            line += ': {'
            # out
            for o in range(outputStartAt, len(titleList)):
                line += titleList[o]
            line += '} = ' + str(len(titleList) - outputStartAt) + '\'b'
            for o in range(outputStartAt, len(titleList)):
                line += input_output_list[o][k]
            line += ';\n'

        line += '           endcase\n       end\nendmodule'



        # save to local txt file


        print(line)
        print('----SAVING----')
        readFileFunctions.write_file(line, )
        textdot.progbar(1, 1, 20)
        print('----COMPLETE----')

        # for input_outbut in column_names:
        #
        #     if not(('in' in input_outbut) and (len(input_outbut) == 3)):
        #         outputStartAt = index;
        #         break
        #         # print(input_outbut)
        #     # else:
        #         # print(index)
        #
        #         # print(index)
        #         # print(input_outbut)
        #     index += 1
        # if (outputStartAt == 0):
        #     print('ERROR ----- NO output found -----')
        # print(Line)
        #
        # print('out put index is ' + str(outputStartAt))
        # for row in csv_reader:
        #     # row variable is a list that represents a row in csv
        #     index = 0
        #     while (index < outputStartAt):
        #         print(row[index])
        #         index += 1
