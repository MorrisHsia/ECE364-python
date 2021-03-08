#! /user/local/bin/python3.7
#######################################################
#   Author:     Tsung Lin Hsia
#   email:      thsia@purdue.edu
#   ID:         ee364g21
#   Date:       02/03/2019
#######################################################
import os
import sys
import re
from uuid import UUID
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Prelab06")
#Part1
#getUrlParts(url)
#getQueryParameters(url)
#getSpecial(sentence,letter)
#getRealMAC(sentence)#example of a MAC address is 58:1C:0A:6E:39:4D
#Part2
#getRejectedEntries()
#getEmployeeWithIDs()
#getEmployeeWithoutIDs()
#getEmployeeWithPhones()
#getEmployeeWithStates()
#getCompleteEntries()

def getUrlParts(url):
    pattern = re.match(r'http://(?P<BaseAddress>[\w\.\-]+)/(?P<Controller>[\w\.\-]+)/(?P<Action>[\w\.\-]+)\?(?P<QueryString>[\w\.\-]+)',url) # ? is appended to the quantifier to indicate nongreedy behaviour
    return pattern.group("BaseAddress","Controller","Action")

def getQueryParameters(url): #Although I got this right but I'm not sure how did my tuple created
    pattern = r"([\w\.\-\_]+)=([\w\.\_\-]+)" #tuple can be create in the format #
    search = re.findall(pattern,url) # ? is appended to the quantifier to indicate nongreedy behaviour
    return (search)

def getSpecial(sentence,letter):
    wrongpattern = r"{0}\w+{0}".format(letter)
    wrong = re.findall(wrongpattern,sentence,re.I)
    pattern=r"\b({0}\w*|{0}\w*[^{0}\W]|[^{0}\W]\w*{0}|\w*{0})\b".format(letter) #special sequences in Python regex conflict with escaped characters    ^:start    $:end
    search = re.findall(pattern,sentence,re.I)
    for i in wrong:
        for j in search:
            if i == j :
                search.remove(j)
    return (search)

def getRealMAC(sentence):
    MAC = r"([a-zA-z0-9]){2}(:|-)([a-zA-z0-9]){2}(:|-)([a-zA-z0-9]){2}(:|-)([a-zA-z0-9]){2}(:|-)([a-zA-z0-9]){2}(:|-)([a-zA-z0-9]){2}"#\w = [a-zA-z0-9_]
    search = re.search(MAC,sentence) #use findall: result [('8', ':', 'c', ':', 'A', ':', 'E', ':', '9', ':', 'D')]
    return search.group(0)

def _loaddata():
    filePath = os.path.join(DataPath, 'Employees.txt')
    FL = r'^(?P<First>[a-zA-Z]+) (?P<Last>[a-zA-Z]+)(?P<Info>.*$)'
    LF = r'^(?P<Last>[a-zA-Z]+), (?P<First>[a-zA-Z]+)(?P<Info>.*$)'
    ID = r'[a-zA-Z0-9]{8}-?[a-zA-Z0-9]{4}-?[a-zA-Z0-9]{4}-?[a-zA-Z0-9]{4}-?[a-zA-Z0-9]{12}'
    NUM1 = r',[0-9]{10};'
    NUM2 = r'\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}'
    NUM3 = r'[0-9]{3}-[0-9]{3}-[0-9]{4}'
    STATE = r'[a-zA-Z ]*$'
    with open(filePath,'r') as file:
        data = file.readlines()
    newdata = {}
    for content in data:
        #print(content)
        id = ''
        num = ''
        state = ''
        if (re.search(LF,content)):
            name = re.search(LF,content)
            nameFL = re.search(LF,content).group("First")+' '+re.search(LF,content).group("Last")
        elif re.search(FL,content):
            name = re.search(FL,content)
            nameFL = re.search(FL, content).group("First") + ' ' + re.search(FL, content).group("Last")
        if re.search(ID,content):
            id = re.search(ID,content)
            id = id.group(0)
            id = str((UUID(id)))
            #print(id)
        if re.search(NUM1,content):
            num = re.search(NUM1,content)
            num = '('+(num.group(0)[1:4])+')'+' '+(num.group(0)[4:7])+'-'+(num.group(0)[7:12])
        elif re.search(NUM2,content):
            num = re.search(NUM2, content)
            num = num.group(0)
        elif re.search(NUM3,content):
            num = re.search(NUM3, content)
            num = '('+(num.group(0)[0:3])+')'+' '+(num.group(0)[4:])
        if re.search(STATE,content):
            state = re.search(STATE,content)
            state = (state.group(0))
        newdata.update({nameFL:[id,num,state]})
    return (newdata)

def getRejectedEntries():
    data = _loaddata()
    output = []
    [output.append(key) for key,value in data.items() if value == ['','','']]
    return sorted(output)

def getEmployeesWithIDs():
    data = _loaddata()
    output = {}
    [output.update({key:value[0]}) for key,value in data.items() if value[0] != '']
    return output

def getEmployeesWithoutIDs():
    data = _loaddata()
    output = []
    [output.append(key) for key,value in data.items() if value[0] == '' and (value[1] != '' or value[2] != '')]
    return sorted(output)

def getEmployeesWithPhones():
    data = _loaddata()
    output = {}
    [output.update({key:value[1]}) for key,value in data.items() if value[1] != '']
    return output

def getEmployeesWithStates():
    data = _loaddata()
    output = {}
    [output.update({key:value[2]}) for key,value in data.items() if value[2] != '']
    return output

def getCompleteEntries():
    data = _loaddata()
    output = {}
    [output.update({key:(value[0],value[1],value[2])}) for key,value in data.items() if value[0] != '' and value[1] != '' and value[2] != '']
    return output




if __name__ == "__main__":
    print(getUrlParts("http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"))
    print(getQueryParameters('http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here'))
    print(getSpecial('The TART program runs on Tuesdays and Thursdays, but it does not start until next week.','t'))
    print(getRealMAC("This 58:1c:0A:6E:39:4D ia MAC"))
    print((getRejectedEntries()))
    print((getEmployeesWithIDs()))
    print(getEmployeesWithoutIDs())
    print(getEmployeesWithPhones())
    print(getEmployeesWithStates())
    print(getCompleteEntries())
    #print(_loaddata())
    #print(len(getRejectedEntries()))
    #print(len(getEmployeesWithIDs()))
    #print(len(getEmployeesWithoutIDs()))
    #print(len(getEmployeesWithPhones()))
    #print(len(getEmployeesWithStates()))
    #print(len(getCompleteEntries()))



