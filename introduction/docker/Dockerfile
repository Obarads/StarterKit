FROM nvidia/cuda:11.1-cudnn8-devel-ubuntu18.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wget \
    curl \
    git \
    vim \
    libboost-all-dev \
    cmake \
    unzip \
    sudo \
    libffi-dev \
    libssl-dev \
    build-essential \
    libopenblas-dev \
    libsparsehash-dev\
    python3-dev python3-venv \
    iproute2 \
    procps \
    lsb-release \
    libsm6 \
    libxext6 \
    libxrender-dev \
    ninja-build

ARG UID
ARG GID

RUN groupadd -g ${GID} host-group
RUN useradd -u ${UID} -g ${GID} -m coder
RUN gpasswd -a coder sudo
RUN echo "coder:qwer1234" | chpasswd
USER ${UID}
ENV HOME /home/coder
ENV SHELL /bin/bash

RUN echo "\n\
    export LANG=C.UTF-8 \n\
    export LANGUAGE=en_US \n\
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;33m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ ' \n\
    " >> /home/coder/.bashrc


