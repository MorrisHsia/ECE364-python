#! /bin/bash
#######################################################
#    Author:      Tsung Lin Hsia
#    email:       thsia@purdue.edu
#    ID:          ee364g21
#    Date:        3/14/19
#######################################################
DataPath=~ee364/DataFolder/Prelab09
circuitsPath=$DataPath/circuits
component1=$1
component2=$2
found1=$(grep -l $component1 $circuitsPath/*dat)
found2=$(grep -l $component2 $circuitsPath/*dat)
count1="${#found1}"
count2="${#found2}"
if [[ $count1 > $count2 ]]
then
    echo $component1
elif [[ $count2 > $count1 ]]
then
    echo $component2
else
    echo "Same used times"
fi
