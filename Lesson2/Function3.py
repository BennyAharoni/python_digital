def calculating(a, b):
    sum = a + b
    return sum


def add_ip(list, ip1, ip2, ip3):
    list.append(ip1)
    list.append(ip2)
    list.append(ip3)
    return list


'''a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print("The new number is: " + str(calculating(a, b)))'''

ip_list = []
ip_n1 = input("Enter first ip: ")
ip_n2 = input("Enter second ip: ")
ip_n3 = input("Enter third ip: ")
ip_list = add_ip(ip_list, ip_n1, ip_n2, ip_n3)
print(str(ip_list) + " The length of the list is: " + str(len(ip_list)))