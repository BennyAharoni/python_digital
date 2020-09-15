from time import sleep

menu_id = input("Menu:\n----------\n"
                "1. Insert a number and ** it by 3.\n"
                "2. Insert 4 IPs to a list and print it.\n"
                "3. Insert 4 Entries of DNS and print it\n"
                "4. Input a string and check if it is a palindrome.\n"
                "Enter your choice: ")

if menu_id == "1":
    number = int(input("Enter a number: "))
    print(str(number) + " powered by 3 is: " + str(number ** 3))
elif menu_id == "2":
    ip_list = []
    ip_list.append(input("Enter new IP: "))
    ip_list.append(input("Enter new IP: "))
    ip_list.append(input("Enter new IP: "))
    ip_list.append(input("Enter new IP: "))
    print("The new list is:\n----------\n" + str(ip_list))
elif menu_id == "3":
    dns_dict = {}
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    print("The new dns_dict is:\n----------\n" + str(dns_dict))
elif menu_id == "4":
    word = input("Enter a string: ")
    if word == word[::-1]:
        print(word + " is a palindrome")
    else:
        print(word + " is not a palindrome")

else:
    print("Enter 1-4 only!")

print("\nIt was a nice game, Bye bye")
