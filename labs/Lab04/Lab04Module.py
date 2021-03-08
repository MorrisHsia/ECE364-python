#! /usr/bin/env python3
#######################################################
#   Author:     Tsung Lin Hsia
#   email:      thsia@purdue.edu
#   ID:         ee364g21
#   Date:       02/06/2019
#######################################################

import os
import sys


# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab04")

def loadphones():
    filePath = os.path.join(DataPath, 'phones.dat')
    name=[]
    phone=[]
    with open(filePath,'r') as file:
        file.__next__()
        for content in file:
            content=(content.split(','))
            name.append(content[0].strip())
            phone.append(content[1].strip())
    return name,phone

def loadproviders(filename):
    filePathproviders = os.path.join(DataPath, 'providers')
    filePath = os.path.join(filePathproviders, filename)
    board = []
    price = []
    with open(filePath, 'r') as file:
        file.__next__()
        file.__next__()
        file.__next__()
        for content in file:
            content = (content.split(','))
            board.append(content[0].strip())
            price.append(content[1].strip())
    return board,price

def providersdic(filename):
    filePathproviders = os.path.join(DataPath, 'providers')
    filePath = os.path.join(filePathproviders, filename)
    with open(filePath,'r') as file:
        providers=file.readlines()[3:]
    pdic = {line.split(',')[0].strip():float(line.split(',')[1].strip().strip('$')) for line in providers}
    return pdic

def inversedic(dic):
    inv_dic={value: key for key, value in dic.items()}
    return inv_dic

def getDifference(provider1,provider2):
    provider1=provider1+'.dat'
    provider2=provider2+'.dat'
    print(provider1,provider2)
    plist1=loadproviders(provider1)
    plist2=loadproviders(provider2)
    list=[]
    for board in plist1[0]:
        #print(board)
        if board not in plist2[0]:
            list.append(board)
    dic={x for x in list}
    return dic

def getPriceOf(sbc,provider):
    provider=provider+'.dat'
    filePathreports = os.path.join(DataPath, 'providers')
    dir = os.listdir(filePathreports)
    pdic=providersdic(provider)
    if provider not in dir or sbc not in pdic:
        raise ValueError('Input does n0t exist')
    return(pdic[sbc])

def checkAllPrices(sbcSet):
    filePathreports = os.path.join(DataPath, 'providers')
    dir = os.listdir(filePathreports)
    outputdic={x:9999.99 for x in sbcSet}
    outputdic1={x:9999.99 for x in sbcSet}
    for file in dir:
        pdic=providersdic(file)
        for sbc in sbcSet:
            if sbc in pdic:
                n=(outputdic1[sbc])
                if pdic[sbc]<n:
                    outputdic.update({sbc: (pdic[sbc], file.strip('.dat'))})
                    outputdic1.update({sbc:pdic[sbc]})
                #else:
                 #   outputdic.update({sbc: (pdic[sbc], file.strip('.dat'))})
    return outputdic





if __name__ == "__main__":
    print(getDifference('provider2','provider4'))
    #print(getPriceOf('Rasp. Pi-4702MQ','provider2'))
    #print(checkAllPrices(['Rasp. Pi-4810MQ','Rasp. Pi-5850EQ','Rasp. Pi-4960HQ','Rasp. Pi-5850EQ']))
    #print(len(providersdic('provider1.dat')))
