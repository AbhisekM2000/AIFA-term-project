# AIFA-term-project
# Heuristic Search Methods for Functional partitioning in Hardware-Software codesign
Group members<br/>
Abhisek Mohanty (18EC3AI20)<br/>
Aishik Mandal (18EC3AI21)<br/>
Hardhik Mohanty (18EE3AI26)<br/>
Samarth (18EC35051)<br/>

### Problem Statement
Given : A task graph with each node $`T_{i}`$ has hardware area cost $`h_{i}`$ and software execution time cost $`s_{i}`$<br/>
Let the binary decision variable be $`y_{i}`$. <br/>
$`y_{i} =1`$, if $`T_{i}`$ is implemented by Software, else if $`y_{i}`$=0, then it is implemented by hardware.<br/>
Optimization objective:<br/>
```math
\sum_{i}(1-y_{i})h_{i}
```
 
Subject to constraint:<br/>
```math
\sum_{i}y_{i}s_{i} \leq D
```

Where, $`D`$ denotes the total Software resources available
