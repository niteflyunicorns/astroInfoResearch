#!/bin/bash
#SBATCH --job-name=snaps  #the name of your job

#change to your NAUID
#SBATCH --output=/scratch/sjc497/astMat.out #this is the file for stdout 
#SBATCH --error=/scratch/sjc497/astMat.err #this is the file for stderr

#SBATCH --time=06:00:00        #Job timelimit is 4 hours
#SBATCH --mem=8GB        #memory requested in MiB
#SBATCH --cpus-per-task=1

# VARIABLES ---------------------------------------
# required variables:
maxIn=1000
offset=2478
fltrType=2
fltrLvl=40
plots=n
exportFlg=y

# optional variables:
fileType=1 # default 2 (.csv)
fileName="~/astroInfoResearch/astroInfo/2478-3478GTE40" # default ""
astName=0 # default 0
featFltr=n # default n
lB=0 # default 0
uB=0 # default 0


# PROFILING ---------------------------------------
# time kernprof -lv astOutlierMatNew.py "$maxIn" "$offset" "$fltrType" "$fltrLvl" "$plots" "$exportFlg"


# RUNNING -----------------------------------------
# No export, multiple asteroids
# time python astOutlierMatNew.py "$maxIn" "$offset" "$fltrType" "$fltrLvl" "$plots" "$exportFlg"

# Export multiple asteroids
time python astOutlierMatNew.py "$maxIn" "$offset" "$fltrType" "$fltrLvl" "$plots" "$exportFlg" "$fileType" "$fileName"

# No export, single asteroid
# time python astOutlierMatNew.py "$maxIn" "$offset" "$fltrType" "$fltrLvl" "$plots" "$exportFlg" "$astName" "$featFltr" "$lB" "$"uB"

# Export single asteroid
# time python astOutlierMatNew.py "$maxIn" "$offset" "$fltrType" "$fltrLvl" "$plots" "$exportFlg" "$fileType" "$fileName" "$astName" "$featFltr" "$lB" "$"uB"

# if [$(maxIn) == -1]; then
# fi

# if [$(maxIn) == 1]; then
# 	echo -n "file type: "
# 	read fileType
# 	echo -n "file name: "
# 	read fileName
# fi

# if [$(exportFlg) == 'n']; then
# fi



   # New Program Variables / Args

   # number of asteroids
   # if only one:
   # 	  get name
   # 	  feature to filter by
   # 	  lower bound
   # 	  upper bound

   # export results flag
   # if yes:
   # 	  file type
   # 	  file name
		 
   # starting position
	  
   # filter type
   # filter value