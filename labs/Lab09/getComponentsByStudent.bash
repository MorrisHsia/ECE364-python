#! /bin/bash
#######################################################
#    Author:      Tsung Lin Hsia
#    email:       thsia@purdue.edu
#    ID:          ee364g21
#    Date:        3/14/19
#######################################################
DataPath=~ee364/DataFolder/Lab09
student="$1"
ID=$(egrep -w "$student" $DataPath/maps/students.dat | cut -d"|" -f2)


cat $(grep -lr -E $ID $DataPath/circuits) | grep -E -o "[A-Z]{3}-[0-9]{3}" | sort -u
