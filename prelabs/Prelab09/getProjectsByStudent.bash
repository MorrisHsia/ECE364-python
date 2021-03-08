#! /bin/bash
#######################################################
#    Author:      Tsung Lin Hsia
#    email:       thsia@purdue.edu
#    ID:          ee364g21
#    Date:        3/14/19
#######################################################
DataPath=~ee364/DataFolder/Prelab09

grep -w "$1" $DataPath/maps/students.dat | grep -oE "[0-9]{5}-[0-9]{5}" | grep -lr -E -f - $DataPath/circuits | grep -E -o "[0-9]{2}-[0-9]-[0-9]{2}" | grep -E -f - $DataPath/maps/projects.dat |  grep -oE "[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}"  | sort -u

