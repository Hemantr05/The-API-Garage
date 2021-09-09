git clone https://github.com/pjreddie/darknet.git
cd darknet
sed -i 's/OPENCV=0/OPENCV=1/g' Makefile
sed -i 's/GPU=0/GPU=1/g' Makefile
sed -i 's/CUDNN=0/CUDNN=1/g' Makefile
sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/g' Makefile
make &> make.log
wget https://pjreddie.com/media/files/yolov3.weights
