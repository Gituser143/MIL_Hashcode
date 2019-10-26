sudo touch img1 img2 img3 img4;
if [ -f "data/traffic4.jpg" ]
then
	sudo ./darknet detect cfg/yolov3.cfg yolov3.weights data/traffic1.jpg > img1
	sudo ./darknet detect cfg/yolov3.cfg yolov3.weights data/traffic2.jpg > img2
	sudo ./darknet detect cfg/yolov3.cfg yolov3.weights data/traffic3.jpg > img3
	sudo ./darknet detect cfg/yolov3.cfg yolov3.weights data/traffic4.jpg > img4

	sudo tr ' ' '\n' < img1 | grep 'car\|bicycle\|truck\|bus\|motorbike' | wc -l >> density.txt
	sudo tr ' ' '\n' < img2 | grep 'car\|bicycle\|truck\|bus\|motorbike' | wc -l >> density.txt
	sudo tr ' ' '\n' < img3 | grep 'car\|bicycle\|truck\|bus\|motorbike' | wc -l >> density.txt
	sudo tr ' ' '\n' < img4 | grep 'car\|bicycle\|truck\|bus\|motorbike' | wc -l >> density.txt
	if [ -f "density.txt" ]
	then
		sudo rm img1 img2 img3 img4
		sudo python3 py_time.py
		sudo rm density.txt
		#su user
		sudo scp t.txt pi@192.168.43.8:~/
		sudo rm t.txt
	fi
	sleep 30
fi
