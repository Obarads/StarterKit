# Create user (name:coder).
# create_user.sh 2000 3000
# -> $1=2000, $2=3000
# $1: User ID
# $2: Group id

# create user (coder).
groupadd -g $2 host-group
useradd -u $1 -g $2 -m coder -s /bin/bash
gpasswd -a coder sudo
echo "coder:qwer1234" | chpasswd

# change python 2.7 to conda python.
# change cli color.
echo "\n\
export LANG=C.UTF-8 \n\
export LANGUAGE=en_US \n\
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;33m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ ' \n\
# change user PATH to root PATH \n\
# user PATH \n\
# export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games \n\
# root PATH \n\
export PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/opt/bin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \n\
" >> /home/coder/.bashrc

# add symbol links.
ln -s /mnt/codebox/ /home/coder/codebox
ln -s /mnt/databox/ /home/coder/databox

# add su coder.
echo "\n\
su coder \n\
" >> /root/.bashrc

