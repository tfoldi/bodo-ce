FROM continuumio/miniconda  


RUN conda create -n Bodo python=3.8 && \
    conda install bodo -c bodo.ai -c conda-forge -n Bodo

RUN git clone https://github.com/Bodo-inc/Bodo-examples

RUN conda install ipyparallel scipy -y -n Bodo -c conda-forge

RUN conda run -n Bodo pip install snowflake-sqlalchemy tabpy

