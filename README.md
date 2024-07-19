# ReleasticEval-Data

## Project Structure

### task_code

​	single task_code directory 

```shell
├─t1
│  │  adapted.py
│  │  original.py
│  │  signature.py
│  │
│  ├─test
│  │  │  test.py
│  │  │
│  │  ├─input
│  │  │  ├─case1
│  │  │  ├─case2
│  │  │  └─case3
│  │  ├─output
│  │  │  ├─case1
│  │  │  ├─case2
│  │  │  ├─case3
```

`adated.py`:Based on the code implementation after changing the original code, the functions remain unchanged

`original.py`:Original code obtained on github

`signature.py`:Functional signature of the changed code

`test`:Test related folders

`test.py`:The test code contains all test cases

`input`:Different test case input

`output`:Different test case output

### task_json

​	task_json contain the task all info you nedd



