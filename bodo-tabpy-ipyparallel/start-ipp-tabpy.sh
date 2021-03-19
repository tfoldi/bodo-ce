#!/bin/bash -x

# keep SNOWFLAKE_URL between conda envs
echo export SNOWFLAKE_URL=$SNOWFLAKE_URL > /opt/conda/envs/Bodo/etc/conda/activate.d/snowflake.sh

# activate Bodo
source /opt/conda/etc/profile.d/conda.sh
conda activate Bodo

# Start IPP cluster with MPI on 4 CPU Cores
ipcluster start -n 4 --engines=MPIEngineSetLauncher --log-level=DEBUG --daemonize

# Start TabPy Server
export TABPY_PORT=8080
(sleep 5 && python lr-bodo-tabpy.py) & 
tabpy 