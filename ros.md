# Robot Operating System (ros)
## ダウンロード後の環境変数設定
.bashrcにて以下の内容を追記する。
```
source /opt/ros/kinetic/setup.bash
#export ROS_MASTER_URI=http://192.168.1.11:11311
#export ROS_HOSTNAME=192.168.1.10
#export ROS_MASTER_URI=http://10.42.0.2:11311
#export ROS_HOSTNAME=10.42.0.2
export ROS_MASTER_URI=http://localhost:11311
export ROS_HOSTNAME=localhost
alias cw='cd ~/catkin_ws'
alias cs='cd ~/catkin_ws/src'
alias cm='cd ~/catkin_ws && catkin_make'
source ~/catkin_ws/devel/setup.bash
```