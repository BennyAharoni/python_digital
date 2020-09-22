filename = "C:/Users/Binyamin Aharoni/PycharmProjects/python_digital/bennyFile.txt"

'''file = open(filename, "r")
for line in file:
    print(line)
file.close()'''

file = open(filename, "r")
my_string = file.read()
file.close()
print(my_string)
#new_list = my_string.split("\n") #delimeter
new_list = my_string.splitlines()
print(type(new_list))
print(new_list)

#my_string = file.read(9) #9 letters of the file

fp = open(filename, "r")
for i, line in enumerate(fp):
    if i == 2: #3th line
        print("3th line is: " + line)
    '''elif i == 29:
        # 30th line
    elif i > 29:
        break'''
fp.close()

'''with open(filename) as fp:
    for i, line in enumerate(fp):
        if i == 25:
            # 26th line
        elif i == 29:
            # 30th line
        elif i > 29:
            break'''

f = open(filename)
lines = f.readlines()
print("3th line is: " + lines[2])
f.close()

f = open("C:/Users/Binyamin Aharoni/PycharmProjects/python_digital/hello.txt", "x") #creates a new file
f.close()