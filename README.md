mkdir TT100K && cd TT100K

wget http://cg.cs.tsinghua.edu.cn/traffic-sign/data_model_code/data.zip

unzip data.zip

cd ..

git clone --depth=1 https://github.com/AlexeyAB/darknet.git

cd darknet

modify makefile:
GPU=1
CUDNN=1
CUDNN_HALF=1
OPENCV=1
LIBSO=1
ARCH= 

make

cd ..

git clone --depth=1 https://github.com/halftop/TT100K_YOLO_Label.git
