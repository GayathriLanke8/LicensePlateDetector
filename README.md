# License Plate Detector🥸
This project uses [OpenCV](https://opencv.org/), [Matplotlib](https://matplotlib.org/), [EasyOCR](https://github.com/JaidedAI/EasyOCR), and a [YOLO (Ultralytics)](https://github.com/ultralytics/ultralytics) object detection model from Ultralytics to detect vehicle license plates from images or video frames.
Once a license plate is detected, the project extracts the alphanumeric license number using OCR and identifies the Indian state/region of registration based on the first two characters of the plate (e.g., AP → Andhra Pradesh).

🛠️ Tech Stack  
- OpenCV — Computer vision library for image processing
- Matplotlib — Plotting and visualization library
- EasyOCR — Optical character recognition tool  
- YOLO (Ultralytics) — Object detection model


  
## Dependencies
#### The License plate Detector needs to be downloaded from [this repository](https://github.com/JaidedAI/EasyOCR).

## Project Setup
* Make an environment with conda using the following command
  
  ```bash
  conda create -n lp_pipeline python=3.12.11

* Activate Environment

  ```bash
  conda activate lp_pipeline
  
* Install the project dependencies using the following command
  
  ```bash
  pip install -r requirements.txt

* Run run.py to get the output

  ```bash
  python run.py



#Output / Results  

**License Plate Detection**
![License Plate Detection](detection_img.png)
License Plate Detection: Shows the detected license plate highlighted with a bounding box on the vehicle.  
OCR Extraction: The extracted alphanumeric text of the license plate is displayed.  
State Identification: Displays the corresponding Indian state based on the license plate prefix.  
