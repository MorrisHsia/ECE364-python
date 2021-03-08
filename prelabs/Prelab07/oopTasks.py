#! /user/local/bin/python3.7
#######################################################
#   Author:     Tsung Lin Hsia
#   email:      thsia@purdue.edu
#   ID:         ee364g21
#   Date:       02/21/19
#######################################################
import sys
import os
from enum import Enum

class Level(Enum):
    Freshman = 1
    Sophomore = 2
    Junior = 3
    Senior =4

class ComponentType(Enum):
    Resistor = 1
    Capacitor = 2
    Inductor = 3
    Transistor = 4

class Student:
    # Initializer
    def __init__(self,ID,firstName,lastName,level):
        self.ID = str(ID)
        self.firsName = firstName
        self.lastName = lastName
        #self.level = level
#        if level in Level.__members__:
        if isinstance(level,Level):
            self.level = level
        else:
            raise TypeError("The argument must be an instance of the 'Level' Enum.")
    #String Representation
    def __str__(self):
        return self.ID+', '+self.firsName+' '+self.lastName+', '+self.level.name
        #"{}, {} {}, {}".format(self.ID,self.firstName, self.lastName, self.level.name.title())

class Component:
    def __init__(self,ID,ctype,price):
        self.ID = str(ID)
        self.price = float(price)
#        if ctype in ComponentType.__members__:
        if isinstance(ctype,ComponentType):
            self.ctype = ctype
        else:
            raise TypeError("The argument must be an instance of the 'ComponentType' Enum.")
    def __str__(self):
        return self.ctype.name+', '+self.ID+', $'+str(round(self.price,2))
    def __hash__(self):
        return hash(self.ID)

class Circuit:
    def __init__(self,ID,components):
        self.ID = str(ID)
        costtemp = 0
        for elements in components:
            if not isinstance(elements,Component):
                raise TypeError("The argument must be an instance of the 'Component'.")
            else:
                costtemp += elements.price
        costtemp = round(costtemp,2)
        self.cost = costtemp
        self.components = set(components)
    def __str__(self):
        r=0
        c=0
        i=0
        t=0
        for element in self.components:
            if element.ctype == ComponentType.Resistor:
                r+=1
            elif element.ctype == ComponentType.Capacitor:
                c+=1
            elif element.ctype == ComponentType.Inductor:
                i+=1
            elif element.ctype == ComponentType.Transistor:
                t+=1
        r = '0' + str(r) if r < 10 else str(r)
        c = '0' + str(c) if c < 10 else str(c)
        i = '0' + str(i) if i < 10 else str(i)
        t = '0' + str(t) if t < 10 else str(t)
        return self.ID+': (R = '+r+', C = '+c+', I = '+i+' T = '+t+'), Cost = $'+str(round(self.cost,2))

    def getByType(self,ComponentType):
        output = []
        for element in self.components:
            if type(element.ctype) != type(ComponentType):
                raise ValueError("The Component is not an instance of the expected enum")
            elif element.ctype == ComponentType:
                output.append(element)
        return set(output)


    def __contains__(self,input):
        if not isinstance(input,Component):
            raise TypeError('The component in the question is not an instance of Component Class')
        if input in self.components:
            return True
        else:
            return False

    def __add__(self, other):
        if not isinstance(other,Component):
            raise TypeError("The component in the question is not an instance of Component Class")
        if other in self.components:
            return self
        else:
            self.components.add(other)
            self.cost += other.price
            return self

    def __sub__(self, other):
        if not isinstance(other,Component):
            raise TypeError("The component in the question is not an instance of Component Class")
        if other in self.components:
            self.components.remove(other)
            self.cost -= round(other.price,2)
            return self
        else:
            return self

    def __gt__(self, other):
        if not isinstance(other,Circuit):
            raise TypeError("The component in the question is not an instance of Circuit Class")
        return True if self.cost > other.cost else False

    def __eq__(self, other):
        if not isinstance(other, Circuit):
            raise TypeError("The component in the question is not an instance of Circuit Class")
        return True if self.cost == other.cost else False

    def __lt__(self, other):
        if not isinstance(other, Circuit):
            raise TypeError("The component in the question is not an instance of Circuit Class")
        return True if self.cost < other.cost else False


class Project:
    def __init__(self,ID,participants,circuits):
        for person in participants:
            if not isinstance(person,Student) and len(participants) != 0:
                raise ValueError("Invalid student in Participants")
        tempcost = 0
        for circuit in circuits:
            if not isinstance(circuit,Circuit) and len(circuits) != 0:
                raise ValueError("Invalid circuit in Circuit")
            else:
                tempcost+=circuit.cost
        self.ID = ID
        self.participants = participants
        self.circuits = circuits
        self.cost = round(float(tempcost),2)
    def __str__(self):
        p = len(self.participants)
        c = len(self.circuits)
        p = '0' + str(p) if p < 10 else str(p)
        c = '0' + str(c) if c < 10 else str(c)
        return self.ID + ': ('+c+' Circuits, '+p+' Participants), Cost = $' + str(round(self.cost, 2))

    def __contains__(self, item):
        if (not isinstance(item,Component)) and (not isinstance(item,Circuit)) and (not isinstance(item,Student)):
            raise TypeError('The item in the question is not an instance of Component, Circuit, or Student Class')
        t = 0
        if isinstance(item,Component):
            for cir in self.circuits:
                if item in cir:
                    t+=1
        elif isinstance(item,Circuit):
            if item in self.circuits:
                t+=1
        elif isinstance(item,Student):
            if item in self.participants:
                t+=1
        return True if t > 0 else False

    def __add__(self, other):
        if not isinstance(other,Circuit):
            raise TypeError("The component in the question is not an instance of Component Class")
        if other in self.circuits:
            return self
        else:
            self.circuits.append(other)
            self.cost += other.cost
            return self

    def __sub__(self, other):
        if not isinstance(other,Circuit):
            raise TypeError("The component in the question is not an instance of Component Class")
        if other in self.circuits:
            self.circuits.remove(other)
            self.cost -= other.cost
        return self

    def __getitem__(self, item):
        for circuit in self.circuits:
            if item in circuit.ID:
                return circuit
        raise KeyError('It is not a valid circuitID.')



