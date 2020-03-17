# Automated Model Training Script on Google CoLab
---

## Upload your labeled dataset to Google Drive

Put all your image data to on folder (remember to categorize each class to individual folders), the file structure will look something like this:

```
- DATASET_NAME
	- CLASS_1_NAME
		- CLASS_1_0.jpg
		- CLASS_1_0.txt
		- CLASS_1_1.jpg
		- CLASS_1_1.txt
		- CLASS_1_2.jpg
		- CLASS_1_2.txt
		...
		- CLASS_1_n.jpg
		- CLASS_1_n.txt
	- CLASS_2_NAME
		- CLASS_2_0.jpg
		- CLASS_2_0.txt
		- CLASS_2_1.jpg
		- CLASS_2_1.txt
		- CLASS_2_2.jpg
		- CLASS_2_2.txt
		- CLASS_2_n.jpg
		- CLASS_2_n.txt
		...
	...
	- CLASS_N_NAME
		- CLASS_N_0.jpg
		- CLASS_N_0.txt
		- CLASS_N_1.jpg
		- CLASS_N_1.txt
		- CLASS_N_2.jpg
		- CLASS_N_2.txt
		- CLASS_N_n.jpg
		- CLASS_N_n.txt
		...
```



## Reference:

* [When should I stop training](https://github.com/AlexeyAB/darknet#when-should-i-stop-training)
