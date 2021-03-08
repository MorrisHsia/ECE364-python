#! /usr/bin/env python
#######################################################
#   Author:     Tsung Lin Hsia
#   email:      thsia@purdue.edu
#   ID:         ee364g21
#   Date:       01/27/2019
#######################################################

import os
from collections import Counter

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab03")

def loadmaps(filename):
    filePathmaps = os.path.join(DataPath, 'maps')
    filePath=os.path.join(filePathmaps,filename)
    with open(filePath,'r') as file:
        if filename == 'projects.dat' or filename == 'students.dat':
            maps=file.readlines()[2:]
        else:
            maps=file.readlines()[3:]
    return maps

def loadcircuits(filename):
    filePathcircuits = os.path.join(DataPath, 'circuits')
    filePath=os.path.join(filePathcircuits,filename)
    participants=[]
    components=[]
    with open(filePath,'r') as file:
        for content in file:
            content=content.strip()
            if len(content) == 11 and content != 'Components:':
                participants.append(content)
            elif len(content) == 7:
                components.append(content)
    return participants,components

def studentsdic(studentlist):
    studentdic={(line.split('|')[0]).strip(): (line.split('|')[1]).strip() for line in studentlist}#split by '|', and then remove spaces by strip
    return studentdic

def invstudentdic(studentdic):
    inv_studentdic={value: key for key, value in studentdic.items()}
    return inv_studentdic

def resistordic():
    list=loadmaps('resistors.dat')
    resistorsdic={(line.split()[0]): (line.split()[1].strip('$')) for line in list}
    return resistorsdic

def inductordic():
    list=loadmaps('inductors.dat')
    inductorsdic={(line.split()[0]): (line.split()[1].strip('$')) for line in list}
    return inductorsdic

def conductordic():
    list=loadmaps('capacitors.dat')
    capacitorsdic={(line.split()[0]): (line.split()[1].strip('$')) for line in list}
    return capacitorsdic

def transistordic():
    list=loadmaps('transistors.dat')
    transistorsdic={(line.split()[0]): (line.split()[1].strip('$')) for line in list}
    return transistorsdic

def projectdic(project):
    projectdictionary={}
    for line in project:
        key,value = line.split()
        projectdictionary.setdefault(key.strip(),[]).append(value.strip())#for duplicate value
    return projectdictionary

def invprojectdic(projectdictionary):
    inv_projectdic={}
    for key,value in projectdictionary.items():
        for x in value:
            inv_projectdic.setdefault(x,[]).append(key)
    return inv_projectdic

def getComponentCountByProject(projectID: str,componentSymbol: str)->int:
    project=loadmaps('projects.dat')
    projectIDs=[]
    storeCircuits=[]
    for line in project:
        projectIDs.append(line.split()[1])
        if line.split()[1] == projectID:
            storeCircuits.append(line.split()[0])
    if projectID not in projectIDs:
        raise ValueError('projectID does not exist')
    if componentSymbol=='R':
        filename='resistors.dat'
    elif componentSymbol=='I':
        filename='inductors.dat'
    elif componentSymbol=='C':
        filename='capacitors.dat'
    elif componentSymbol=='T':
        filename='transistors.dat'
    R_I_C_T=loadmaps(filename)
    ID=[]
    for line in R_I_C_T:
        ID.append(line.split()[0])
    circuit=[]
    for content in storeCircuits:
        content='circuit_'+content+'.dat'
        for index in loadcircuits(content)[1]:
            if index in ID:
                circuit.append(index)
    anslist=[]
    for i in circuit:
        if i not in anslist:
            anslist.append(i)

    return len(anslist)


