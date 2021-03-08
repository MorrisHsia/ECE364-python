#! /user/local/bin/python3.7
#######################################################
#   Author:     Tsung Lin Hsia
#   email:      thsia@purdue.edu
#   ID:         ee364g21
#   Date:       03/27/19
#######################################################
import os
import sys
import re
from Lab10.measurement import calculateDistance
DataPath = os.path.expanduser("~ee364/DataFolder/Lab10")
def getCost(sourceZip,destinationZip):
    filePath = os.path.join(DataPath, 'coordinates.dat')
    with open(filePath,'r') as file:
        data = file.readlines()
    pattern1 = r"[0-9]{2,3}.[0-9]{5}"
    pattern2= r"-[0-9]+.[0-9]+"
    t1=()
    t2=()
    for content in data:
        #print(content)
        if sourceZip in content:
            temp1=re.search(pattern1,content)
            temp2=re.search(pattern2,content)
            t1=(float(temp1.group()),float(temp2.group()))

        if destinationZip in content:
            temp1=re.search(pattern1,content)
            temp2=re.search(pattern2,content)
            t2=(float(temp1.group()),float(temp2.group()))
    cost = calculateDistance(t1,t2)
    cost = round(cost/100,2)
    return cost

'''
def loadPackages():
    filePath = os.path.join(DataPath, 'packages.dat')
    temp = []
    with open(filePath,'r') as file:
        data = file.readlines()[1:]
    pattern = r"(\"[\w\s.,]+\")"
    for i in data:
        j = re.findall(pattern,i)
        temp.append(j[0])
    comp = sorted(set(temp))
    result = []
    for c in comp:
        temp = []
        for d in data:
            j = re.findall(pattern, d)
            if c == j[0]:
                src = j[1]
                dest = j[2]
                temp.append(Package(c,src,dest))
        result.append(PackageGroup(c,temp))
    return result


class PackageGroup:
    def __init__(self,company,packages):
        self.company = company
        self.packages = sorted(packages,reverse = False)
        #for i in packages:
         #   cost += float(i.cost)
'''



class Package:
    source = ""
    destination = ""
    cost = ""
    sourceZip=''
    destinationZip=''
    def __init__(self,sourceadd,destadd):
        self.sourceZip=sourceadd
        self.destinationZip=destadd
        costtemp=getCost(sourceadd,destadd)
        self.cost=costtemp

    def __str__(self):
        return self.sourceZip+' => '+self.destinationZip+', Cost'+' = $'+str(self.cost)


    def __eq__(self, other):
        if not isinstance(other,Package):
            raise TypeError("The input in the question is not an instance of Package Class")
        return True if self.cost == other.cost else False
    def __ne__(self, other):
        if not isinstance(other,Package):
            raise TypeError("The input in the question is not an instance of Package Class")
        return True if self.cost != other.cost else False
    def __gt__(self, other):
        if not isinstance(other,Package):
            raise TypeError("The input in the question is not an instance of Package Class")
        return True if self.cost > other.cost else False
    def __lt__(self, other):
        if not isinstance(other,Package):
            raise TypeError("The input in the question is not an instance of Package Class")
        return True if self.cost < other.cost else False
    def __ge__(self, other):
        if not isinstance(other,Package):
            raise TypeError("The input in the question is not an instance of Package Class")
        return True if self.cost >= other.cost else False
    def __le__(self, other):
        if not isinstance(other,Package):
            raise TypeError("The input in the question is not an instance of Package Class")
        return True if self.cost <= other.cost else False


def getNumberPattern():
    pattern=r"[0-9\.]+"
    return pattern
def getTagPattern():
    pattern = r'http://(?P<url>[\w\.\-]+)/(?P<Controller>[\w\.\-]+)/(?P<Action>[\w\.\-]+)\?(?P<QueryString>[\w\.\-]+)' # ? is appended to the quantifier to indicate nongreedy behaviour
    return pattern


if __name__ == "__main__":
    sourceZip='99337'
    destinationZip='35115'
    print(getCost(sourceZip,destinationZip))
    print(Package(sourceZip,destinationZip))
    getNumberPattern()
    getTagPattern()