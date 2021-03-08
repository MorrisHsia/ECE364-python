#! /usr/bin/env python3
#######################################################
#   Author:     Tsung Lin Hsia
#   email:      thsia@purdue.edu
#   ID:         ee364g21
#   Date:       01/23/2019
#######################################################

import os
import sys

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab02")

def getCodeFor(stateName: str)->list:
    filePath = os.path.join(DataPath, 'zip.dat')
    with open(filePath, "r") as file:
        ans = []
        final=[]
        for content in file:
            l = content.split()
            if l[0] == stateName and len(l)!=4:
                ans.append(l[2])
            elif l[0] == 'New' and stateName == 'New York':
                ans.append(l[3])
    final=sorted(ans)
    return final

def getMinLatitude(stateName:str)->int:
    filePath = os.path.join(DataPath, 'coordinates.dat')
    zips = getCodeFor(stateName)
    with open(filePath, "r") as file:
        min=999
        for line in file:
            l=line.split()
            if l[0] != 'Latitude' and l[0] != '------------------------------------------':
                for i in range(0,len(zips)):
                    if l[2]==zips[i] and float(l[0]) < float(min):
                        min=l[0]
    return min

def getMaxLongitutde(stateName:str)->int:
    filePath = os.path.join(DataPath, 'coordinates.dat')
    zips = getCodeFor(stateName)
    with open(filePath, "r") as file:
        max=-999
        for line in file:
            content=line.split()
            if content[0] != 'Latitude' and content[0] != '------------------------------------------':
                for i in range(0,len(zips)):
                    if content[2]==zips[i] and float(content[1]) > float(max):
                        max=content[1]
    return max

def getSubMatrixSum(startRowIndex, endRowIndex, startColumnIndex, endColumnIndex):
    filePath = os.path.join(DataPath, 'matrix.dat')
    with open(filePath, "r") as file:
        data=file.read()
    data=data.split()
    start=(startRowIndex-1)*100+startColumnIndex-1
    end=(endRowIndex-1)*100+endColumnIndex-1
    sum=0
    for i in range(start,end+1):
        sum+=int(data[i])
    return sum

if __name__ == "__main__":
    print(getCodeFor('New York'))
    print(getMinLatitude('Florida'))
    print(getMaxLongitutde('Florida'))
    print(getSubMatrixSum(1,1,1,2))