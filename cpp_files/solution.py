import os
import subprocess
import time
def start(executable_file):
    return subprocess.Popen(
        executable_file,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

def write_read(process, msg):
    return process.communicate(input=(msg+"\n").encode("utf-8"))[0].decode("utf-8")

def terminate(process):
    process.stdin.close()
    process.terminate()
    process.wait(timeout=0.2)

process = None #will replaced in preparation()
def preparation():
    cpp_file = "a.cpp"
    commands = f"g++ {cpp_file} -o output.o"
    os.system(commands)
    global process
    process = start(["./output.o"])

def solution(x):
    output = write_read(process, str(x))
    return output
    

# inp = [1, 2, 3, 4, 5]
# inp = [str(i) for i in inp]

# for i in inp:
#     process = start(["./output.o"])
#     print(write_read(process, i))
#     terminate(process)


