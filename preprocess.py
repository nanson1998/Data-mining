import decimal
from tkinter import filedialog
import os,string
import ast
huhu=''
def most_frequent(List):
    return max(set(List), key= List.count)

def medium(List):
    sum = 0
    for i in List:
        if type(i)!= int :
            continue
        else:
            sum += i
    med = sum / len(List)
    return round(med,3)

def replaceValue(file_in):
    f_in = open(file_in)
    fields = []
    for line in f_in.readlines():
        fields.append([item.strip('\n') for item in line.split(',')])
    f_in.close()
    f_out = filedialog.asksaveasfilename(filetypes=[("Save File", ".csv")],
    defaultextension=".csv")
    f_out = open(f_out, 'w')
    for field in fields:
        for i,x in enumerate(field):
            if x == '?':
                if i == len(fields) - 1:
                    f_out.write(str(most_frequent(fields)+',\n'))
                else:
                    if type(fields[i + 1]) != int:
                        f_out.write(str(most_frequent(fields)+',\n'))
                    else:
                        f_out.write(str(medium(fields)+',\n'))
            else :
                f_out.write(str(x)+',')
        f_out.write('\n')
    f_out.close()

    huhu= f_out.name
    return huhu

def convertStringToArray(stri):
    arr=stri.split()
    new=[]
    for ech in arr:
        ax=ast.literal_eval(ech)
        new.append(ax)
    return new
def preprocessAsample(List):
    for i,x in enumerate(List) :
        if x == '?':
            if i == len(List)-1:
                List[i] = most_frequent(List)
            else:
                if type(List[i+1]) != int :
                    List[i] = most_frequent(List)
                else:
                    List[i] = medium(List)

