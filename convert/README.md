# Workflow

## Prerequisites

* Tensorflow in Python 3
* (Kendryte NCC Toolchain)[https://cocoroboai.s3-ap-southeast-1.amazonaws.com/ncc.zip]
* Linux CLI set:
	* `unzip`
	* `python 3.6`
	* `wget`

```
rm cfg/bckss.cfg && rm bin/bckss.weights
cp ../bckss-v2/yolo-obj.cfg cfg/bckss.cfg && cp ../bckss-v2/backup/yolo-obj_last.weights bin/bckss.weights
source activate tensorflow_p36
./flow --model cfg/bckss.cfg --load bin/bckss.weights --savepb

rm workspace/bckss.meta && rm workspace/bckss.pb
cp ../darkflow/built_graph/bckss.meta workspace/bckss.meta && cp ../darkflow/built_graph/bckss.pb workspace/bckss.pb
rm workspace/bckss.tflite
./pb2tflite.sh workspace/bckss.pb
# copy some testing images to images directory
bash tflite2kmodel.sh workspace/bckss.tflite
```
---

## Reference:
* https://medium.com/@manivannan_data/how-to-train-multiple-objects-in-yolov2-using-your-own-dataset-2b4fee898f17