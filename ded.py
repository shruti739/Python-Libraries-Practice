
def argument(*args):
    print(args)       #packed output
    print(*args)      #unpacked output
argument(100)


def argument(*cool):  #we can pass anything inplace of args, * is madetory only
    print(cool)
    print(*cool)
argument(1, 2.3, 'abc', 'xyz', True)  # we can pass unlimited argument




#combination *args and **kwargs
def both(*args,**kwargs):
    print(args, kwargs)
both()                           #prints empty tuple and dict
both(1,2,3)                      #only single value passed, consider as args. prints tuple with value and empty dict
both(1,2,4,x=90,y=100)           #single value and key:value pair passed. prints tuple and dict with values

