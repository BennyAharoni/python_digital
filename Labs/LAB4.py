details_list = ["Benny", 54, "benny@gmail.com", "050-4545457"]
print("\nFull name: " + details_list[0] + "\nAge: " + str(details_list[1]) + "\nMail: " + details_list[2]
      + "\nPhone: " + details_list[3] + "\n")

ip_list = ["192.128.2.5", "10.10.0.2"]

ip_list.append("192.168.2.54")
ip_list.append("172.138.2.5")
ip_list.append("10.0.0.138")

ip_list.pop(2)
print("IP list length is: " + str(len(ip_list)) + "\nAnd the IP list: " + str(ip_list))
