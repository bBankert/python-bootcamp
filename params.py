# format is as follows
# a & b are positional args (basic stuff...)
# args are any number of positional args (just values / in format of tuple)
# kwargs are any number of keyword args (key value pairs in format of dictionary)
def foo(a, b, *args, **kwargs):
    print(a,b)
    print(args[:])

    for key in kwargs:
        print(key,kwargs[key])


foo(1,2,3,4,5,six=6,seven=7)