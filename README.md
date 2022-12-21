# Motion Planning of Mbot Mega Robot on Qualcomm RB5 Platform

<p align="justify">
This project focuses on search-based planning algorithm to solve the problem of intercepting a moving target by feeding the shortest path to the robot. The maps are provided in form of 2D matrices with known initial positions of robot and target along with the obstacle locations. Results shows the success of current algorithm with plots of the paths tracked by both: robot and the target.
</p>

## Project Report
[Orish Jindal, 'A search-based motion planning algorithm to intercept a moving target](https://github.com/ojindal/Motion-Planning-Moving-target/blob/main/Orish%20PR2%20report.pdf)

## The images below represents the final map where the blue and red marks represent the robot and target position respectively, when the catching condition is met. Path travelled by the target is shown in Red and the path travelled by the robot is shown in Blue. Bigger
blue mark represents the initial position of the robot and the smaller one represents the final position after the catching condition is met. Initial position of target is shown in green, and the final position is shown by red mark as before.
<p align="center">
  <img src = "https://user-images.githubusercontent.com/89351094/208837683-f4e457ab-1d3a-4318-b63a-65891c27f78a.jpg"/>
 </p>
 
<p align="center">

  <img src = "https://user-images.githubusercontent.com/89351094/208837565-1a314959-1271-4376-b5c9-9c0e344c23c3.jpg"/>

</p>

## Details of code files (This is a class homework: ECE276B SP22 PR2)

Run the main.py
Current setting: it will plot the final position as well as path for the map 3.
To run other maps, change map name in two places: 

1) test_map
2) argument of 'plotting(path)'. (give path location of the map that you want to run)

#### Folder attached: Results
Contains the results

Other files attached:
#### 1. robotplanner.py

This file contains the algorythm RTAAstar which is used accordingly in the function robotplanner.
Also contains other small helper functions needed for the algorith.

#### 2. targetplanner.py
This file is not modified in any way (as instructed).

#### 3. main.py

This file contains test functions.

This file is almost same as given.
Changes:

1) from robotplanner import *
2) from path import * 
3) Arrays to store the states at each timestamp in order to use the data for plotting the path later
4) tqdm to track the time and number of iterations in real time
5) calling the 'plotting(path)' function at the end that plots the complete path (need to feed the map location)

#### 4. path.py

This contains 'plotting(path)' function that plots the stored path
