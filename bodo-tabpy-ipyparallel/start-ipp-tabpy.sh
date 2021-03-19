#!/bin/bash -x

source /opt/conda/etc/profile.d/conda.sh

conda activate Bodo

# Start IPP cluster with MPI on 4 CPU Cores
ipcluster start -n 4 --engines=MPIEngineSetLauncher --log-level=DEBUG --daemonize

# Start TabPy Server
/opt/conda/envs/Bodo/lib/python3.8/site-packages/tabpy_server/startup.sh
