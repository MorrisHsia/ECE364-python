#! /usr/bin/env python
#######################################################
#   Author:     Tsung Lin Hsia
#   email:      thsia@purdue.edu
#   ID:         ee364g21
#   Date:       01/09/2019
#######################################################

import os
import sys

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab01")

def find(pattern):
    ans=[]
    filePath=os.path.join(DataPath,'sequence.txt')
    with open(filePath, "r") as file:
        seq=file.read()
    for i in range(len(seq)-len(pattern)):
        nrst=0
        for j in range(len(pattern)):
            if nrst==0 and pattern[j]=='X':
                nrst=0
            elif nrst==0 and (seq[j+i]==pattern[j]):
                nrst=0
            else:
                nrst=1
        if nrst == 0:
            ans.append(seq[i:i+len(pattern)])
    return ans

def getStreakProduct(sequence, maxSize, product):
    result = []
    for i in range(0,len(sequence)):
        count = 0
        tempi = i
        ans = 1
        while ans != product and tempi < len(sequence):
            val = int(sequence[tempi])
            ans *= val
            tempi += 1
            count += 1
        if count>=2 and count<=maxSize and ans == product:
            result.append(sequence[i:tempi])
    return result

def writePyramids(filePath, baseSize, count, char):

    with open(filePath, 'w') as file:
        row = int((baseSize + 1) / 2)
        whitespace = int(baseSize / 2)
        charcount = 0 #number of char has been inserted
        for i in range(row):#height of pyramids
            for j in range(count):
                for k in range(baseSize):#baseSize*count=width
                    if k < whitespace:
                        file.write(' ')
                    elif k > whitespace+charcount:#between whitespaces and whitespaces will have some char
                        file.write(' ')
                    else:
                        file.write(char)
                if j < count-1 :#last column doesn't have whitespaces
                    file.write(' ')
            charcount+=2
            whitespace-= 1
            file.write('\n')
                
def getStreaks(sequence, letters):
    list = []
    temp='temp'
    count=0
    for i in range(0,len(sequence)):
        if sequence[i] == temp:
            count+=1
        elif sequence[i] != temp:
            if count:
                list.append(sequence[i-count:i])
                count = 0
            for j in range(0, len(letters)):
                if sequence[i] == letters[j]:
                    count = 1
                    temp = sequence[i]
                    j+=1
    if count:
        list.append(sequence[i+1-count:i+1])
    #else:
     #   return []
    return list
            
                
def findNames(nameList, part, name):
    result=[]
    for i in range(len(nameList)):
        namesplit = nameList[i].split(" ")
        if part == "F":
            if namesplit[0]==name.title():
                result.append(nameList[i])
        elif part == "L":
            if namesplit[1]==name.title():
                result.append(nameList[i])
        elif part == "FL":
            if namesplit[0]==name.title() or namesplit[1]==name.title():
                result.append(nameList[i])
    return result

def convertToBoolean(num, size):
    ans=[]
    if type(num)!=int or type(size)!=int:
        return []
    bnum=(bin(num)[2:])
    more=0
    if len(bnum) < size:
        bnum=bnum.zfill(size)
        more=size-len(bnum)
    for i in range(len(bnum)+more):
        if bnum[i]=='1':
            ans.append(True)
        elif bnum[i]=='0':
            ans.append(False)
    return ans

    
def convertToInteger(boolList):
    if type(boolList) != type([]):
        return None
    if len(boolList)==0:
        return None
    else:
        pos=0
        ans=0
        for i in range(len(boolList)-1, -1, -1):
            val=2**i*boolList[pos]
            pos+=1
            ans+=val
        return ans


#if __name__ == "__main__":
#    print(find("X8XX8X"))

#    print(getStreakProduct("54789654321687984",7,288))
#    filePath = os.path.join(DataPath, 'pyramid.txt')
#    writePyramids("pyramid.txt", 13, 6, 'X')

#    print(getStreaks("AAASSSSSAPPPSSPPBBCCCSSS","PAZ"))

#    print(findNames(["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"], "FL", "JOHNSON"))

#    print(convertToBoolean(9, 6))

#    print(convertToInteger([False, False, True, True, False, True]))
