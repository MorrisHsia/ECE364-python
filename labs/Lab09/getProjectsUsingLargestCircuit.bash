#! /bin/bash
#######################################################
#    Author:      Tsung Lin Hsia
#    email:       thsia@purdue.edu
#    ID:          ee364g21
#    Date:        3/14/19
#######################################################
DataPath=~ee364/DataFolder/Lab09
ls $DataPath/circuits -lS | head -n 2 | tail -n 1 | grep -oE "[0-9]{2}-[0-9]-[0-9]{2}" | grep -f - $DataPath/maps/projects.dat | grep -oE "[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}"  | sort -u

#head -n 1 $file

