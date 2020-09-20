a = "Benny"
b = "54"
c = "benny@gmail.com"
d = '''
Full name: Benny
Age: 54
'''

print(d)
print(a + "'s age is: " + str(b))
print("\nMy name is {} and my age is {m}\nMy mail is {}".format(a, b, m=c))
print("Benny" in "Benny Aharoni") #True
print("benny" in c) #True
print(c[0]) #b
print(c[-1] + c[-2]) #mo
print(c[1:-1]) #enny@gmail.co
print(c[6:]) #gmail.com //until the end
print(c[:]) #all the string
print(c[-1:3]) #nothing
print(c[1::2]) #from 2th step 2
print(c[::-1]) #reversed //useful!