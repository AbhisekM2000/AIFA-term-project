# AIFA-term-project
# Heuristic Search Methods for Functional partitioning in Hardware-Software codesign
Group members<br/>
Abhisek Mohanty (18EC3AI20)<br/>
Aishik Mandal (18EC3AI21)<br/>
Hardhik Mohanty (18EE3AI26)<br/>
Samarth (18EC35051)<br/>

### Problem Statement
Given : A task graph with each node T<sub>i</sub> has hardware area cost h<sub>i</sub> and software execution time cost s<sub>i</sub><br/>
Let the binary decision variable be y<sub>i</sub>. <br/>
y<sub>i</sub> =1, if T<sub>i</sub> is implemented by Software, else if y<sub>i</sub>=0, then it is implemented by hardware.<br/>
Optimization objective:<br/>

![equation](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BWhite%7D%20%5Csum_%7Bi%7D%281-y_%7Bi%7D%29h_%7Bi%7D%7D)

 
Subject to constraint:<br/>

![eqation](https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BWhite%7D%20%5Csum_%7Bi%7Dy_%7Bi%7Ds_%7Bi%7D%5Cleq%20D%7D)


Where, D denotes the total Software resources available
