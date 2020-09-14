from time import sleep

menu_id = input("Enter your chosen: ")
if menu_id == "1":
    number = int(input("Enter a number: "))
    print(str(number) + " powered by 3 is: " + str(number ** 3))
elif menu_id == "2":
    ip_list = ["1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"]
    print(ip_list)
elif menu_id == "3":
    dns_dict = {"www.google.com": "192.168.2.2", "www.ynet.com": "2.2.2.2", "www.apple.com": "3.3.3.3",
                "www.youtube.com": "4.4.4.4"}
    print(dns_dict)
elif menu_id == "4":
    str = input("Enter a string: ")
    if str == str[::-1]:
        print(str + " is a palindrome")
    else:
        print(str + " is not a palindrome")

else:
    print("Bye")

print("\nIt was a nice game, Bye bye")
