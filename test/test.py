s="htb"
x = s.__class__.mro()[1].__subclasses__()
for i in range(len(x)):
    fn=x[i].__name__

    if fn.find("warning")>-1:
        print(i,fn)