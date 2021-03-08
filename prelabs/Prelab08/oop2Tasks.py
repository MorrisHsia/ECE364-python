#! /user/local/bin/python3.7
#######################################################
#   Author:     Tsung Lin Hsia
#   email:      thsia@purdue.edu
#   ID:         ee364g21
#   Date:       03/03/19
#######################################################
import collections
from copy import deepcopy
from enum import Enum
class Datum:
    _storage = ()
    def __init__(self,*args):
        temp = []
        for a in args:
            if type(a) is not float:
                raise TypeError("Needs to be float")
            else:
                temp.append(a)
        self._storage = tuple(temp)
    def __str__(self):
        output = []
        for i in self._storage:
            output.append(round(i,2))
        return str(tuple(output))

    def __hash__(self):
        return(hash(self._storage))
    def __repr__(self):
        return self.__str__()

    def distanceFrom(self,other):
        if not isinstance(other,Datum):
            raise TypeError("The input in the question is not an instance of Datum Class")
        temp1 = list(self._storage)
        temp2 = list(other._storage)
        temp3 = []
        total = 0.0
        if len(temp1) - len(temp2):
            for i in range(len(temp1) - len(temp2)):
                temp2.append(0.0)
        elif len(temp2) - len(temp1):
            for i in range(len(temp2) - len(temp1)):
                temp1.append(0.0)
        for i in range(len(temp1)):
            total+=(temp1[i] - temp2[i])**2
        total = total**0.5
        return total

    def clone(self):
        other = deepcopy(self)
        return other
    def __contains__(self, item):
        if type(item) is not float:
            raise TypeError("The item is not type float")
        if item in self._storage:
            return True
        else:
            return False
    def __len__(self):
        return(len(self._storage))

    def __iter__(self):
        return (iter(self._storage))

    def __neg__(self):
        output = []
        for i in self._storage:
            output.append(-i)
        new_obj = Datum(*output)
        return new_obj

    def __getitem__(self, item):
        return self._storage[item]

    def __add__(self, other):
        if not isinstance(other,Datum):
            if type(other) is not float:
                raise TypeError('Wrong input, should be either Datum class or type float')
        if isinstance(other,Datum):
            temp1 = list(self._storage)
            temp2 = list(other._storage)
            temp3 = []
            if len(temp1) - len(temp2):
                for i in range(len(temp1) - len(temp2)):
                    temp2.append(0.0)
            elif len(temp2) - len(temp1):
                for i in range(len(temp2) - len(temp1)):
                    temp1.append(0.0)
            for i in range(len(temp1)):
                temp3.append(temp1[i] + temp2[i])
            new_obj = Datum(*temp3)
            return new_obj
        elif type(other) is float:
            temp = []
            [temp.append(self._storage[i] + other) for i in self._storage]
            new_obj = Datum(*temp)
            return new_obj
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other,Datum):
            if type(other) is not float:
                raise TypeError('Wrong input, should be either Datum class or type float')
        if isinstance(other,Datum):
            temp1 = list(self._storage)
            temp2 = list(other._storage)
            temp3 = []
            if len(temp1) - len(temp2):
                for i in range(len(temp1) - len(temp2)):
                    temp2.append(0.0)
            elif len(temp2) - len(temp1):
                for i in range(len(temp2) - len(temp1)):
                    temp1.append(0.0)
            for i in range(len(temp1)):
                temp3.append(temp1[i] - temp2[i])
            new_obj = Datum(*temp3)
            return new_obj
        elif type(other) is float:
            temp = []
            [temp.append(self._storage[i] - other) for i in self._storage]
            new_obj = Datum(*temp)
            return new_obj

    def __mul__(self, other):
        if type(other) is not float:
            raise TypeError("Not a type float")
        temp = []
        [temp.append(self._storage[i] * other) for i in range(len(self._storage))]
        new_obj = Datum(*temp)
        return new_obj
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) is not float:
            raise TypeError("Not a type float")
        temp = []
        [temp.append(self._storage[i] / other) for i in range(len(self._storage))]
        new_obj = Datum(*temp)
        return new_obj

    def __eq__(self, other):
        if not isinstance(other,Datum):
            raise TypeError("The input in the question is not an instance of Datum Class")
        return True if Datum.distanceFrom(self,Datum(0.0)) == Datum.distanceFrom(other,Datum(0.0)) else False
    def __ne__(self, other):
        if not isinstance(other,Datum):
            raise TypeError("The input in the question is not an instance of Datum Class")
        return True if Datum.distanceFrom(self,Datum(0.0)) != Datum.distanceFrom(other,Datum(0.0)) else False
    def __gt__(self, other):
        if not isinstance(other,Datum):
            raise TypeError("The input in the question is not an instance of Datum Class")
        return True if Datum.distanceFrom(self,Datum(0.0)) > Datum.distanceFrom(other,Datum(0.0)) else False
    def __lt__(self, other):
        if not isinstance(other,Datum):
            raise TypeError("The input in the question is not an instance of Datum Class")
        return True if Datum.distanceFrom(self,Datum(0.0)) < Datum.distanceFrom(other,Datum(0.0)) else False
    def __ge__(self, other):
        if not isinstance(other,Datum):
            raise TypeError("The input in the question is not an instance of Datum Class")
        return True if Datum.distanceFrom(self,Datum(0.0)) >= Datum.distanceFrom(other,Datum(0.0)) else False
    def __le__(self, other):
        if not isinstance(other,Datum):
            raise TypeError("The input in the question is not an instance of Datum Class")
        return True if Datum.distanceFrom(self,Datum(0.0)) <= Datum.distanceFrom(other,Datum(0.0)) else False

