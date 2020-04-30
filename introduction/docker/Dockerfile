FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

RUN apt-get update && apt-get install -y \
python3 \
python3-pip \
wget \
curl \
git \
vim \
libboost-all-dev \
cmake
RUN echo -e $"\n\
export LANG=C.UTF-8 \n\
export LANGUAGE=en_US \n\
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;33m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ ' \n\
alias py36='conda activate py36' \n\
" >> /root/.bashrc
