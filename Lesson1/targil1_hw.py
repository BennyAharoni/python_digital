import datetime

print("Net4U, is the best place\n     ...in the world\n")

print(datetime.datetime.now())

a = input("Enter full name: ")
b = ' '.join(a[::-1])
print("#" + b + "#")

c = "abc.java".split(".")
print(type(c))
print(len(c))
print(c[len(c)-1])

x = int(input("Enter a number: "))
if x%2 ==0:
    print("The number is even")
else:
    print("The number is odd")

n = 20
d = {"x": 200}
l = [1, 3, 5]

print(type(n)()) #clean it
print(type(d)()) #clean it
print(type(l)()) #clean it

s = ' '.join("hihigukgukkkkkk").split()
print("len is: " + str(len(s)))
d = dict()
for el in s:
    if el in d:
        d.update({el: d[el]+1})
    else:
        d.update({el: 1})
print(d)