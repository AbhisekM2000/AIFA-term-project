# AIFA-term-project
# Heuristic Search Methods for Functional partitioning in Hardware-Software codesign
Group members<br/>
Abhisek Mohanty (18EC3AI20)<br/>
Aishik Mandal (18EC3AI21)<br/>
Hardhik Mohanty (18EE3AI26)<br/>
Samarth (18EC35051)<br/>

### Problem Statement
Given : A task graph with each node T<sub>i</sub> has hardware area cost h<sub>i</sub> and software execution time cost s<sub>i</sub><br/>
Let the binary decision variable be y_{i}. <br/>
y_{i} =1, if T_{i} is implemented by Software, else if y_{i}=0, then it is implemented by hardware.<br/>
Optimization objective:<br/>

![equation](https://latex.codecogs.com/svg.latex?%5Cbg_white%20%5Csum_%7Bi%7D%281-y_%7Bi%7D%29h_%7Bi%7D)

 
Subject to constraint:<br/>

![eqation](https://latex.codecogs.com/svg.latex?%5Cbg_white%20%5Csum_%7Bi%7Dy_%7Bi%7Ds_%7Bi%7D%20%5Cleq%20D)


Where, D denotes the total Software resources available
