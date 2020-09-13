new_list1 = []
#new_list2 = list #Also a list
print(type(new_list1))
new_list = [2, 6.6, []]
print(new_list)
new_list2 = new_list + [77, "Hello"]
print(new_list2)
new_list3 = new_list2 + new_list
print(new_list3)
new_list3 = new_list2 * 2
print(new_list3)
print(new_list[0]) #first element
my_list = [1, 2, 3, 6, 54, "dudu cohen"]
print(my_list[4])
print("My age: " + str(my_list[4]))
my_list2 = list("1234567") #seperates to digits
print(my_list2)
my_string = 'A'.join(my_list2) #1A2A3A4A5A6A7
print(my_string)
my_list3 = my_string.split()
print(my_list3) #letters
my_string = "Hello Benny how are you?"
my_list3 = my_string.split()
print(my_list3) #words
my_string = "Hello Benny\nHow are you?"
my_list3 = my_string.splitlines()
print(my_list3) #lines
my_list = ["hello", "benny", 54]
print(len(my_list)) #3
my_str = "132iuyriuwqyrhiwqr"
print(len(my_str))

my_list.append("wow")
my_list.append("Benny")
print(my_list)
print("The length is:" + str(len(my_list)))
my_list.insert(4, "Rami") #insert "Rami" at place 4
print(my_list)

my_list.pop()
print(my_list) #remove the last
my_list.pop(1)
print(my_list) #remove the 2th

my_list = ["google", "ebay"]
print("google" in my_list) #True