# Python-Advanced-Concepts

Python must-have skills:
1. Dictionar, sets, lists
A set is unordered and contains unique elements. 
You can use set() to remove duplicates from list. 
Also a set can be ordered with the help of sorted()
2. Mutable and immutable data types
	mutable: list, dictionary, set.
	immutable: int, str, float, bool, tuple, etc. 
	mutable objects create aliases 
	immutable objects are easier to debug  but the down-side is that mutable objects are easier to do operations or changes to the objects.
[:] - this copies the list into a new object. 
3. Common methods in python 
4. File i/o operation. 

It is important to use context manager (with) to open the file as it closes the file after you exit the with block. 

"w" rewrites the whole file. hence, use "a" to append to the file. 
also to work with jpg and other files that require changing the file type to binary before reading and writing, use "rb" or "wb"

Intermediate skills: 

1. Object oriented programming (working and classess) and Inheritence (polymorphism)

makes our work easier by creating our own data structure to work on. 
We can create a class for our objects with data(atributes) to define their behaviour (methods) 
there are instance methods, class methods, and static methods.

using inheritence we can use all the attributes and methods of parent class and even overwrite it.

eg: HTTP exception inherits from Exception class

2. data structures (algoexpert.io) - efficiency and complexity 
3. list and dictionary comprehensions.  

comprehensions helps us avoid loops and is used for iterables. 

They help you avoid maps, filters and lambda
4. Collection module - {map and filter and lambda}
Lambda reduces a function into single line without  the  use  of def or return. 
map function iterates function(lambda or any other fuction) to each item. It basically combines lambda function and your variable.
filter is basically a condition on the list variable.

reduce function takes specified number of parameters  of the list and applies the function and does the same with the result and the rest of the list

so, basically you can either use comprehensions or lambda map and filter. The former is more suggested.

5. *args, and **kwargs 
These are used for packing and unpacking variables. 
*args takes arguments as tuple or sends a list into different variables while **kwargs takes arguments into dictionary or sends the values of the dictionary into variables.

unpacking is very important in the python programming. generally used. pass it as (*variable) or (**variable)

Optional parameters can have default values in case the functional is not passing. But while using mutable datatypes like List or dictionary it is advised to pass None instead of [] or {}

6. Dunder methods
It allows operator overloading
used in debugging. Eg: repr, str is a way of returning a readable object type

__name__ returns __main__ if python is running on te same file else it will return file name

7. making own modules  
8. Async IO
Asynchronous helps when your processor  is free to run the code as the code waits for some data base connection or other operation that is not dependent on processor.
we must await the tasks for them to finish else the program will not wait for them to finish and they will not be executed. 
use asyncio. - functions to create task. 
you can use threading to solve the problem. 

Advanced skills:
1. decorators and generators (efficient usage of memory)
decorators allow you to modify functionality without changing the structure
@property allows you to use an attribute like a method you can use both setters and deleters.

for class decorators
we can use class functions __int__ to pass function and __call__ to create a wraper and return the function back with new arguments or even same arguments.

one common usage of decorators is to create logging and check the time it takes for a function to run.

yield keyword makes a generator 
a generator returns an iterator object rather than a value so that the function resumes again from were it left off. 

generators help saving memory. whereas list will take a lot of memory and time to run.
2. Context managers
using context managers are the right way of operating with i/o operations where closing a file/process is required. we can create our own context manager by using @contextmanager decorator from context manager module
3. Metaclasses
4. concurrency and parallasim. (Global interpreter lock, multi processing and multi threading)
multi-threading is useful for the i/o operations wherein a lot of time is lost which can be avoided using concurrence.future.Threadpoolexecutor() similarly concurrence.future.Processpoolexecutor() helps with  reducing time related to cpu based operations to reduce the  process time of complex problems by sharing processors(as many as cores in the cpu)
5. Testing (Test driven programming)
This involves using Try, except, else, finally blocks
else runs if there is no exception. we can also raise our own exception with the help of raise keyword. finally blocks always  executes no matter what.
6. Build and manipulate packages 
7. Cython 
8. Rest API with python 


Beautiful soup :

it is a python package for webscraping and it parses html and xml files. 


