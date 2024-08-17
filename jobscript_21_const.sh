#!/bin/bash

#SBATCH --job-name=test         # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --cpus-per-task=18        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=8GB         # memory per cpu-core (4G is default)
#SBATCH --time=00:45:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=end,fail          # send email when job ends
#SBATCH --mail-user=gm1710@princeton.edu

module purge
module load anaconda3/2022.5

conda activate powergenome
python /home/gm1710/PowerGenome/powergenome/run_powergenome_multiple_outputs_cli.py -sf /home/gm1710/Real_Conus_Aggs/conus_21z_const_settings.yml -rf /home/gm1710/Real_Conus_Aggs/results_21z_const
