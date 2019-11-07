#!/bin/bash
fswebcam -S 20 -d /dev/video0 traffic1.jpg;
fswebcam -S 20 -d /dev/video2 traffic2.jpg;

sudo scp traffic1.jpg user@10.20.204.67:~/
sudo scp traffic2.jpg user@10.20.204.67:~/

sleep 3;
fswebcam -S 20 -d /dev/video0 traffic3.jpg;
fswebcam -S 20 -d /dev/video2 traffic4.jpg;

sudo scp traffic3.jpg user@10.20.204.67:~/
sudo scp traffic4.jpg user@10.20.204.67:~/

#rm *.jpg



