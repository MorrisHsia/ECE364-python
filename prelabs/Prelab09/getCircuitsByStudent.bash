#! /bin/bash
#######################################################
#    Author:      Tsung Lin Hsia
#    email:       thsia@purdue.edu
#    ID:          ee364g21
#    Date:        3/14/19
#######################################################
DataPath=~ee364/DataFolder/Prelab09
ID=$(cat $DataPath/maps/students.dat | grep -E "$1" | grep -oE "[0-9]{5}-[0-9]{5}")
grep -lr -E $ID $DataPath/circuits | grep -E -o "[0-9]{2}-[0-9]-[0-9]{2}" | sort -u

