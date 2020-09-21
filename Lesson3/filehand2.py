filename = "C:/Users/Binyamin Aharoni/PycharmProjects/python_digital/bennyFile.txt"

'''file = open(filename, "r")
for line in file:
    print(line)
file.close()'''

file = open(filename, "r")
my_string = file.read()
file.close()
print(my_string)
my_list = my_string.split("\n") #delimeter
print(type(my_list))
print(my_list)