# 601A1
## Multi-View Stereo
### What is Multi-View Stereo?
  Multi-view stereo (MVS) is a general term for a series of methods of multi-view 3D reconstruction which refers to the task of reconstructing a 3D shape from calibrated overlapping images captured from different viewpoints. In short, it uses multiple photos taken by multiple cameras to reconstruct the scene in the photo.
![](/images/1.png)
<p align="center">
                                                                                    Figure1
  </p>
                                                                  
  For example, in the picture above, we took different images of the Buddha statue in different orientations. Different images contain different and overlapping information about the Buddha statues. The main goal of the MVS is to use an algorithm to maximize the use of the information get from the images to model the Buddha statue in 3D. 
### Why MVS is important?
  MVS is widely used range from 3D mapping and navigation to online shopping, 3D printing, computational photography, computer video games, or cultural heritage archival.
  
  ![](/images/AR.png) ![](/images/autonomous.png) ![](/images/robots.png)
<p align="center">
                                                                                    Figure2
  </p>
   In the robotics, MVS can be used by a single camera to obtain the position and posture of the object to assist the grasping of the robotic arm. In the remote sensing, processing millions of photographs over hundreds of kilometers at a time, mvs can effectively reconstructing large metropolitan and rural areas. In autonomous driving, using MVS can more accurately generate models of nearby objects to assist obstacle avoidance. These all are the applications of MVS. They are widely used in our daily life, but we rarely pay attention to them.
   
### Literature review
  MVS originated as a natural improvement to the two-view case. Until this day, two-view stereo algorithms have been a very active and fruitful research area. Instead of capturing two photographs from two different viewpoints, multi-view stereo would capture more viewpoints in-between to increase robustness which significantly increase the difficulty. Two major breakthroughs nowsdays gradually trun two-view into multi-view. First is the improvements in digital cameras and computation power which makes the photos to be more precise and enables the algorithms to easily handle tens of thousands of images. Second is the improvements of Algorithms over decades. With these two changes, MVS gradually step into the industry from the lab.
  After decades of development, the algorithm of MVS has gradually matured, and the 3D modeling accuracy has become higher and higher. According to the method, it can be divided into two categories. The first is the traditional statistical-like algorithm, and the second is the modeling method based on deep learning after 2015.
  
#### Statistics-like method

#### Deep learning methed
##### MVSNet
  After 2010, cnn has achieved sota results in more and more image processing tasks. Many people begun to wonder whether CNN can be used in the mvs, but the results obtained are not satisfactory. Until the proposal of MVSNet, the first to apply cost volume to the neural network, obtained a very good experimental result. MVSNet can be regarded as the originator of the application of neural networks to the MVS field.
  ![](/images/MVSNet.png)
<p align="center">
                                                                                    Figure3
  </p>
  In the paper, the author proposed an end-to-end deep learning architecture for depth map inference(see Figure3). The network takes one reference image and several source images as input, then use the convolutional network to obtain the feature maps separately. The key insight is the differentiable homography warping operation, which implicitly encodes camera geometries in the network to build the 3D cost volumes from 2D image features maps. And then a variance-based metric was proposed that maps multiple features into one cost feature in the volume. Cost volume then undergoes multi-scale 3D convolutions and regress an initial depth map. Finally, the depth map is refined with the reference image to improve the accuracy of boundary areas.
  After the network was proposed, many researchers generally accepted this idea and many improved versions were proposed on MVSNET, such as R-MVSNet, Fast-MVSNet and Cas-MVSNet. 
  
![](/images/overall.png)
<p align="center">
                                                                                    Figure4
  </p>
  Figure 4 is the performance comparison diagram of the existing neural network-based MVS algorithm. From this picture, we can find that the best method today is CVP-MVSNet based on neural networks, with a minimum distance error of 0.351 which is much smaller than the traditional method. And it is worth noting that unsupervised method also achieve a good result which was proposed in 2021 and was a very promising direction in the future.
  
### Open Source Project
#### PMVS
  PMVS is probably the first successful open-source MVS software, which has been extensively used by nonexperts such as artists and civil engineers. PMVS is a multi-view stereo software that takes a set of images and camera parameters, then reconstructs 3D structure of an object or a scene visible in the images. This project started in 2007. With the emergence of new algorithms, this software is constantly updated, such as PMVS2, CMVS, etc., and it is now a fairly mature open source product.
#### MVE
  The Multi-View Environment, MVE, is an implementation of a complete end-to-end pipeline for image-based geometry reconstruction. It features Structure-from-Motion, Multi-View Stereo and Surface Reconstruction. MVE is written in C++ and comes with a set of efficient, cross-platform and easy-to-use libraries.
#### OpenMVG
  OpenMVG's mission is to extend awareness of the power of 3D reconstruction from images by developing a C++ framework. The library also includes the two complete SfM pipelines and provides customizable tools to help engineers to deal with MVS problems.


The goal of an image-based 3D reconstruction algorithm can be de- scribed as ”given a set of photographs of an object or a scene, estimate
the most likely 3D shape that explains those photographs, under the assumptions of known materials, viewpoints, and lighting conditions” (See Figure 1.1).
