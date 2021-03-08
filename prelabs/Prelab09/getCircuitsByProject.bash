#! /bin/bash
#######################################################
#    Author:      Tsung Lin Hsia
#    email:       thsia@purdue.edu
#    ID:          ee364g21
#    Date:        3/14/19
#######################################################
DataPath=~ee364/DataFolder/Prelab09
grep $1 $DataPath/maps/projects.dat | tr -s " " | cut -f2 -d' ' | sort -u
