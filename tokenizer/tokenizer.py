import re


with open("sample.txt","r") as f:
    raw_text = f.read() ##f is the variable assigned to the file, you can also use it by saying f.open() but u als0 need to close the file afterwoards
    ##print(raw_text)
## f.open("sample.txt","r") wrong way
f = open("sample.txt","r")
rawr_text = f.read()
f.close()
#print(rawr_text)
re.split(rawr_text,'/s')


