my_dict = {"Benny": 45, "Sara": 90, "Nachman": 100, "Bibi": 1000, "Ezra": 67}
sum = my_dict["Benny"] + my_dict["Ezra"]
print(sum)

my_dict.update({"Tamar": sum})
#Another way:
#my_dict["Tamar"] = sum

print("Number of elements in list: " + str(len(my_dict)))
print("idan" in my_dict)
