# 601A1
## Multi-View Stereo
  Multi-view stereo (MVS) is a general term for a series of methods of multi-view 3D reconstruction which refers to the task of reconstructing a 3D shape from calibrated overlapping images captured from different viewpoints. In short, it uses multiple photos taken by multiple cameras to reconstruct the scene in the photo.
![](/images/1.png)
  In the picture above, we took different images of the Buddha statue in different orientations. Different images contain different information about Buddha statues. The main goal of the MVS is finding an algorithm to maximize the use of this information to model the Buddha statue in 3D. 

  MVS originated as a natural improvement to the two-view case. Until this day, two-view stereo algorithms have been a very active and fruitful research area. In two-view stereo, only two images from different angels are taken. 
  
  Instead of capturing two photographs from two different viewpoints, multi-view stereo would capture more viewpoints in-between to increase robustness which significantly increase the difficulty. Two major breakthroughs in nowsdays gradually trun two-view into multi-view. First is the improvements in digital cameras and computation power which makes the photos to be more precise and enables the algorithms to easily handle tens of thousands of images. Second is the improvements of Algorithms over decades. With these two changes, MVS gradually step into the industry from the lab.
  
MVS is used in many aspects of production and life such as VR/AR, autonomous driving and Robot manupilation. 
  ![](/images/AR.png) ![](/images/autonomous.png) ![](/images/robot.png)
Its applications range from 3D mapping and navigation to online shopping, 3D printing, computational photography, computer video games, or cultural heritage archival.

The goal of an image-based 3D reconstruction algorithm can be de- scribed as ”given a set of photographs of an object or a scene, estimate
the most likely 3D shape that explains those photographs, under the assumptions of known materials, viewpoints, and lighting conditions” (See Figure 1.1).
