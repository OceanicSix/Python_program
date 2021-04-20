from threading import Timer




def foo():
    raise Exception

try:
    t=Timer(2,foo)
    t.daemon=True
    a=input("type soImething...")
except:
    print("all good")
