FROM continuumio/miniconda  


RUN conda create -n Bodo python=3.8 && \
    conda install bodo -c bodo.ai -c conda-forge -n Bodo

RUN conda install tabpy-server ipyparallel -y -n Bodo

EXPOSE 9004
