echo "\n\
export LANG=C.UTF-8 \n\
export LANGUAGE=en_US \n\
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;33m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ ' \n\
" >> /root/.bashrc

# add symbol links.
ln -s /mnt/codebox/ /root/codebox
ln -s /mnt/databox/ /root/databox

