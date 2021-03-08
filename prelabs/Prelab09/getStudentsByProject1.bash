DataPath=~ee364/DataFolder/Prelab09
circs=$(for c in $(bash getCircuitsByProject.bash $1); do echo $DataPath/circuits/circuit_$c.dat; done)
cat $circs | grep -E "[0-9]+-[0-9]+" | grep -f - $DataPath/maps/students.dat | cut -d"|" -f1 | sort -u
