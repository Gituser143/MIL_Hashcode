echo "GOTO1"
fswebcam -S 20 -d /dev/video0 traffic1.jpg;
echo "GOTO2"
sleep 5
fswebcam -S 20 -d /dev/video0 traffic2.jpg;
scp traffic1.jpg user@10.16.160.171:~/
scp traffic2.jpg user@10.16.160.171:~/
echo "GOTO3"
sleep 5
fswebcam -S 20 -d /dev/video0 traffic3.jpg;
echo "GOTO4"
sleep 5
fswebcam -S 20 -d /dev/video0 traffic4.jpg;
scp traffic3.jpg user@10.16.160.171:~/
scp traffic4.jpg user@10.16.160.171:~/

