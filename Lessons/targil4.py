my_dict = {"www.google.com": "8.8.8.8", "www.facebook.com": "7.7.7.7",
           "www.youtube.com": ["5.5.5.5", "4.4.4.4"]}

#my_dict2 = dict()

print(my_dict)

#my_dict.update({"www.ynet.com": "30.3.3.3", "www.groo.co.il": "88.88.88.88"})
#print(my_dict)

#or:

my_dict2 = {"www.ynet.com": "30.3.3.3", "www.groo.co.il": "88.88.88.88"}
my_dict.update(my_dict2)
print(my_dict)

print("Number of entries: " + str(len(my_dict)))
print(my_dict["www.google.com"]) #prints the value of google 8.8.8.8
#print(my_dict.values()) #all values

my_dict["www.google.com"] = "8.8.4.4"
print(my_dict["www.google.com"])

print("www.google.com" in my_dict) #True, search in keys
print("30.3.3.3" in my_dict.values()) #True, search in values

