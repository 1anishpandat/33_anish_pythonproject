file = open("myfile.txt","w")
L=["this is lagos \n","this is python\n","this is Ecc\n"]

file.write("hello there\n")
file.writelines(L)
file=open("myfile.txt","r")
print(file.read())
file.cloese()
