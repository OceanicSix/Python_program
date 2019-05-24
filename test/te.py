import json

a={1:'1',
   2:[{2.1:"2.1",
       2.2:"2.2"}]}

b=a.get(2.1)
print(type(b))
print(b)