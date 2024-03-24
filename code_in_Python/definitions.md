# Python Definitions for Reference

    Higher Order Function:
    ----------------------
        -- if a Function takes another function as an argument or returns functions as a result.
        -- For Eg. Map function in Python takes a Function as an argument. 
    
    Free Variables:
    ----------------------
        -- When we Define a Higher order function, then the variables defined in that function are called Free Variables. 

    Closure:
    ----------------------
        -- Closure is an inner function that remembers and has access to variables in the local scope in which it was created, even after the 
            outer function has finished executing.
    
    Decorators:
    ----------------------
        -- A Decorator is a function that takes another function as an argument, add some fucntionality to it, 
            then returns another function. All this is done while leaving intact, the original function. 

    # Function to Generate Logs for the Functions passed as params

## Explanation of passing arguments to a function used as a Ddecorator

~~~python

def log_wrapper(func):
    print("*"*20)
    print(f'Function Starting.\nPassed functions {[x.__name__ for x in func]}')
    import logging
    logging.basicConfig(level = logging.INFO)

    print(f'\nLogging configured')

    def wrap_log(*args,**kwargs):
        print("Inside wrap_log function")

        logging.info(f'Logging {func[0].__name__}, args {args} and kwargs {kwargs}')
        return func[0](*args,**kwargs)
    
    def wrap_log2():
        print("Inside wrap_log function")

        logging.info(f'Logging {func[1].__name__}')
        return func()
    
    return wrap_log, wrap_log2

def dummy_func():
    print(f'Dummy')

sqr = log_wrapper([square_num,dummy_func])
print(f'\nThe Value of sqr variable is {[x.__name__ for x in sqr]}')
sqr[0](3)

~~~

    ### Explanation of why we pass arguments in the inner function

    When we define sqr = log_wrapper([func1,func2]),
    we are actually passing the function names to the main log wrapper function.
    At this point, sqr is pointing to a tuple containing "Function Names"

    To actually invoke the function, we use the inner definition, which takes any argument.
    Then does it's thing and returns the original function, now with the arguments.

    So, the first time, we are passing the address of the function. Then second time, we are taking the arguments,
    when we say "sqr[0](3)".

    Finally, when the function is returned at " return func[0](*args,**kwargs)", at this point,
    the function is actually called with the argument.

    At the final    " return wrap_log, wrap_log2", the value of the function with the argument is returned.

    '''

