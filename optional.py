def myopt(a ,b, c=None):
    if c is None:
        print(a,b)
    else:
        print(a,b,c)
myopt(1,2)

myopt(1,2,3)
