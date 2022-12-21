# ECE276B SP22 PR2

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