def getComponentCountByStudent(studentName,componentSymbol):
    students=loadmaps('students.dat')
    studentdic=studentsdic(students)
    if studentName not in studentdic:
        raise ValueError('student Name does not exit')
    studentID=studentdic[studentName]
    if componentSymbol=='R':
        filename='resistors.dat'
    elif componentSymbol=='I':
        filename='inductors.dat'
    elif componentSymbol=='C':
        filename='capacitors.dat'
    elif componentSymbol=='T':
        filename='transistors.dat'
    R_I_C_T=loadmaps(filename)
    ID=[]
    for line in R_I_C_T:
        ID.append(line.split()[0])
    circuits=[]
    filePathcircuits = os.path.join(DataPath, 'circuits')
    dir=os.listdir(filePathcircuits)
    for file in dir:
        if studentID in loadcircuits(file)[0]:
            for index in loadcircuits(file)[1]:
                if index in ID:
                    circuits.append(index)
    anslist=[]
    for i in circuits:
        if i not in anslist:
            anslist.append(i)

    return len(anslist)

def getParticipationByStudent(studentName):
    students=loadmaps('students.dat')
    studentdic=studentsdic(students)
    if studentName not in studentdic:
        raise ValueError('student name does not exist')
    studentID=studentdic[studentName]
    filePathcircuits = os.path.join(DataPath, 'circuits')
    dir=os.listdir(filePathcircuits)
    files=[]
    for file in dir:
        if studentID in loadcircuits(file)[0]:
            files.append(file[8:15])
    project=loadmaps('projects.dat')
    projectdictionary=projectdic(project)
    print(projectdic)
    ans=[]
    for circuit in files:
        ans=list(set(ans)|set(projectdictionary[circuit]))
    return set(ans)

def getParticipationByProject(projectID):
    project=loadmaps('projects.dat')
    pdic=projectdic(project)
    value=pdic.values()
    if projectID not in [x for v in value for x in v if type(v) == list] and projectID not in value:#double for loops to check the list
        raise ValueError('project ID does not exist')
    inv_pdic=invprojectdic(pdic)
    students=loadmaps('students.dat')
    sdic=studentsdic(students)
    inv_sdic=invstudentdic(sdic)
    circuit=inv_pdic[projectID]
    filePathcircuits = os.path.join(DataPath, 'circuits')
    dir=os.listdir(filePathcircuits)
    store=[]
    for file in dir:
            for index in circuit:
                if 'circuit_'+index+'.dat' == file:
                    store+=(loadcircuits(file)[0])
    anslist=[]
    for i in store:
        if i not in anslist:
            anslist.append(i)
    return set(anslist)

def getCostOfProjects():
    project = loadmaps('projects.dat')
    projectdictionary = projectdic(project)
    inv_pdic = invprojectdic(projectdictionary)
    rdic=resistordic()
    idic=inductordic()
    cdic=conductordic()
    tdic=transistordic()
    for key, value in inv_pdic.items():
        total=0
        for i,index in enumerate(value):
            sum=0
            store = []
            store += (loadcircuits('circuit_'+index+'.dat')[1])
            for j in store:
                if j in rdic:
                    sum+=round(float(rdic[j]),2)
                elif j in idic:
                    sum+=round(float(idic[j]),2)
                elif j in cdic:
                    sum+=round(float(cdic[j]),2)
                elif j in tdic:
                    sum+=round(float(tdic[j]),2)
            value[i]=round(sum,2)
            total+=value[i]
        inv_pdic[key]=round(total,2)
    return inv_pdic

def getProjectByComponent(componentIDs):
    filePathcircuits = os.path.join(DataPath, 'circuits')
    dir=os.listdir(filePathcircuits)
    storecircuitfile=[]
    for file in dir:
        if bool(componentIDs & set(loadcircuits(file)[1])):
            storecircuitfile.append(file[8:15])#strip will work too
    project=loadmaps('projects.dat')
    pdic=projectdic(project)
    ID=[]
    for i in storecircuitfile:
        ID.extend(pdic[i])
    return (set(ID))

def getCommonByProject(projectID1,projectID2):
    project=loadmaps('projects.dat')
    pdic=projectdic(project)
    inv_pdic=invprojectdic(pdic)
    if(projectID1 not in inv_pdic.keys()) or (projectID2 not in inv_pdic.keys()):
        raise ValueError('projectID1 or 2 does not exist')
    store1 = []
    for file in inv_pdic[projectID1]:
        store1.extend(loadcircuits('circuit_' + file + '.dat')[1])
    store2 = []
    for file in inv_pdic[projectID2]:
        store2.extend(loadcircuits('circuit_' + file + '.dat')[1])
    temp1=set(sorted(store1))
    temp2=set(sorted(store2))
    ans=temp1&temp2
    return sorted(ans)

