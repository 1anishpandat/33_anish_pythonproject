with open("a.txt","w") as f:
    f.write("hello world \n")
    f.write("this is the 2nd line")
try:
    
    with open("d.txt","r") as f:
        
    
        c = f.read()
except Exception as e:
    print("Error:")
print(c)