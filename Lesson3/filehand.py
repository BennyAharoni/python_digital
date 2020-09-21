#r - read
#w - write
#r+ - read & write
#a - append
#a+ - also read

filename = "C:/Users/Binyamin Aharoni/PycharmProjects/python_digital/bennyFile.txt"

file = open(filename, "r")
print(file.read())
file.close()

file = open(filename, "w")
file.write("192.168.10.1\n255.255.255.0\n")
file.close()

file = open(filename, "a")
file.write("192.168.10.3\n255.255.255.4\n")
file.close()

file = open(filename, "r")
print(file.read())
file.close()