def getComponentReport(componentIDs):
    filePathcircuits = os.path.join(DataPath, 'circuits')
    dir=os.listdir(filePathcircuits)
    components=[]
    for file in dir:
        components+=(loadcircuits(file)[1])
    cnt=Counter()
    for number in components:
        cnt[number]+=1
    report={}
    for ID in componentIDs:
        report.update({ID:cnt[ID]})
    return(report)

def getCircuitByStudent(studentNames):
    students=loadmaps('students.dat')
    studentdic=studentsdic(students)
    studentID=[]
    for name in studentNames:
        studentID.append(studentdic[name])
    filePathcircuits = os.path.join(DataPath, 'circuits')
    dir=os.listdir(filePathcircuits)
    circuitID=[]
    for file in dir:
        if bool(set(studentID) & set(loadcircuits(file)[0])):
            circuitID.append(file[8:15])
    return(set(circuitID))

def getCircuitByComponent(componentIDs):
    filePathcircuits = os.path.join(DataPath, 'circuits')
    dir=os.listdir(filePathcircuits)
    circuitID=[]
    for file in dir:
        if bool(componentIDs & set(loadcircuits(file)[1])):
            circuitID.append(file[8:15])
    return(circuitID)

if __name__ == "__main__":
    #print('task1')
    print(getComponentCountByProject('082D6241-40EE-432E-A635-65EA8AA374B6','R'))
    #print('task2')
    #print(getComponentCountByStudent('Alexander, Carlos','R'))
    #print('task3')
    #print(len(getParticipationByStudent('Alexander, Carlos')))
    #print('task4')
    #print(len(getParticipationByProject('082D6241-40EE-432E-A635-65EA8AA374B6')))
    #print('task5')
    #print(len(getCostOfProjects()))
    #print('task6')
    #print(getProjectByComponent({'RNW-027','HRK-348','KSR-430'}))
    #print('task7')
    #print(len(getCommonByProject('082D6241-40EE-432E-A635-65EA8AA374B6','96CC6F98-B44B-4FEB-A06B-390432C1F6EA')))
    #print('task8')
    #print(getComponentReport({'TAZ-349','CUI-043','QLS-943'}))
    #print('task9')
    #print(len(getCircuitByStudent({'Baker, Craig','Bennett, Nancy','Coleman, Lori'})))
    #print('task10')
    #print(len(getCircuitByComponent({'TAZ-349','CUI-043','QLS-943','ORW-143'})))
    #print('task11')
    #print(len(getCommonByProject('66FA081D-D1AA-4306-8650-9C39429CCDAB','DE06228A-0544-4543-9055-A39D19DEDFA4')))
    #print((getComponentCountByProject('082D6241-40EE-432E-A635-65EA8AA374B6', 'T')))
    #print((getCostOfProjects()))
    #print((getComponentCountByStudent('Adams, Keith', 'I')))
    #print(len(getParticipationByStudent('Adams, Keith')))
    #print(len(getParticipationByProject('96CC6F98-B44B-4FEB-A06B-390432C1F6EA')))
    #print((getProjectByComponent({'BLL-583', 'GTV-294','CJF-903','JTQ-023','AIR-801'})))
    #print(len(getCommonByProject('66FA081D-D1AA-4306-8650-9C39429CCDAB','DE06228A-0544-4543-9055-A39D19DEDFA4')))
    #print((getComponentReport({'BLL-583', 'GTV-294','CJF-903','JTQ-023','AIR-801'})))
    #print((getCircuitByStudent({'Adams, Keith','Alexander, Carlos'})))
    #print(len(getCircuitByComponent({'TAZ-349'})))
    #print(len(getCircuitByComponent({'BLL-583', 'GTV-294','CJF-903','JTQ-023','AIR-801'})))

