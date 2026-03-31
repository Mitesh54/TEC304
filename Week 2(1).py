def func(): 
    print("I am function func()!") 
print("cat", func, 42) 
objects = ["cat", func, 42] 
print(objects[1]) 
objects[1]() 
d = {"cat": 1, func: 2, 42: 3} 
print(d[func])