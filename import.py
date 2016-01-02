#! /bin/python3
#import csv
import re
import pdb

#pdb.set_trace()
#Define input/output file names
in_txt="BD2_MCPBA_test3.csv"
out_txt="test_out.txt"
data_txt="data.txt"

#Add a blank line at the beginning and one at the end of the file
#Replace all lines containing letters except "e" or "E" with a blank line
#Remove spaces and tabs from beginning and end of line
with open(out_txt, 'w+') as outfile:
    with open(in_txt, 'r+') as infile:
        outfile.write("\n")
        for row in infile:            
            if re.search('[A-DF-Za-df-z]',row):
                outfile.write("\n")
            else:
                outfile.write(row.strip(" \t"))
        outfile.write("\n")


#Make a list with the number of the lines not containing numbers
#Find the largest interval between lines not containing numbers
#Make a new file containing only the data series, separated by ";"
with open(data_txt, 'w+') as outfile:
    with open(out_txt, 'r+') as infile:
        lines=[]          
        for num, row in enumerate(infile, 1):
            if re.search('[0-9]',row):
                pass
            else:
                lines.append(num)
        diff=[]
        for i in range(len(lines)-1):
            diff.append(lines[i+1]-lines[i])
        
        max_value=max(diff)
        max_index=diff.index(max_value)
        line_start=lines[max_index]
        line_end=lines[max_index + 1]
        
        infile.seek(0)                      
        for num, row in enumerate(infile, 1):
            if num <= line_start or num >= line_end:
                pass
            else:
                outfile.write(row.replace(",",";").replace(" ",";").replace("\t",";").rstrip(";\n") + "\n")



