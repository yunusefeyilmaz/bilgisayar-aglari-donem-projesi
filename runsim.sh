#./ns3 run scratch/network-simulation -- --randomStream=2 --ueNumPergNb=10 --ueVelocity=40
script="scratch/network-simulation"

#2 car 20m/s
nDevices=2  # Change from 2 to 10
MaxSpeed=20 # Change from 20 to 80
folder="scratch/experiments/Test_${MaxSpeed}_${nDevices}/run"
echo -n "Running experiments: "
for r in `seq 1 30`;
do
  echo -n " $r"
  mkdir -p $folder${r}
	./ns3 run "$script --randomStream=$r --ueNumPergNb=$nDevices ueVelocity=$MaxSpeed --outputDir=${folder}${r}" > "$folder${r}/log.txt" 2>&1
done

echo " END"

#5 car 20m/s
nDevices=5  # Change from 2 to 10
MaxSpeed=20 # Change from 20 to 80
folder="scratch/experiments/Test_${MaxSpeed}_${nDevices}/run"
echo -n "Running experiments: "
for r in `seq 1 30`;
do
  echo -n " $r"
  mkdir -p $folder${r}
	./ns3 run "$script --randomStream=$r --ueNumPergNb=$nDevices ueVelocity=$MaxSpeed --outputDir=${folder}${r}" > "$folder${r}/log.txt" 2>&1
done

echo " END"

#5 car 60m/s
nDevices=5  # Change from 2 to 10
MaxSpeed=60 # Change from 20 to 80
folder="scratch/experiments/Test_${MaxSpeed}_${nDevices}/run"
echo -n "Running experiments: "
for r in `seq 1 30`;
do
  echo -n " $r"
  mkdir -p $folder${r}
	./ns3 run "$script --randomStream=$r --ueNumPergNb=$nDevices ueVelocity=$MaxSpeed --outputDir=${folder}${r}" > "$folder${r}/log.txt" 2>&1
done

echo " END"

#10 car 20m/s
nDevices=10  # Change from 2 to 10
MaxSpeed=20 # Change from 20 to 80
folder="scratch/experiments/Test_${MaxSpeed}_${nDevices}/run"
echo -n "Running experiments: "
for r in `seq 1 30`;
do
  echo -n " $r"
  mkdir -p $folder${r}
	./ns3 run "$script --randomStream=$r --ueNumPergNb=$nDevices ueVelocity=$MaxSpeed --outputDir=${folder}${r}" > "$folder${r}/log.txt" 2>&1
done

echo " END"
