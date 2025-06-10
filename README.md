# NumPlay_solver

## Purpose
Solve NumPlay problems.

## Method
1. Need python-sat to run solver.py
  ```
  pip install python-sat
  ```
2. Prepare NumPlay questions in .csv files. Here I have prepared some questions in /questions .
  The .csv file should be like:
  ```
  5,3,0,0,7,0,0,0,0
  6,0,0,1,9,5,0,0,0
  0,9,8,0,0,0,0,6,0
  8,0,0,0,6,0,0,0,3
  4,0,0,8,0,3,0,0,1
  7,0,0,0,2,0,0,0,6
  0,6,0,0,0,0,2,8,0
  0,0,0,4,1,9,0,0,5
  0,0,0,0,8,0,0,7,9
  ```
  Note that you can only use number 0 ~ 9, while 1 ~ 9 means the number filled in the box, and 0 means the box is empty.


3. Run solver.py, and you will see the words "Enter the path to csv file: ", enter your NumPlay question .csv file. Then you will see the words "Enter the max number of solutions to find: ", here you should enter the max solution numbers.  After this, you will get answers.
  ```
  $ python solver.py
  Enter the path to the csv file: questions/numplay_q1.csv
  Enter the max number of solutions to find: 3
  Solution 1:
  -------------------------------
  | 5  3  4 | 6  7  8 | 9  1  2 |
  | 6  7  2 | 1  9  5 | 3  4  8 |
  | 1  9  8 | 3  4  2 | 5  6  7 |
  ----------+---------+---------
  | 8  5  9 | 7  6  1 | 4  2  3 |
  | 4  2  6 | 8  5  3 | 7  9  1 |
  | 7  1  3 | 9  2  4 | 8  5  6 |
  ----------+---------+---------
  | 9  6  1 | 5  3  7 | 2  8  4 |
  | 2  8  7 | 4  1  9 | 6  3  5 |
  | 3  4  5 | 2  8  6 | 1  7  9 |
  -------------------------------
  ```

