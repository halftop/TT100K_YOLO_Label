# -*- coding: utf-8 -*-   
import time     
import os  
import shutil
 
 
def readFilename(path, allfile):
    filelist = os.listdir(path)
 
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            readFilename(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile
 
 
 
if __name__ == '__main__':
    path1="/home/halftop/Downloads/TT100K/test/"
    allfile1=[]
    allfile1=readFilename(path1,allfile1)
    allname1=[]
    txtpath="/home/halftop/Downloads/TT100K/"+"test.txt"
    for name in allfile1:
        print (name)
        file_cls=name.split("/")[-1].split(".")[-1]
        if file_cls=='jpg':
            print (name.split("/")[-1])
            with open(txtpath,'a+') as fp:
                fp.write("".join(name)+"\n")