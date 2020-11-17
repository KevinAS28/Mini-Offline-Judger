#one or both below variables must be True
use_naive_solution = False 
use_constant_result = True

#implement this function, and set use_naive_solution True
# if you want use naive solution for your expected output
def naive_solution(x):
    import time
    time.sleep(0.5)
    return x


#args_results format: [
    # [arguments], #for solution function in solution module 
    # expected constant result,
    # use naive solution? True/False, 
    # use constant result? True/False 
    # ]
    
args_results = [
    [
        [1], #arguments for solution function in solution module
        "1", #expected result
        True, #set/add False in third elements for exception not judging the naive_solution (default=True)
        True, #set/add False in fourth for exception not judging the constant result (default=True)
    ],
    [
        [2], #arguments for solution function in solution module
        "2", #expected result
        True, #set/add False in third elements for exception not judging the naive_solution (default=True)
        True, #set/add False in fourth for exception not judging the constant result (default=True)
    ],
    [
        [3], #arguments for solution function in solution module
        "3", #expected result
        True, #set/add False in third elements for exception not judging the naive_solution (default=True)
        True, #set/add False in fourth for exception not judging the constant result (default=True)
    ],        
]

if __name__ ==  "__main__":
    print(naive_solution(1))