#! /usr/bin/env python
#######################################################
#   Author:     Tsung Lin Hsia
#   email:      thsia@purdue.edu
#   ID:         ee364g21
#   Date:       01/15/2019
#######################################################

import os
import sys

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab02")

def getMaxDifference(symbol):
    filePath = os.path.join(DataPath, symbol + '.dat')
    with open(filePath, "r") as file:
        data=file.read()
    l=data.split(',')
    index= 0
    diff=0
    for i in range(5,len(l)-1,5):
        low=l[i+5].split('\n')
        if(float(l[i+4])-float(low[0])>diff):
            index=i
            diff=float(l[i + 4]) - float(low[0])
    date=l[index].split('\n')
    return(date[1])

def getGainPercent(symbol):
    filePath = os.path.join(DataPath, symbol + '.dat')
    with open(filePath, "r") as file:
        data=file.read()
    l=data.split(',')
    count=0
    for i in range(5, len(l)-1,5):
        if(float(l[i+1]))>(float(l[i+3])):
            count+=1
    total=((len(l)-1)/5)-1
    return round((count/total*100),4)

def getVolumeSum(symbol,date1,date2):
    filePath=os.path.join(DataPath, symbol+'.dat')
    with open(filePath, "r") as file:
        data=file.read()
    l=data.split(',')
    d1=date1.split('/')
    d2=date2.split('/')
    d1="".join(x for x in d1)
    d2="".join(x for x in d2)
    if int(d1)>=int(d2):
        return None
    v1=0#index of date1
    v2=0
    for i in range(5, len(l)-1,5):
        templist=l[i].split('\n')
        if i==5:
            temp=templist[2].split('/')
        else:
            temp=templist[1].split('/')
        temp="".join(x for x in temp)
        if temp == d1:
            v1=i+2
        elif temp == d2:
            v2=i+2
    total=0
    for j in range(v2,v1+5,5):
        total+=float(l[j])


    return int(total)

def getBestGain(date):
    dir=os.listdir(DataPath)
    bestgain=0
    for file in dir:
        if('.dat' in file):
            filePath=os.path.join(DataPath, file)
            with open(filePath, "r") as currentfile:
                data=currentfile.read()
            list=data.split(',')
            for i in range(5, len(list) - 1, 5):
                l=list[i].split('\n')
                if i==5:
                    temp=l[2]
                else:
                    temp=l[1]#date
                gain=0.0
                if(temp==date):
                    gain = ((float(list[i + 1]) - float(list[i + 3])) / float(list[i + 3])) * 100
                if abs(gain) > bestgain:
                    bestgain=abs(gain)
    return round(bestgain,4)

def getAveragePrice(symbol,year):
    filePath=os.path.join(DataPath, symbol+'.dat')
    with open(filePath, "r") as file:
        data=file.read()
    l=data.split(',')
    days=0.0
    total=0.0
    for i in range(5, len(l) - 1, 5):
        avg=0.0
        if(str(year)+'/' in l[i]):
            days+=1
            avg=((float(l[i + 1]) + float(l[i + 3])))/2.0
            total+=avg
    ans=total/days
    return round(ans,4)

def getCountOver(symbol, price):
    filePath=os.path.join(DataPath, symbol+'.dat')
    with open(filePath, "r") as file:
        data=file.read()
    l=data.split(',')
    days=0
    for i in range(10, len(l) -1, 5):
        low = l[i].split('\n')
        if(float(l[i-4])>=price and float(l[i-2])>=price and float(l[i-1])>=price and float(low[0]) >= price):
            days+=1
    if(float(l[i+1])>=price and float(l[i+3]))>=price and float(l[i+4])>=price and float(l[i+5])>=price:
        days+=1

    return days



if __name__ == "__main__":
    print('Task1:')
    print(getMaxDifference('FB'))
    print('Task2:')
    print(getGainPercent('FB'))
    print('Task3:')
    print(getVolumeSum('FB','2018/12/24','2019/01/11'))
    print('Task4:')
    print(getBestGain('2019/01/11'))
    print('Task5:')
    print(getAveragePrice('FB', 2019))
    print('Task6:')
    print(getCountOver('FB', 130))
    print('==================')
    print('Task1:')
    print(getMaxDifference('AAPL'))
    print('Task2:')
    print(getGainPercent('AAPL'))
    print('Task3:')
    print(getVolumeSum('AAPL','2017/04/12','2019/01/11'))
    print('Task4:')
    print(getBestGain('2014/02/10'))
    print('Task5:')
    print(getAveragePrice('AAPL', 2019))
    print('Task6:')
    print(getCountOver('AAPL', 150.0))
