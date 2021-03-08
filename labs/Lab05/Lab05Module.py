#! /usr/bin/env python
#######################################################
#   Author:     Tsung Lin Hsia
#   email:      thsia@purdue.edu
#   ID:         ee364g21
#   Date:       02/03/2019
#######################################################

import os
from collections import Counter, defaultdict

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab05")
def load(filename):
    filePath=os.path.join(DataPath,filename)
    with open(filePath,'r') as file:
        file.__next__()
        file.__next__()
        maps = file.readlines()
    return maps

def loadpin():
    filePath=os.path.join(DataPath,'pins.dat')
    with open(filePath,'r') as file:
        file.__next__()
        date = file.readline()
        file.__next__()
        pin = file.readlines()
    return pin,date

def peopledic():
    techy=load('people.dat')
    pdic={(line.split('|')[0].strip()): (line.split('|')[1].strip()) for line in techy}#split by '|', and then remove spaces by strip
    #print(pdic)
    return pdic

def pindic():
    pin,_=loadpin()
    pdic={(line.split()[0]): (line.split()[1:]) for line in pin}#split by '|', and then remove spaces by strip
    return pdic

def inversedic(dic):
    inv_dic={value: key for key, value in dic.items()}
    return inv_dic

def inv_pin():
    pin,_=loadpin()
    inv_pdic={(line.split()[1:]) : (line.split()[0])  for line in pin}#split by '|', and then remove spaces by strip
    return inv_pdic



def getPinFor(name, date):
    pdic=peopledic()
    if name not in pdic:
        raise ValueError("Error")
    _,d=loadpin()
    pin = pindic()
    d=d.split()
    if date not in d:
        raise ValueError("Error")
    i=d.index(date)
    output=pin[(pdic[name])][i-1]
    return output


def getUserOf(pin, date):
    pdic=peopledic()
    invpdic=inversedic(pdic)
    pindict = pindic()
    p, d = loadpin()
    d=d.split()
    if date not in d:
        raise ValueError("Error")
    dateindex = d.index(date)
    dateindex-=1
    for key,v in pindict.items():
        if pin in v[dateindex]:
            output=(key)
    ans=invpdic[output]
    return ans


def getUsersOn(date):
    pdic = peopledic()
    invpdic = inversedic(pdic)
    pindict = pindic()
    p, d = loadpin()
    d = d.split()
    if date not in d:
        raise ValueError("Error")
    dateindex = d.index(date)
    dateindex -= 1
    idlist=[]
    for key,v in pindict.items():
        if v[dateindex]:
            idlist.append(key)
    return idlist



# getMostActiveUserOn(dates)
# getMostAccessedOn(dates)
#def getAbsentUsers():

def getDifference(slot1, slot2):
    filePath=os.path.join(DataPath,'slots.dat')
    with open(filePath,'r') as file:
        file.__next__()
        time=file.readline()
        file.__next__()
        slot = file.readlines()
    time=time.split()
    s1index=time.index(slot1)
    s2index=time.index(slot2)
    sum=0
    for s in slot:
        s=s.split()
        if(s[s1index] == '1' and s[s2index] == '0'):
            sum+=1
    return sum

def getCommon(slot1, slot2):
    filePath=os.path.join(DataPath,'slots.dat')
    with open(filePath,'r') as file:
        file.__next__()
        time=file.readline()
        file.__next__()
        slot = file.readlines()
    time=time.split()
    s1index=time.index(slot1)
    s2index=time.index(slot2)
    sum=0
    for s in slot:
        s=s.split()
        if(s[s1index] == '1' and s[s2index] == '1'):
            sum+=1
    return sum
def getMissing(slots):
    filePath=os.path.join(DataPath,'slots.dat')
    with open(filePath,'r') as file:
        file.__next__()
        time=file.readline()
        file.__next__()
        slot = file.readlines()
    time=time.split()
    timeindex=[]
    for s in slots:
        timeindex.append(time.index(s))
    total=0

    for s in slot:
        sum=0
        s = s.split()
        for t in timeindex:
            sum+=int(s[t])
        if sum == 0:
           total+=1
    return total




# getBestPair()

if __name__=="__main__":
    #print((getPinFor("Bailey, Catherine",'03/18')))
    #print(getUserOf('710','03/18'))
    #print(getUsersOn('04/15'))
    print(getDifference('11:30AM-01:20PM','01:30PM-03:20PM'))
    print(getCommon('01:30PM-03:20PM','03:30PM-05:20PM'))
    print(getMissing(('11:30AM-01:20PM','01:30PM-03:20PM','03:30PM-05:20PM')))