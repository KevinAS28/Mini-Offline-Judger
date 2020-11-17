# Mini Offline Judger
## Tired to upload your code to online judger and waiting for the result? Here is the answer
## Language supported: Python, C++/C (It's really easy to add another languages if you do a little bit python

#Concepts
Basically we just need to compare the expected outputs and our program outputs based from several inputs, but surely there are couple of additional features:
- Fast (Need to create shortcut in terminal / command line / CMD)
- Different project -> different IO
- Constant outputs and dynamic outputs (generated with naive/slow solution)
- Configureable

for python, it will import your solution module and run it, but in another languages (C/C++), the solutions will just compile and run a.cpp (default name).

#Preparation
Python requirements: 3.5+
We just need to add shortcut in our command line to call judge.py and able to pass arguments to it.
for C/C++ support, by default it's using g++ (it's easy to change it in cpp_files/solution.py (at preparation() function)

#Usage
Copy the content of py_files or cpp_files to your code directory. (You can make it faster if you add shortcut too)
Those folders contains the templates of the solutions file. The solution just print whatever it's input (integer)

But in this example, I will assume that you are not using any shortcut in command line, so you need to copy judge.py too
Test: `python3 judge.py`

Back to concepts, we need to compare the PROGRAM OUTPUT and EXPECTED OUTPUT based on SEVERAL INPUTS.
to specify the SEVERAL INPUTS, go to judgment.py, and you will see args_result list, which should contain lists too (2D array).
In each list, you need to specify at least 2 items, which is: [[list of inputs (String)], (String)EXPECTED_CONSTANT_OUTPUT)]

notice that, at top of judgment.py, there are also:
`use_naive_solution = False #If True, then all the outpus will compared with the naive solution function result
use_constant_result = True #If True, then all outputs will compared with the EXPECTED_CONSTANT_OUTPUT `
