#! /bin/bash
#######################################################
#    Author:      Tsung Lin Hsia
#    email:       thsia@purdue.edu
#    ID:          ee364g21
#    Date:        3/14/19
#######################################################
DataPath=~ee364/DataFolder/Prelab09
studentfile=$DataPath/maps/students.dat
circs=$(for c in $(bash getCircuitsByProject.bash $1); do echo $DataPath/circuits/circuit_$c.dat; done)
cat $circs | grep -E "[0-9]+-[0-9]+" | grep -f - $studentfile | cut -d"|" -f1 | sort -u
