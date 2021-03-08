#! /bin/bash
#    email:       thsia@purdue.edu
#    ID:          ee364g21
#    Date:        3/14/19
#######################################################
DataPath=~ee364/DataFolder/Lab10
grep -E "$1" $DataPath/facilities.txt | grep -Eo "[0-9]{9}" | grep -lr -E -f - $DataPath/facilities/*json | grep -Eo "[0-9]{5}" | sort -u

