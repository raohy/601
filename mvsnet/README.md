

### goal
  to develop a tool which can turn several 2d images of an object into a 3d model(expecially small objects)

### approach 
  deep learning:  MVSNet family 
  ![](/images/MVSNet.png)
### dataset
  dtu:
  
 ![](/images/cat_01.png) ![](/images/cat_11.png) ![](/images/cat_21.png)
  
  This dataset is aimed at multiple view stereo (MVS) evaluation.
  
  The data set consist of 124 different scenes, each scenes have about 48 images from different views. 44 of them consist mainly of scenes that have been rotatated and scanned four times with 90 degree intervals, which enables 360 degree models. 
  
  The scenes include a wide range of objects in an effort to span the MVS problem. At the same time, the data set also include scenes with very similar objects, e.g. model houses, such that intra class variability can be explored. The image resolution is 1600 x 1200. The camera positions and internal camera parameters have been found with high accuracy, via the matlab calibration toolbox, which is also the toolbox you need to retrieve these parameters. Lastly, the scenes have been recorded in all 49 or 64 scens with seven different lighting conditions from directional to diffuse.

### training results
   ![](/images/building1.png)![](/images/depth1.png)![](/images/probability1.png)
   
  &emsp;&emsp;&emsp;&emsp; inference image(without noises) &emsp; &emsp; &emsp; &emsp; &emsp;                 depth map        &emsp;&emsp; &emsp; &emsp; &emsp; &emsp; &emsp;&emsp; &emsp; &emsp; &emsp;        probability map                       
   
 depth map:reflects the distance of the object from the origin, and it is a way to represent 3d objects.
 
 probability map: reflects the depth estimation quality.
 
   ![](/images/sofa1.png)
   
   inference image(without noises)
   
 Through comparison, it can be found that mvsnet can greatly reconstruct 3d models without background disturbance. However, it cannot effectively eliminate background disturbance for objects with the noises. The generated 3d model will inevitably contain background noises.
 So if we want it to be a tool that can be used in any situations, the network should be improved.
 
 ### Sprint 3 Plan
  explore more algorithms or models and find solutions to eliminate background noises.
   
