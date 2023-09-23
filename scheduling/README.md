## Generic

You may change input.txt to vary the input parameters.

First line is the type of scheduling to be used.

1 -> FCFS

2 -> SJF

3 -> Priority Scheduling

4 -> Round Robin

Second line is the number of processes.

Third line is space separated list of arrival times

Fourth line is space separated list of burst times.

Fifth line is space separated list of priority

### Question 1:

The input is in file `input.txt`

**FCFS :**

Average Wait Time : 16.5
Average Turn Around Time : 27

**SJF :**

Average Wait Time : 16.5
Average Turn Around Time : 27

**Priority Scheduling :**

Average Wait Time : 12.5
Average Turn Around Time : 23

**Round Robin. Time Quanta = 4 :**

Average Wait Time : 10
Average Turn Around Time : 20.5

**_Based of the above metrics, it is safe to say that Round Robin with Time Quanta 4 is the best choice_**

### Question 2:

Input is in file input2.txt

You may also run scheduling2.cpp

We have used the same program with minor change in the inputs. Since priority 4 is the highest here, we have subtracted all the priorities from 5 to have have same program working for both the questions.

**FCFS :**

Average Wait Time : 31.25
Average Turn Around Time : 57.5

**SJF :**

Average Wait Time : 23.75
Average Turn Around Time : 50

**Priority Scheduling :**

Average Wait Time : 23.75
Average Turn Around Time : 50

**Round Robin. Time Quanta = 4 :**

Average Wait Time : 47.75
Average Turn Around Time : 74

**_Based of the above metrics, it is safe to say that SJF or Priority Scheduling is the best choice_**