class Data(collections.UserList):
    def __init__(self,initial=None):
        super(Data,self).__init__()
        if initial is None:
            self.data = list()
            print("None")
        else:
            self.data = initial
        for element in self.data:
            if not isinstance(element,Datum):
                raise TypeError("need to be Datum instance")

    def __str__(self):
        return repr(self.data)

    def computeBounds(self):
        maxlength = 0
        tempselflist = deepcopy(self.data)
        for datum in self.data:
            if len(datum) > maxlength:
                maxlength = len(datum)
        for i,datum in enumerate(tempselflist):
            if len(datum) < maxlength:
                temp = list(datum._storage)
                for x in range(maxlength - len(datum)):
                    temp.append(0.0)
                tempselflist[i] = Datum(*temp)
        datummax = Datum(*tuple(map(max, zip(*tempselflist))))
        datummin = Datum(*tuple(map(min, zip(*tempselflist))))
        return datummin,datummax

    def computeMean(self):
        maxlength = 0
        tempselflist = deepcopy(self.data)
        for datum in self.data:
            if len(datum) > maxlength:
                maxlength = len(datum)
        for i,datum in enumerate(tempselflist):
            if len(datum) < maxlength:
                temp = list(datum._storage)
                for x in range(maxlength - len(datum)):
                    temp.append(0.0)
                tempselflist[i] = Datum(*temp)
        summ = list(map(sum, zip(*tempselflist)))
        datummean = Datum(*[i/len(self.data) for i in summ])
        return datummean

    def append(self,item):
        if not isinstance(item, Datum):
            raise TypeError("The input in the question is not an instance of Datum Class")
        super().append(item)

    def count(self,item):
         if not isinstance(item, Datum):
             raise TypeError("The input in the question is not an instance of Datum Class")
         return super().count(item)
    def index(self, item, *args):
         if not isinstance(item, Datum):
             raise TypeError("The input in the question is not an instance of Datum Class")
         return super().index(item)
    def insert(self, i: int, item):
         if not isinstance(item, Datum):
             raise TypeError("The input in the question is not an instance of Datum Class")
         super().insert(item)
    def remove(self, item):
        if not isinstance(item, Datum):
            raise TypeError("The input in the question is not an instance of Datum Class")
        super().remove(item)

    def __setitem__(self, key, value):
        if not isinstance(value, Datum):
            raise TypeError("The input in the question is not an instance of Datum Class")
        super().__setitem__(key,value)
    #
    def extend(self, other):
         if not isinstance(other, Data):
             raise TypeError("The input in the question is not an instance of Datum Class")
         super().extend(other)

class DataClass(Enum):
    Class1 = 1
    Class2 = 2

class DataClassifier:
    def __init__(self,group1,group2):
        if not isinstance(group1,Data) or not isinstance(group2,Data):
            raise TypeError("Group1 or Group2 is not class Data")
        if not group1 or not group2:
            raise ValueError("Group1 or Group2 is empty")
        self._class1 = group1
        self._class2 = group2
    def classify(self,item):
        if not isinstance(item, Datum):
            raise TypeError("Group1 or Group2 is not class Datum")
        mean1 = self._class1.computeMean()
        mean2 = self._class2.computeMean()
        dist1 = item.distanceFrom(mean1)
        dist2 = item.distanceFrom(mean2)
        if dist1 > dist2:
            return DataClass.Class2
        elif dist1 < dist2:
            return DataClass.Class1

if __name__ == "__main__":
    datum1 = Datum(1.05, 2.224, 3424.32132, 4424.32137, 6666.6666)
    datum2 = Datum(2.05, 3.222, 4424.32135, 5424.32132)
    #print(datum1[1])
    #print(datum1.distanceFrom(datum2))
    #print(len(datum1))
    #print(-datum1)
    #print(datum1 <= datum2)
    #print(-datum1)
    #print(datum1*3.0)
    data1 = Data([datum1,datum2])
    #print(data1)
    #print(data1.computeMean())
    print(data1)
    print("DATA1 ComputeBounds", data1.computeBounds())
    print(data1)
    data1.__setitem__(1,datum1)
    print(data1)
    #data1.remove(datum1)
    #print(data1)
    data2 = Data([datum1,datum1])
    data1.extend(data2)
    print(data1)
    print(data1.count(datum1))
    print(data1.index(datum1))
    data11 = Data([datum1,datum2])
    data22 = Data([datum2,datum1])
    dataclassifier1 = DataClassifier(data11,data22)
    #print(repr(dataclassifier1.classify))


