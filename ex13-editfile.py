from sys import argv
script, filename = argv
target = open(filename)
print("Press enter to view file")
input("Enter")
print(target.read())
#print(f"conten of file \n {target}",target.read())
print(f"We are going to erase {filename}")
print("If you dont want that , hit CTRL_c(^C).")
print("if you want that , hit RETURN.")
input("?")
print("Opening file ....")
target = open(filename,'w')
print("Truncating the file .Good bye")
target.truncate()
print("Now iam going to add three lines")
line1 = input("Line 1 : ")
line2 = input("line 2:")
line3 = input("line 3:")
print("I am goingt o write these file")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally , we we lose it")
target.close()
newfile = open("new.py")
print(newfile.read())