class Capstone(Project):
    def __init__(self,ID,participants,circuits):
        Project.__init__(self,ID,participants,circuits)
        for person in participants:
            if person.level.name != 'Senior':
                raise ValueError("All participants have to be Senior")




if __name__ == "__main__":

    student1 = Student("15487-79431", "John", "Smith", Level.Freshman)
    print(student1.__str__())
    '''
    student2 = Student("98765-43210", "Tsung Lin", "Hsia", Level.Sophomore)
    print(student2.__str__())
    student3 = Student("12345-67890", "Hsia", "TsungLin", Level.Junior)
    print(student3.__str__())
    student4 = Student("96969-12345", "Lin", "Tsung", Level.Senior)
    print(student4.__str__())
    student5 = Student("96769-12345", "Purdue", "Pete", Level.Senior)
    print(student5.__str__())
    student6 = Student("98969-12345", "John", "Mark", Level.Senior)
    print(student6.__str__())
    student7 = Student("96960-12345", "Alex", "Quinn", Level.Senior)
    print(student7.__str__())
    studentList = [student1, student2, student3, student4, student5, student6, student7]

    component1 = Component("REW - 321", ComponentType.Resistor, 1.40)
    print(component1.__str__())
    print(component1.__hash__())

    component2 = Component("REW - 123", ComponentType.Resistor, 2.50)
    print(component2.__str__())
    print(component2.__hash__())

    component3 = Component("REW - 999", ComponentType.Resistor, 2.00)
    print(component3.__str__())
    print(component3.__hash__())

    component4 = Component("REW - 876", ComponentType.Resistor, 1.90)
    print(component4.__str__())
    print(component4.__hash__())

    component5 = Component("REW - 888", ComponentType.Inductor, 1.50)
    print(component5.__str__())
    print(component5.__hash__())

    component6 = Component("REW - 777", ComponentType.Transistor, 1.00)
    print(component6.__str__())
    print(component6.__hash__())

    component7 = Component("REW - 666", ComponentType.Inductor, 0.90)
    print(component7.__str__())
    print(component7.__hash__())

    component8 = Component("REW - 667", ComponentType.Transistor, 0.92)
    print(component8.__str__())
    print(component8.__hash__())

    componentList = (component1, component2, component3, component4, component5, component6, component7)

    circuit1 = Circuit("123-321", componentList)
    print(circuit1.__str__())
    print('getByType')
    print(circuit1.getByType(ComponentType.Resistor))
    if circuit1.__contains__(component4):
        print("Circuit contain True test success")
    addBefore = []
    for com in circuit1.components:
        addBefore.append(com.ID)
    print(circuit1.cost)
    circuit1.__add__(component8)
    addAfter = []
    for com in circuit1.components:
        addAfter.append(com.ID)
    print(addBefore)
    print(addAfter)
    print(circuit1.cost)

    circuit1.__sub__(component1)
    addAfter = []
    for com in circuit1.components:
        addAfter.append(com.ID)
    print(addAfter)
    print(circuit1.cost)

    circuit2 = Circuit("123-178", (component1, component4, component3, component2))
    print(circuit2.__str__())
    if circuit2.__contains__(component5) is not True:
        print("Circuit contain False test success")

    circuit3 = Circuit("123-190", (component5, component4, component6, component1))
    print(circuit3.__str__())

    circuit4 = Circuit("123-191", (component5, component4, component6, component1))
    print(circuit4.__str__())

    # 3 cost 5.8
    if circuit1.__gt__(circuit3):
        print("circuit _gt_ success")
    if circuit3.__lt__(circuit1):
        print("circuit _lt_ success")
    if circuit3.__eq__(circuit4):
        print("circuit _eq_ success")

    proj1 = Project("38753067-e3a8-4c9e-bbde-cd13165fa21e", [student1, student2, student3], [circuit1, circuit2])
    print(proj1.__str__())
    if proj1.__contains__(student1):
        print("student contain success")
    if proj1.__contains__(circuit1):
        print("circuit contain success")
    if proj1.__contains__(student4) is not True:
        print("student does not contain success")
    if proj1.__contains__(circuit4) is False:
        print("circuit does not contain success")
    print(proj1.circuits)
    print(proj1.cost)
    proj1.__add__(circuit3)
    print(proj1.circuits)
    print(proj1.cost)

    proj1.__sub__(circuit3)
    print(proj1.circuits)
    print(proj1.cost)

    print(proj1.__getitem__("123-178"))
    #circuit1 = Circuit('11-0-88',(R=12, C=03, I=75, T=00), 123.90)
    #print(Capstone(proj1.ID,proj1.participants,proj1.circuits))
    '''

