def outer_function():
    vari = "Hi"
    def inner_function():
        print(vari)
    # return(inner_function)

# var1 = outer_function(inner_function)

# var1()

# var1()



# def decorator_employee(original_function):
#     def wrapper_function(*args, **kwargs):
#         print(args)
#         new_args = ['a'+ 's' for i in args]
#         return(original_function(*new_args,**kwargs))
#     return(wrapper_function)
#
# @decorator_employee
# def funct(*args,**kwargs):
#     print(args)
#
#
#
#
# funct('a', 'b', 'c')
from functools import wraps

def my_logging(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__),level=logging.INFO)
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info(
            'ran with arguments: {}, and keyword arguments: {}'.format(args,kwargs)
        )
        return original_function()
    return wrapper

def my_timingfunc(original_function):
    import time
    @wraps(original_function)
    def wrapper_time(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args,**kwargs)
        t2 = time.time()
        t3 = t2 - t1
        print('{} ran in: from {} to {} seconds in {}'.format(original_function.__name__, t1,t2,t3))
        return result
    return wrapper_time

@my_logging
@my_timingfunc
def display_info(*args, **kwargs):
    import time
    time.sleep(1)
    print('display ran with arguments {} and {}'.format(args,kwargs))


display_info('a','b','c','d',a='fine',b='veryfine',c='super')

