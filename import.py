#! /bin/python3
import csv	#For csv file handling
import re	#Regular expressions
import sys	#System processes
import os	#Work on files and folders depending on your OS

#import pdb	#Debugger
#pdb.set_trace()

#Input arguments
#sys.argv[1] = Input file name
#sys.argv[2] = Output file name
#sys.argv[3] = Folder name (Default = Current Working Directory)

#If the folder name is given as third argument, use it, otherwise use current directory
if len(sys.argv) > 3:
    folder=sys.argv[3]
else:
    folder=os.getcwd()

#Define input/output file names joining the folder and file names ensuring portability between different OSs
in_txt=os.path.join(folder,sys.argv[1])
tmp_txt=os.path.join(folder,"tmp.txt")
out_txt=os.path.join(folder,sys.argv[2])

#Add a blank line at the beginning and one at the end of the file
#Replace all lines containing letters except "e" or "E" with a blank line
#Remove spaces and tabs from beginning and end of line
with open(tmp_txt, 'w+') as outfile:
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
with open(out_txt, 'w+') as outfile:
    with open(tmp_txt, 'r+') as infile:
        #Find lines not containing numbers
        lines=[]          
        for num, row in enumerate(infile, 1):
            if re.search('[0-9]',row):
                pass
            else:
                lines.append(num)

        #Find the largest interval between non-numeric lines (our dataset) and find the first and last lines of the interval
        diff=[]
        for i in range(len(lines)-1):
            diff.append(lines[i+1]-lines[i])
        
        max_value=max(diff)
        max_index=diff.index(max_value)
        line_start=lines[max_index]
        line_end=lines[max_index + 1]
        
        infile.seek(0)

        #Find the delimiter in the first numeric line encountered
        sniffer = csv.Sniffer()
        for num,row in enumerate(infile,1):
            if re.search('[0-9]',row):
                dialect = sniffer.sniff(row)
                break
        delimiter=dialect.delimiter

        infile.seek(0)

        #Replace the delimiter with ";" and remove ";" if it is at the end of the line                       
        for num, row in enumerate(infile, 1):
            if num <= line_start or num >= line_end:
                pass
            else:
                outfile.write(row.replace(delimiter,";").rstrip(";\n") + "\n")

#Delete temporary files
os.remove(tmp_txt)


