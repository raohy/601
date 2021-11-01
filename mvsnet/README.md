

**goal:make a tool which can turn several 2d images of an object into a 3d model

approach: deep learning / mvsnet family

dataset:
  dtu:
  This data set (freely available) is aimed at multiple view stereo (MVS) evaluation, and is made using our robotic lab set up outlined here.
  An industrial robot arm was mounted with a structured light scanner. This allowed for structured light scans corresponding to each image in the data set. The images were taken by one of the cameras in the structured light scanner. A small video presenting the dataset can be found here.

The data set consist of 124 different scenes, where 80 of them have been used in the evaluation of the above mentioned paper. The remaining 44 consist mainly of scenes that have been rotatated and scanned four times with 90 degree intervals, which enables 360 degree models. A few have been removed from the evaluation due to low quality.

The scenes include a wide range of objects in an effort to span the MVS problem. At the same time, the data set also include scenes with very similar objects, e.g. model houses, such that intra class variability can be explored. Each scene has been taken from 49 or 64 position, corresponding to the number of RGB images in each scene or scan. The image resolution is 1600 x 1200. The camera positions and internal camera parameters have been found with high accuracy, via the matlab calibration toolbox, which is also the toolbox you need to retrieve these parameters.  Lastly, the scenes have been recorded in all 49 or 64 scens with seven different lighting conditions from directional to diffuse.

  etu:街景
    The multi-view stereo / 3D reconstruction benchmark covers a variety of indoor and outdoor scenes.
Ground truth geometry has been obtained using a high-precision laser scanner.
A DSLR camera as well as a synchronized multi-camera rig with varying field-of-view was used to capture images.
We offer the following challenges:

13 training and 12 test scenes (data / results) for high-resolution multi-view stereo with images recorded by the DSLR camera
5 training and 5 test videos (data / results) at ca. 13.6 Hz for low-resolution many-view stereo on video data recorded with the multi-camera rig
27 training and 20 test frames (data / results) for low-resolution two-view stereo on frames of the multi-camera rig

training process:
  
