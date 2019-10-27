for i in {0..3}
do
	python detect.py
	if [ -f "a.txt" ]
	then
		scp a.txt pi@10.16.160.167:~/
		nohup ./ex2.sh
	fi
	rm a.txt
	rm /home/user/*.jpg
	ssh pi@10.16.160.167 << EOF
./cam.sh
EOF
	touch img1 img2 img3 img4
	sudo ./darknet detect cfg/yolov3.cfg yolov3.weights /home/user/traffic1.jpg > img1
	sudo ./darknet detect cfg/yolov3.cfg yolov3.weights /home/user/traffic2.jpg > img2
	sudo ./darknet detect cfg/yolov3.cfg yolov3.weights /home/user/traffic3.jpg > img3
	sudo ./darknet detect cfg/yolov3.cfg yolov3.weights /home/user/traffic4.jpg > img4

	sudo tr ' ' '\n' < img1 | grep 'car\|bicycle\|truck\|bus\|motorbike' | wc -l >> density.txt
	sudo tr ' ' '\n' < img2 | grep 'car\|bicycle\|truck\|bus\|motorbike' | wc -l >> density.txt
	sudo tr ' ' '\n' < img3 | grep 'car\|bicycle\|truck\|bus\|motorbike' | wc -l >> density.txt
	sudo tr ' ' '\n' < img4 | grep 'car\|bicycle\|truck\|bus\|motorbike' | wc -l >> density.txt
	echo $i >> density.txt
	cat density.txt
	python new_time.py
	cat t.txt
	scp t.txt pi@10.16.160.167:~/
	sudo rm detect.py density.txt img1 img2 img3 img4
	nohup ./ex.sh &
	#sudo rm data/*.jpg
done
