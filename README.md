# Mask-Wear-Detector
The Mask Wear Detector is a computer vision-based project that uses YOLOv5, a state-of-the-art algorithm used for real time object detection, to detect whether individuals are wearing masks or not. The project aims to enhance public safety and promote mask-wearing compliance in various settings, such as public places, workplaces, and transportation hubs.
 
<p align="center"> <img src="results\public2_AdobeExpress.gif" /></p>

## Dataset
The model was trained on [Face-Mask](https://www.kaggle.com/andrewmvd/face-mask-detection) dataset which contains 853 images belonging to 3 classes, as well as their bounding boxes in the PASCAL VOC format. The classes are defined as follows:
* `With mask`
* `Without mask`
* `Mask worn incorrectly`

## How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Vinit21592/Face-Mask-Detection.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n maskdt python=3.7 -y
```

```bash
conda activate maskdt
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```