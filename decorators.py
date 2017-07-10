
# coding: utf-8

# ## Decorators are wrapper functions just look at some examples

# In[16]:

def my_first_decarator(func):
    print("I think the decorator will replace the replace the given function with wrapper function")
    print("Decorator will be called the moment we use the @decorator")
    def wrapper():
        print("Before executing the func")
        func()
        print("After Executing the func")
    return wrapper 


# In[17]:

@my_first_decarator
def print_hello_world():
    print("Hello world")


# In[18]:

print_hello_world()


# ## Let us understand decorators with params

# In[58]:

#first argument is always the function name
def param_decorator(param1, param2):
    print("First call to the param decorator")
    def real_param_decorator(func):
        print("Second call to the real param decorator")
        def wrapper(a):
            print("Printing the args")
            return func(a)
            print("Done with function execution")
        return wrapper
    return real_param_decorator


# In[59]:

@param_decorator(12,12)
def square(a):
    return a*a


# In[60]:

square(12)


# ## Building simple route app like stuff

# In[2]:

map = {}
def route(key):
    def real_router(func):
        map[key] = func
        def wrapper():
            return func()
        return wrapper
    return real_router
def execute(param):
    map[param]()


# In[3]:

@route("addition")
def add():
    print("I am addition")

@route("multiplication")
def church():
    print("I am multiplication")
    
@route("substraction")
def batting():
    print("I am substraction")


# In[4]:

execute("addition")


# In[5]:

execute("multiplication")


# In[6]:

execute("substraction")


# In[ ]:



