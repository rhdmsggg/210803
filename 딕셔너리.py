#Dictionary.py
"""
d = dict(a=1, b=2, c=3)
print(d)
print('-------')
print(type(d))
print('-------')
color = {"apple":"red","banana":"yello"}
print(color)
print('-------')
color["cherry"] = "red"
print(color)
print('-------')
for item in color.items():
    print(item)
print('-------')
for k,v in color.items():
    print(k,v)  #print(key값,value값)
print('-------')
print(color)
del color["cherry"]
print(color)
print('-------')
color.clear()
print(color)
"""
print("id: %s, name: %s" % ("kim","홍길동"))
def add(a,b):
    return a+b
args = (3,4)
print(add(*args))   #은 튜플이다