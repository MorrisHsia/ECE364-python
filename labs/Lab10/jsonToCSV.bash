#! /bin/bash
#    email:       thsia@purdue.edu
#    ID:          ee364g21
#    Date:        3/14/19
#######################################################
DataPath=~ee364/DataFolder/Lab10
echo FACILITYNAME,FACILITYNUMBER,STREETADDRESS,TELEPHONE
grep -E "$1" $DataPath/facilities/*.json 
