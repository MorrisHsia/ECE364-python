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
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab04")

def loadmaps(filename):
    filePathmaps = os.path.join(DataPath, 'maps')
    filePath=os.path.join(filePathmaps,filename)
    with open(filePath,'r') as file:
        maps = file.readlines()[2:]
    return maps

def loadreports(filename):
    filePathcircuits = os.path.join(DataPath, 'reports')
    filePath=os.path.join(filePathcircuits,filename)
    ID=''
    virus=[]
    units=[]

    with open(filePath,'r') as file:
        ID=file.readline()
        file.__next__()
        file.__next__()
        file.__next__()
        for content in file:
            content=(content.split())
            virus.append(content[1].strip())
            units.append(content[2].strip())
    return ID,virus,units

def techydic():
    techy=loadmaps('technicians.dat')
    techysdic={(line.split('|')[0].strip()): (line.split('|')[1].strip()) for line in techy}#split by '|', and then remove spaces by strip
    return techysdic

def inversedic(dic):
    inv_dic={value: key for key, value in dic.items()}
    return inv_dic

def virusdicwithunitcost():
    virus = loadmaps('viruses.dat')
    vdic = {line.split('|')[0].strip():{line.split('|')[1].strip():line.split('|')[2].strip()} for line in virus}
    return vdic

def virusdic():
    virus = loadmaps('viruses.dat')
    vdic = {line.split('|')[0].strip():line.split('|')[1].strip() for line in virus}
    return vdic

def virusprice():
    virus = loadmaps('viruses.dat')
    vdic = {line.split('|')[1].strip():float(line.split('|')[2].strip().strip('$')) for line in virus}
    return vdic

def virusnameandprice():
    virus = loadmaps('viruses.dat')
    vdic = {line.split('|')[0].strip():float(line.split('|')[2].strip().strip('$')) for line in virus}
    return vdic


def reportdic(filename):
    filePathreports = os.path.join(DataPath, 'reports')
    filePath=os.path.join(filePathreports,filename)
    with open(filePath,'r') as file:
        report=file.readlines()[4:]
    rdic = {int(line.split()[0]):{(line.split()[1]): (line.split()[2])} for line in report}
    return rdic

def getTechWork(techName):
    techdic = techydic()
    if techName not in techdic:
        raise ValueError('The Technician is not on the list!')
    ID=techdic[techName]
    filePathreports = os.path.join(DataPath, 'reports')
    dir = os.listdir(filePathreports)
    DIC=[]
    #make every report that has same , and put them together
    for file in dir:
        sameID = loadreports(file)[0].strip('User ID:').strip()
        if ID == sameID:
            #print(file)
            #print("here")
            DIC.append(reportdic(file))
    #the format of the report is in {trial:virusId,units} so in DIC there are many dictionary within dictionary [{trial:{virusid:units}}.....]
    df = defaultdict(list)
    for i in range(1,101):
        for d in DIC:
            for key,value in d[i].items():
                df[key].append(value)
    tempdic = virusdic()
    vdic=inversedic(tempdic)
    #d = {'x':1, 'y':2, 'z':3}   d1 = {'x':'a', 'y':'b', 'z':'c'}         dict((d1[key], value) for (key, value) in d.items())         Ans:{'a': 1, 'b': 2, 'c': 3}
    outputdic=dict((vdic[key],value) for key,value in df.items())
    for d in outputdic:
        outputdic[d]=sum(int(i) for i in outputdic[d])
    #print(outputdic)
    return (outputdic)

def getStrainConsumption(virusName):
    tempdic = virusdic()
    virusID = tempdic[virusName]
    tdic = techydic()
    invtdic=inversedic(tdic)
    filePathreports = os.path.join(DataPath, 'reports')
    dir = os.listdir(filePathreports)
    keydic={value: 0 for key,value in tdic.items()}
    cnt=Counter(keydic)
    for file in dir:
        tempdic=reportdic(file)
        total=0
        temp=0
        ID = loadreports(file)[0].strip('User ID:').strip()
        for i in range(1,101):
            if virusID in tempdic[i]:
                total+=int(tempdic[i][virusID])
            smalldic = Counter({ID:total})
        cnt=(cnt+smalldic)
    outputdic={}
    for k in cnt.keys():
        outputdic.update({invtdic[k]:cnt[k]})

    return (outputdic)

def getTechSpending():
    pricedic = virusprice()#virusID:price
    techdic = techydic()
    invtechdic = inversedic(techdic)
    filePathreports = os.path.join(DataPath, 'reports')
    dir = os.listdir(filePathreports)
    cnt=Counter({})
    #make every report that has same , and put them together
    for file in dir:
        report = loadreports(file)
        ID=report[0].strip('UserID: ').strip()
        virusID = report[1]
        unit = report[2]
        total=0
        for i,virusID in enumerate(virusID):
            price = pricedic[virusID]
            total+=(int(unit[i])*price)
        dic=Counter({invtechdic[ID]:total})
        cnt=cnt+dic
    output=dict(cnt)
    for k in output.keys():
        output[k]=round(output[k],2)
    return(output)

def getStrainCost():
    vdic=virusnameandprice()
    vdic=virusdic()#Virus name: Virus ID
    invdic=inversedic(vdic)
    vprice=virusprice()# Virus ID: price
    filePathreports = os.path.join(DataPath, 'reports')
    dir = os.listdir(filePathreports)
    cnt = Counter({})
    for file in dir:
        report = loadreports(file)
        virusID = report[1]
        unit = report[2]
        total = 0
        for i, virusid in enumerate(virusID):
            total=(int(unit[i])*vprice[virusid])
            dic=Counter({invdic[virusid]:total})
            cnt = cnt + dic
            #print(cnt)
    output = dict(cnt)
    for k in output.keys():
        output[k] = round(output[k], 2)
    return (output)

def getAbsentTechs():
    techdic = techydic()
    invdic = inversedic(techdic)
    filePathreports = os.path.join(DataPath, 'reports')
    dir = os.listdir(filePathreports)
    empty=set()
    for key in invdic.keys():
        count=0
        for file in dir:
            filePath = os.path.join(filePathreports, file)
            with open(filePath, 'r') as file:
                ID = file.readline()
            if key in ID:
                count=1
        if count == 0:
            empty.add(invdic[key])
    return empty


def getUnusedStrains():
    vdic = virusdic()
    inv_vidic = inversedic(vdic)
    filePathreports = os.path.join(DataPath, 'reports')
    dir = os.listdir(filePathreports)
    empty=[]
    for key in inv_vidic.keys():
        count=0
        for file in dir:
            virusID = loadreports(file)[1]
            if key in virusID:
                count=1
        if count == 0:
            empty.append(inv_vidic[key])
    return set(empty)









if __name__=="__main__":
    print((getTechWork('Alexander, Carlos')))
    print((getStrainConsumption('Henipavirus')))
    print((getTechSpending()))
    print((getStrainCost()))
    print((getAbsentTechs()))
    print((getUnusedStrains()))
